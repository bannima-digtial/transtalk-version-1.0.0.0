from django.db import models

class ServiceModel(models.Model):
    servicename = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "tb_service"
    
    def __str__(self):
        return self.servicename
    

class UploadXL(models.Model):
    filename = models.FileField()

    class Meta:
        db_table = "tb_xl"

    def __str__(self):
        return self.filename


# Supplier/Booking Agent Model
class VendorModel(models.Model):
    clientname = models.CharField(max_length=30, verbose_name= "Vendor Name", null = True, blank=True)
    businessname = models.CharField(max_length=150, null = True)
    address = models.CharField(max_length=150, null = True)
    local = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, null = True)
    state = models.CharField(max_length=30, null = True)
    contact = models.CharField(max_length=100, null = True)
    fastconnect = models.IntegerField(default=None, null = True)
    email = models.EmailField(default="", null = True, blank=True)
    website = models.CharField(max_length=30, default = "", null = True, blank=True)
    # category = models.CharField(max_length=30)
    remark = models.TextField(blank=True)
    services = models.TextField(blank=True)
    ad_status = models.CharField(max_length=4, null = True)
    user_status = models.CharField(max_length=4, null = True)
    payment = models.CharField(max_length=10, null=True, default=0)
    subscription_period = models.CharField(default="", null=True, max_length=10 )
    profile_status = models.CharField(default="SHOW", null=True, max_length=4 )
    column_status = models.CharField(max_length=30, default="")
    f2 = models.CharField(max_length=30, default="")
    f3 = models.CharField(max_length=30, default="")
    entry_via = models.CharField(max_length=4, default="sys")

    category= models.ManyToManyField(ServiceModel, related_name= 'servicemodeldetail')

    class Meta:
        db_table = "tb_vendor"
    def __str__(self):
        return self.businessname
        

# Advertisement
class AdvertiseModel(models.Model):
    ad_image = models.ImageField(upload_to='images/')
    ad_city = models.CharField(max_length=20)
    client_ad = models.ForeignKey(VendorModel, on_delete=models.CASCADE, related_name= "client_ad")
    ad_type = models.CharField(max_length=4, blank=True, default='1')
    ad_priority = models.CharField(max_length=4, blank=True, default='N')
    ad_post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "advertisement"


class StatesofCountryModel(models.Model):
    statename = models.CharField(max_length=100)
    state_abbreviation = models.CharField(max_length=5)
    cityname = models.CharField(max_length=100)
    city_abbreviation = models.CharField(max_length=100)
    category= models.ManyToManyField(ServiceModel, related_name= 'city_service_category')

    class Meta:
        db_table = "stateofcountry"

    def __str__(self):
        return self.statename
    

class DestinationModel(models.Model):
    destiny_name = models.CharField(max_length=60)

    class Meta:
        db_table = "tb_destinations"

    def __str__(self) -> str:
        return self.destiny_name
    
        
