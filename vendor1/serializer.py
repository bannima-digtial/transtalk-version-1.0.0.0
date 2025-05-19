# from rest_framework import serializers
# from .models import ServiceModel, StatesofCountryModel, VendorModel

# class VendorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = VendorModel
#         fields = ['id', 'clientname', 'businessname', 'address','city','state','contact','email','website','remark','services','user_status']


# class ServiceInCitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VendorModel
#         fields = ['city']

# class ServiceCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceModel
#         fields = ['servicename']

# class AllCitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StatesofCountryModel
#         fields = "__all__" 