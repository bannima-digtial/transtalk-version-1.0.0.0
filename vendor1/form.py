# from django import forms
# from .models import VendorModel, ServiceModel, AdvertiseModel, StatesofCountryModel
# from django.db.models import Count

# # list of state in country
# stateslist = StatesofCountryModel.objects.values("statename","state_abbreviation").distinct()
# # print(stateslist)
# STATE_CHOICES = [("disabled",'Select State')]

# for state in stateslist:
#     # STATE_CHOICES.append((state.state_abbreviation,state.statename))
#     STATE_CHOICES.append((state['state_abbreviation'],state['statename']))

# citieslist = StatesofCountryModel.objects.values("cityname","city_abbreviation")   
# CITY_CHOICES = []
# for city in citieslist:
#     CITY_CHOICES.append((city['city_abbreviation'],city['cityname']))

# USER_TYPE = [('FREE','FREE'),('PAID','PAID')]


# # Vendor Form For BookingAgent
# class BookingVendorForm(forms.ModelForm):
#     class Meta:
#         model = VendorModel
#         # fields = "__all__"
#         fields = ["clientname","businessname","user_status","address","city","state","contact","email","website","remark","services"]
#         widgets = {
#             'clientname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Supplier Name'}),
#             'businessname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Name'}),
#             'user_status' : forms.Select(attrs={'class': 'form-control'}, choices=USER_TYPE),
#             'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Address'}),
#             'city': forms.Select(attrs={'class': 'form-control'}, choices=CITY_CHOICES),
#             'state': forms.Select(attrs={'class': 'form-control'}, choices=STATE_CHOICES),
#             'contact': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Contact'}),
#             'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Email'}),
#             'website': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Website'}),
#             'remark': forms.Textarea(attrs={'class': 'form-control','rows':'3'}), 
#             'services': forms.TextInput(attrs={'class': 'd-none','value':'BA','readonly':'true'}),
#             'user_status' : forms.Select(attrs={'class': 'form-control'}, choices=USER_TYPE),
#         }

# # Vendor Form For SUpplier
# class VendorForm(forms.ModelForm):
#     class Meta:
#         model = VendorModel
#         # fields = "__all__"
#         fields = ["clientname","businessname","user_status","address","local","city","state","contact","fastconnect","email","website","remark","services","category"]
#         widgets = {
#             'clientname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Supplier Name'}),
#             'businessname': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Name'}),
#             'user_status' : forms.Select(attrs={'class': 'form-control'}, choices=USER_TYPE),            
#             'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Business Address'}),
#             'local': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Local Town'}),
#             'city': forms.Select(attrs={'class': 'form-control'}, choices=CITY_CHOICES),
#             'state': forms.Select(attrs={'class': 'form-control'}, choices=STATE_CHOICES),
#             'contact': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Contact'}),
#             'fastconnect': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Fast Connect Number'}),
#             'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Email'}),
#             'website': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Website'}),
#             'remark': forms.Textarea(attrs={'class': 'form-control','rows':'3'}), 
#             'services': forms.TextInput(attrs={'class': 'd-none','value':'SU','readonly':'true'}),
#             'category': forms.CheckboxSelectMultiple()
#         }


# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = ServiceModel
#         fields = ["servicename"]

# # stateslist1 = VendorModel.objects.values("state").distinct()

# # STATE_CHOICES1 = []
# # for state in stateslist1:
# #     STATE_CHOICES1.append((state,state))





# # STATE_CHOICES1 = [("maharashtra","mh"),("haryana","hr"),("nagaland","nl"),("bihar","br"),]

# class AdForm(forms.ModelForm):
#     class Meta:
#         model = AdvertiseModel
#         fields = ['ad_image','ad_state','ad_for_client']
#         CHOICES = (VendorModel.objects.values("state"))
#         widgets = {
#             'ad_image': forms.FileInput(attrs={'class': 'form-control'}),
#             'ad_state': forms.Select(attrs={'class': 'form-control'},choices=STATE_CHOICES),
#             'ad_for_client': forms.Select(attrs={'class': 'form-control'})
#         }
        