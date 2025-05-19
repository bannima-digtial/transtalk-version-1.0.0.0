from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from .models import DestinationModel, StatesofCountryModel, VendorModel, AdvertiseModel, ServiceModel
from .serializer import AdvertiseSerializer, AllCitySerializer, CityServiceCategorySerializer, DestinationSerializer, VendorSerializer, ServiceInCitySerializer, ServiceCategorySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
import xlrd
from tablib import Dataset
from .resources import UploadXLResource
from django.core.paginator import Paginator

# forms
from .form import CityServiceCategoryForm, DestinationForm, UploadXLForm, VendorForm, BookingVendorForm, AdForm


# DashBoard
class Dash(View):
    def get(self, request):
        return render(request, "home.html")



# Supplier class
# class Supplier(TemplateView):
#     template_name = "supplier.html"
#     model = VendorModel
#     limit = 5
#     offset = 0
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['dataset'] = self.model.objects.all().exclude(column_status = "del")[self.offset:self.limit]
#         self.offset += self.limit
#         return context
        # return render(request, self.template_name, context)

class Supplier(View):
    def get(self, request):
        queryset = VendorModel.objects.all().exclude(column_status = "del")
        pagination = Paginator(queryset, 20)
        page =  request.GET.get('page')
        context = {"dataset" : pagination.get_page(page)}
        return render(request, "supplier.html", context)
        

# Add Supplier
class AddSupplier(View):
    def get(self,request):
        frm = VendorForm()
        context = {"form": frm}
        return render(request, 'addsupplier.html', context)

    def post(self, request):
        # Vendor.objects.all().values([businessname=request.POST.get["businessname"]])
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/supplier")
    
class ViewSupplier(TemplateView):
    template_name = "supplier_profile.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = VendorModel.objects.get(id=kwargs['pk'])
        return context
    
class UpdateSupplierForm(View):
    def get(self, request, pk):
        formdata = VendorModel.objects.get(id=pk)
        form = VendorForm(instance= formdata)
        context = {"form":form}
        return render(request, "addsupplier.html",context)
    
    def post(self, request, pk):
        formdata = VendorModel.objects.get(id=pk)
        form = VendorForm(request.POST, instance= formdata)
        if form.is_valid():
            form.save()
        return redirect("/supplier/profile/{}".format(pk))



# Booking Agent class
class BookingAgent(TemplateView):
    template_name = "bookingagent.html"
    model = VendorModel
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dataset'] = self.model.objects.filter(services = "BA").exclude(column_status = "del")
        return context    

# Add Booking CLass
class AddBookingAgent(View):
    def get(self,request):
        frm = BookingVendorForm()
        context= {'form': frm}
        return render(request, 'addbookingagent.html',context)
    
    def post(self, request):
        frm = BookingVendorForm(request.POST)
        if frm.is_valid():
            frm.save()
        print("saved Booking")
        return redirect('/bookingagent')
    
class ViewBookingAgent(TemplateView):
    template_name = "bookingagent_profile.html"
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["data"] = VendorModel.objects.filter(services="BA").get(id=kwargs['pk'])
        return context
    
class UpdateBookingAgentForm(View):
    def get(self, request, pk):
        formdata = VendorModel.objects.filter(services = "BA").get(id=pk)
        form = BookingVendorForm(instance=formdata)
        context = {"form":form}
        return render(request, "addbookingagent.html",context)
    
    def post(self, request, pk):
        formdata = VendorModel.objects.get(id=pk)
        forminput = BookingVendorForm(request.POST, instance=formdata)
        if forminput.is_valid():
            forminput.save()
        return redirect('/bookingagent')
    



# Delete Vendor(both Supplier)

class DeleteForm(TemplateView):
    # Render Delete Form to Delete
    # if press Yes, it will update form to disabled
    # instead of delete it permanently

    template_name = "deleteform.html"
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['id'] = kwargs['pk']
        return context
    
# Update Profile to disable mode
#for SUpplier Only
class DeleteProfile(RedirectView):
    url = "/supplier"
    # pattern_name = "supplier-view"
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['pk']
        vendor = VendorModel.objects.get(pk=del_id)
        vendor.column_status = 'del'
        vendor.save()
        return super().get_redirect_url(*args, **kwargs)
    
# Search Supplier
class searchSupplier(View):
    def get(self, request):
        return render(request, "search.html")
    
def searchSupplierByName(request):
    if request.method == "GET":
        name = request.GET.get('searchbyname')
        if name:
            queryset = VendorModel.objects.filter(businessname__istartswith = name)
            serializer = VendorSerializer(queryset, many=True)
            context = {"dataset": tuple(serializer.data), "searchkeyname" : name, "namemsg": ""} # convert dataset from list to tuple
            return render(request, "search.html", context)
        
        context= {"namemsg": "Enter Valid Vendor Name"}
        return render(request, "search.html", context)
    
