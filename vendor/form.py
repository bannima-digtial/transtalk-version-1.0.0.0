from django import forms
from .models import DestinationModel, VendorModel, ServiceModel, AdvertiseModel, StatesofCountryModel, UploadXL
from django.db.models import Count

# list of state in country
stateslist = StatesofCountryModel.objects.values("statename","state_abbreviation").distinct()
# print(stateslist)
STATE_CHOICES = [("disabled",'Select State')]

for state in stateslist:
    # STATE_CHOICES.append((state.state_abbreviation,state.statename))
    STATE_CHOICES.append((state['statename'],state['statename']))

citieslist = StatesofCountryModel.objects.values("cityname","cityname")   
CITY_CHOICES = []
for city in citieslist:
    CITY_CHOICES.append((city['cityname'],city['cityname']))

USER_TYPE = [('FREE','FREE'),('PAID','PAID')]
PROFILE_STATUS = [('HIDE', 'HIDE'),('SHOW','SHOW')]


# Vendor Form For BookingAgent
class BookingVendorForm(forms.ModelForm):
    class Meta:
        model = VendorModel
        # fields = "__all__"
        fields = ["clientname","businessname","user_status","address","city","state","contact","email","website","remark","services"]
        widgets = {
            'clientname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Supplier Name'}),
            'businessname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Name'}),
            'user_status' : forms.Select(attrs={'class': 'form-control'}, choices=USER_TYPE),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Address'}),
            'city': forms.Select(attrs={'class': 'form-control'}, choices=CITY_CHOICES),
            'state': forms.Select(attrs={'class': 'form-control'}, choices=STATE_CHOICES),
            'contact': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Contact'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Email'}),
            'website': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Website'}),
            'remark': forms.Textarea(attrs={'class': 'form-control','rows':'3'}), 
            'services': forms.TextInput(attrs={'class': 'd-none','value':'BA','readonly':'true'}),
            'user_status' : forms.Select(attrs={'class': 'form-control'}, choices=USER_TYPE),
        }

# Vendor Form For SUpplier
class VendorForm(forms.ModelForm):
    class Meta:
        model = VendorModel
        # fields = "__all__"
        fields = ["clientname","businessname","user_status","address","local","city","state","contact","fastconnect","email","website","remark","services","payment","subscription_period","profile_status","category"]
        widgets = {
            'clientname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Supplier Name'}),
            'businessname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Name'}),
            'user_status' : forms.Select(attrs={'class': 'form-control'}, choices=USER_TYPE),            
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Address'}),
            'local': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Local Town'}),
            'city': forms.Select(attrs={'class': 'form-control'}, choices=CITY_CHOICES),
            'state': forms.Select(attrs={'class': 'form-control'}, choices=STATE_CHOICES),
            'contact': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Contact'}),
            'fastconnect': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Fast Connect Number'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Email'}),
            'website': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Website'}),
            'remark': forms.Textarea(attrs={'class': 'form-control','rows':'3'}), 
            'payment': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Payment Amount Received'}), 
            'subscription_period': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Subscription Duration'}), 
            'profile_status': forms.Select(attrs={'class': 'form-control'}, choices=PROFILE_STATUS),
            'services': forms.TextInput(attrs={'class': 'd-none','value':'SU','readonly':'true'}),
            'category': forms.CheckboxSelectMultiple()
        }

class CityServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = StatesofCountryModel
        fields = ['statename','state_abbreviation','cityname','city_abbreviation','category']
        widgets = {
            'statename': forms.TextInput(attrs={'class': 'form-control','placeholder':'State Name'}),
            'state_abbreviation': forms.TextInput(attrs={'class': 'form-control','placeholder':'MH'}),
            'cityname' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'City Name'}),            
            'city_abbreviation': forms.TextInput(attrs={'class': 'form-control','placeholder':'City Name'}),
            'category': forms.CheckboxSelectMultiple()
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        fields = ["servicename"]

# stateslist1 = VendorModel.objects.values("state").distinct()

# STATE_CHOICES1 = []
# for state in stateslist1:
#     STATE_CHOICES1.append((state,state))





# STATE_CHOICES1 = [("maharashtra","mh"),("haryana","hr"),("nagaland","nl"),("bihar","br"),]

class AdForm(forms.ModelForm):
    class Meta:
        model = AdvertiseModel
        fields = ['ad_image','ad_city','ad_type','client_ad']
        CHOICES = (VendorModel.objects.values("state"))
        ADTYPE = {("box","Box"), ("full","Full")}
        ADPRIORITY = {("Y","YES"), ("N","NO")}
        widgets = {
            'ad_image': forms.FileInput(attrs={'class': 'form-control'}),
            'ad_city': forms.Select(attrs={'class': 'form-control'},choices=CITY_CHOICES),
            'ad_type' : forms.Select(attrs={'class': 'form-control'},choices=ADTYPE),
            'ad_priority' : forms.Select(attrs={'class': 'form-control'},choices=ADPRIORITY),
            'client_ad': forms.Select(attrs={'class': 'form-control'})
        }
        

class UploadXLForm(forms.ModelForm):
    class Meta:
        model = UploadXL
        fields = ['filename']
        widgets = {
            'filename' : forms.FileInput(attrs={'class':'form-control','accept':'.xlsx','name':'filename'})
        }


class DestinationForm(forms.ModelForm):
    class Meta:
        model = DestinationModel
        fields = ["destiny_name"]
        widgets = {
            'destiny_name': forms.TextInput(attrs={'class': 'form-control'})
         }
