from rest_framework import serializers
from .models import AdvertiseModel, ServiceModel, StatesofCountryModel, VendorModel, DestinationModel

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ['id','servicename']

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset = ServiceModel.objects.all())
    class Meta:
        model = VendorModel
        fields = ['id', 'clientname', 'businessname', 'address','local','city','state','contact','fastconnect','email','website','remark','services','user_status','payment','subscription_period','profile_status','category']


class ServiceInCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = ['city']

# Service Category Available in city
class CityServiceCategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset = ServiceModel.objects.all())
    class Meta:
        model = StatesofCountryModel
        fields = ['statename','state_abbreviation','cityname','city_abbreviation','category']


class AllCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StatesofCountryModel
        fields = "__all__" 

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationModel
        fields = ['destiny_name']

class AdvertiseSerializer(serializers.ModelSerializer):
    # client_ad = serializers.PrimaryKeyRelatedField(many=True, queryset = VendorModel.objects.all())
    
    class Meta:
        model = AdvertiseModel
        fields = ['ad_image','ad_city', 'ad_type','ad_priority','client_ad']