def searchSupplierByAddress(request):
    if request.method == "GET":
        addr = request.GET.get('searchbyaddress')
        if addr:
            queryset = VendorModel.objects.filter(address__contains = addr)
            serializer = VendorSerializer(queryset, many=True)
            context = {"dataset": tuple(serializer.data), "searchkeyaddr" : addr, "addrmsg": ""} # convert dataset from list to tuple
            return render(request, "search.html", context)
        
        context= {"addrmsg": "Field cannot be blank"}
        return render(request, "search.html", context)

    
def searchSupplierByMobile(request):
    if request.method == "GET":
        mob = request.GET.get('searchbymob')
        if mob:
            if len(mob) == 10: 
                queryset = VendorModel.objects.filter(contact__contains=str(mob))
                serializer = VendorSerializer(queryset, many=True)
                # return Response(serializer.data)
                print(serializer.data)
                context = {"dataset": tuple(serializer.data), "searchkeymob" : mob, "mobmsg": ""} # convert dataset from list to tuple
                return render(request, "search.html", context)
        context= {"mobmsg": "Enter Valid Mobile Number"}
        return render(request, "search.html", context)
        
    

# Delete Vendor(both Supplier & Booking Agent)

class BADeleteForm(TemplateView):
    # Render Delete Form to Delete
    # if press Yes, it will update form to disabled
    # instead of delete it permanently

    template_name = "ba-deleteform.html"
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['id'] = kwargs['pk']
        return context
    
# Update Profile to disable mode
# for booking agent only
class BookingagentDeleteProfile(RedirectView):
    url = "/bookingagent"
    # pattern_name = "supplier-view"
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['pk']
        vendor = VendorModel.objects.get(pk=del_id)
        vendor.column_status = 'del'
        vendor.save()
        return super().get_redirect_url(*args, **kwargs)
    
# Show All ADVERTISMENTS
class AdView(View):
    def get(self, request):
        queryset = AdvertiseModel.objects.all()
        pagination = Paginator(queryset, 20)
        page =  request.GET.get('page')
        context = {"dataset" : pagination.get_page(page)}
        return render(request, "advertise.html", context)

# Add Ad Image FOrm
class addAdvertisement(View):
    def get(self, request):
        form = AdForm()
        context = {"form":form}
        return render(request, "adform.html",context)
    
    def post(self, request):
        form = AdForm(request.POST, request.FILES)
        # if form.is_valid():
        form.save()
        form = AdForm()
        context = {"form":form, "msg": "Advertisement Posted Successfully"}
        return render(request, "adform.html", context)
        # return HttpResponse("Something Went Wrong")

class DeleteADComfirmation(TemplateView):
    # Render Delete Form to Delete
    # if press Yes, it will update form to disabled
    # instead of delete it permanently

    template_name = "deletead.html"
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['id'] = kwargs['pk']
        return context

# Delete Advertise
class deleteAdvertisement(View):
    def get(self, request, pk):
        print(pk)
        queryset = AdvertiseModel.objects.filter(pk=pk).delete()
        return redirect("/advertise")
    
# AD PRIORITY
class AdPriority(View):
    def get(self, request, pk):
        print(pk)
        queryset = AdvertiseModel.objects.filter(ad_priority='Y')
        if queryset:
            print("PRIORITY EXIST")
            print(queryset.update(ad_priority='N'))
            print("PRIORITY REMOVED")
            priorityqueryset = AdvertiseModel.objects.filter(pk=pk).update(ad_priority='Y')
        else:
            priorityqueryset = AdvertiseModel.objects.filter(pk=pk).update(ad_priority='Y')
        return redirect("/advertise")
    
    
class AdPriorityRemove(View):
    def get(self, request, pk):
        print(pk)
        queryset = AdvertiseModel.objects.filter(pk=pk).update(ad_priority='N')
        return redirect("/advertise")

class DestinationView(View):
    def get(self, request):
        form = DestinationForm()
        context = {"form":form}
        return render(request, "adddestination.html",context)
    
    def post(self, request):
        form = DestinationForm(request.POST, request.FILES)
        # if form.is_valid():
        form.save()
        return redirect('/destination/add')
        # return render(request, "adddestination.html")
        # return HttpResponse("Something Went Wrong")

class CityServiceCategoryView(View):
    def get(self, request):
        queryset = StatesofCountryModel.objects.all()
        context = {'dataset':queryset}
        return render(request, 'citycategory.html', context)
    

class AddCityServiceCategoryView(View):
    def get(self, request):
        form = CityServiceCategoryForm()
        context = {"form":form}
        return render(request, "addcitycategory.html",context)
    
    def post(self, request):
        form = CityServiceCategoryForm(request.POST, request.FILES)
        # if form.is_valid():
        form.save()
        return redirect('/city-service/add')
        # return render(request, "adddestination.html")
        # return HttpResponse("Something Went Wrong")

class UpdateCityServiceCategoryView(View):
    def get(self, request, pk):
        formdata = StatesofCountryModel.objects.get(id=pk)
        form = CityServiceCategoryForm(instance= formdata)
        context = {"form":form}
        return render(request, "addcitycategory.html",context)
    
    def post(self, request, pk):
        formdata = StatesofCountryModel.objects.get(id=pk)
        form = CityServiceCategoryForm(request.POST, instance= formdata)
        if form.is_valid():
            form.save()
        return redirect("/city-service")


