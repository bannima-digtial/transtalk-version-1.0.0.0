# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic.base import TemplateView, RedirectView
# from .models import StatesofCountryModel, VendorModel, AdvertiseModel, ServiceModel
# from .serializer import AllCitySerializer, VendorSerializer, ServiceInCitySerializer, ServiceCategorySerializer
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# # forms
# from .form import VendorForm, BookingVendorForm, AdForm


# # DashBoard
class Dash(View):
    def get(self, request):
        return render(request, "home.html")



# # Supplier class
# class Supplier(TemplateView):
#     template_name = "supplier.html"
#     model = VendorModel
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['dataset'] = self.model.objects.filter(services = "SU").exclude(column_status = "del")
#         return context
#         # return render(request, self.template_name, context)

# # Add Supplier
# class AddSupplier(View):
#     def get(self,request):
#         frm = VendorForm()
#         context = {"form": frm}
#         return render(request, 'addsupplier.html', context)

#     def post(self, request):
#         # Vendor.objects.all().values([businessname=request.POST.get["businessname"]])
#         form = VendorForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("/supplier")
    
# class ViewSupplier(TemplateView):
#     template_name = "supplier_profile.html"
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = VendorModel.objects.filter(services="SU").get(id=kwargs['pk'])
#         return context
    
# class UpdateSupplierForm(View):
#     def get(self, request, pk):
#         formdata = VendorModel.objects.filter(services = "SU").get(id=pk)
#         form = VendorForm(instance= formdata)
#         context = {"form":form}
#         return render(request, "addsupplier.html",context)
    
#     def post(self, request, pk):
#         formdata = VendorModel.objects.get(id=pk)
#         form = VendorForm(request.POST, instance= formdata)
#         if form.is_valid():
#             form.save()
#         return redirect("/supplier/profile/{}".format(pk))



# # Booking Agent class
# class BookingAgent(TemplateView):
#     template_name = "bookingagent.html"
#     model = VendorModel
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['dataset'] = self.model.objects.filter(services = "BA").exclude(column_status = "del")
#         return context    

# # Add Booking CLass
# class AddBookingAgent(View):
#     def get(self,request):
#         frm = BookingVendorForm()
#         context= {'form': frm}
#         return render(request, 'addbookingagent.html',context)
    
#     def post(self, request):
#         frm = BookingVendorForm(request.POST)
#         if frm.is_valid():
#             frm.save()
#         print("saved Booking")
#         return redirect('/bookingagent')
    
# class ViewBookingAgent(TemplateView):
#     template_name = "bookingagent_profile.html"
#     def get_context_data(self, **kwargs): 
#         context = super().get_context_data(**kwargs)
#         context["data"] = VendorModel.objects.filter(services="BA").get(id=kwargs['pk'])
#         return context
    
# class UpdateBookingAgentForm(View):
#     def get(self, request, pk):
#         formdata = VendorModel.objects.filter(services = "BA").get(id=pk)
#         form = BookingVendorForm(instance=formdata)
#         context = {"form":form}
#         return render(request, "addbookingagent.html",context)
    
#     def post(self, request, pk):
#         formdata = VendorModel.objects.get(id=pk)
#         forminput = BookingVendorForm(request.POST, instance=formdata)
#         if forminput.is_valid():
#             forminput.save()
#         return redirect('/bookingagent')
    



# # Delete Vendor(both Supplier)

# class DeleteForm(TemplateView):
#     # Render Delete Form to Delete
#     # if press Yes, it will update form to disabled
#     # instead of delete it permanently

#     template_name = "deleteform.html"
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['id'] = kwargs['pk']
#         return context
    
# # Update Profile to disable mode
# #for SUpplier Only
# class DeleteProfile(RedirectView):
#     url = "/supplier"
#     # pattern_name = "supplier-view"
#     def get_redirect_url(self, *args, **kwargs):
#         del_id = kwargs['pk']
#         vendor = VendorModel.objects.get(pk=del_id)
#         vendor.column_status = 'del'
#         vendor.save()
#         return super().get_redirect_url(*args, **kwargs)
    

# # Delete Vendor(both Supplier & Booking Agent)

# class BADeleteForm(TemplateView):
#     # Render Delete Form to Delete
#     # if press Yes, it will update form to disabled
#     # instead of delete it permanently

#     template_name = "ba-deleteform.html"
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(*args,**kwargs)
#         context['id'] = kwargs['pk']
#         return context
    
# # Update Profile to disable mode
# # for booking agent only
# class BookingagentDeleteProfile(RedirectView):
#     url = "/bookingagent"
#     # pattern_name = "supplier-view"
#     def get_redirect_url(self, *args, **kwargs):
#         del_id = kwargs['pk']
#         vendor = VendorModel.objects.get(pk=del_id)
#         vendor.column_status = 'del'
#         vendor.save()
#         return super().get_redirect_url(*args, **kwargs)
    


# # Add Ad Image FOrm
# class AdView(View):
#     def get(self, request):
#         form = AdForm()
#         context = {"form":form}
#         return render(request, "adform.html",context)
    
#     def post(self, request):
#         form = AdForm(request.POST, request.FILES)
#         # if form.is_valid():
#         form.save()
#         return render(request, "adform.html")
#         # return HttpResponse("Something Went Wrong")


# class getVendorBA(generics.ListAPIView):
#     queryset = VendorModel.objects.filter(services="BA")
#     serializer_class = VendorSerializer  

# @api_view()
# def getVendorBAcity(requests,city):
#     print("========",city)
#     queryset = VendorModel.objects.filter(services="BA").filter(city=(city.upper()))
#     serializer = VendorSerializer(queryset, many=True)
#     return Response(serializer.data)


# @api_view()
# def getRespVendorBA(requests,id):
#     print("========r",id)
#     print(type(id))
#     queryset = VendorModel.objects.get(id=id)
#     serializer = VendorSerializer(queryset)
#     return Response(serializer.data)
        
    
        
    
 

# class getVendorSU(generics.ListAPIView):
#     queryset = VendorModel.objects.filter(services="SU")
#     serializer_class = VendorSerializer

# class getVendorCity(generics.ListAPIView):
#     queryset = VendorModel.objects.values("city").distinct()
#     serializer_class = ServiceInCitySerializer

# class getServiceCategory(generics.ListAPIView):
#     queryset = ServiceModel.objects.all()
#     serializer_class = ServiceCategorySerializer

# class getAllCity(generics.ListAPIView):
#     queryset = StatesofCountryModel.objects.all()
#     serializer_class = AllCitySerializer


    