class getVendorBA(generics.ListAPIView):
    queryset = VendorModel.objects.filter(category="1")
    serializer_class = VendorSerializer  

@api_view()
def getVendorBAcity(requests,city):
    print("========",city)
    queryset = VendorModel.objects.filter(category="1").filter(city=city)
    serializer = VendorSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def getRespVendorBA(requests,id):
    print("========r",id)
    print(type(id))
    queryset = VendorModel.objects.get(id=id)
    serializer = VendorSerializer(queryset)
    return Response(serializer.data)
        
    
        
    
 

class getVendorSU(generics.ListAPIView):
    queryset = VendorModel.objects.all().exclude(column_status='del')
    serializer_class = VendorSerializer
    # pagination_class = LimitOffsetPagination

class getVendorCity(generics.ListAPIView):
    queryset = VendorModel.objects.values("city").distinct()
    serializer_class = ServiceInCitySerializer

class getServiceCategory(generics.ListAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceCategorySerializer

class getAllCity(generics.ListAPIView):
    queryset = StatesofCountryModel.objects.all()
    serializer_class = AllCitySerializer

# Get All Town in City
@api_view() 
def getAllTownInCity(self, city):
    queryset = VendorModel.objects.only('local').exclude(column_status='del').filter(city=city)
    serializer = VendorSerializer(queryset, many=True)
    return Response(serializer.data)
        
# Get All Vendors in Town City
@api_view() 
def getAllVendorInTown(self, town):
    queryset = VendorModel.objects.all().exclude(column_status='del').filter(local=town)
    serializer = VendorSerializer(queryset, many=True)
    return Response(serializer.data)


# Search Vendors in Town City
@api_view()
def searchVendor(self, city, destiny, category):
    queryset = VendorModel.objects.exclude(column_status='del').filter(category__exact = category).filter(city=city).filter(remark__contains=destiny)
    serializer = VendorSerializer(queryset, many=True)
    print(queryset)
    return Response(serializer.data)

# Search All Vendors in City
@api_view()
def getVendorsInCity(self, city):
    queryset = VendorModel.objects.all().exclude(column_status='del').filter(city=city)
    serializer = VendorSerializer(queryset, many=True)
    return Response(serializer.data)

# Available Service Category in City
@api_view()
def getServiceCategoryInCity(self, city):
    queryset = StatesofCountryModel.objects.only('category').filter(cityname=city)
    serializer = CityServiceCategorySerializer(queryset, many=True)
    # print(queryset)
    return Response(serializer.data)

# Get Service Category Detail by id
@api_view()
def getServiceCategoryDetailsByID(self, id):
    queryset = ServiceModel.objects.get(id=id)
    serializer = ServiceCategorySerializer(queryset)
    print(queryset)
    return Response(serializer.data)

    
# Load All Destination for Search
@api_view()
def getAllDestination(self, cityinitial):
    # queryset = DestinationModel.objects.all().filter(city=destiny)
    queryset = DestinationModel.objects.filter(destiny_name__istartswith = cityinitial).values()
    serializer = DestinationSerializer(queryset, many=True)
    return Response(serializer.data)

# Load All Ads in City
@api_view()
def getAdbyCity(self, cityname):
    # getstate = StatesofCountryModel.objects.get(cityname=cityname)
    print(cityname,"--------------------------------------------------------------------------------------")
    queryset = AdvertiseModel.objects.filter(ad_city__iexact = cityname)
    serializer = AdvertiseSerializer(queryset, many=True)
    print(queryset)
    return Response(serializer.data)


    
# Upload XL
class uploadXL(View):
    def get(self,request):
        form = UploadXLForm()
        context = {"form":form}
        return render(request,"upload_xl.html", context)
    
    def post(self,request):
        # form = UploadXLForm(request.POST, request.FILES)
        
        # # print("ddddddddddddddddddddddddddddddddd",list(request.FILES))

        # if form.is_valid():
        #     form.save()

        # a = xlrd.open_workbook("f{list(request.FILES)}")
        # print("===============================",a)
        # return redirect("/upload")
        uploadxl_resource = UploadXLResource()
        dataset = Dataset()
        new_file = request.FILES['filename']
        imported_data = dataset.load(new_file.read(), format = 'xlsx')
        for data in imported_data:
            value = VendorModel(
                clientname = data[7],
                businessname = data[0],
                address = data[1],
                local = data[2],
                city = data[3],
                state = data[4],
                contact = data[6],
                fastconnect = data[10],
                email = data[8],
                website = data[9],
                remark = data[5],
                services = "",
                user_status = "FREE",
                ad_status = "",
                column_status = "",
                f2 = "",
                f3 = "",
                entry_via = "xls"

            )
            value.save()
        form = UploadXLForm()
        context = {"form":form, 'msg': "File Uploaded Successfully"}
        return render(request, "upload_xl.html",  context)



    
    