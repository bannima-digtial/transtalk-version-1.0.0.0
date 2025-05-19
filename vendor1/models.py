from django.db import models

class ServiceModel(models.Model):
    servicename = models.CharField(max_length=30, default="")

    class Meta:
        db_table = "tb_service"
    
    def __str__(self):
        return self.servicename


# Supplier/Booking Agent Model
class VendorModel(models.Model):
    clientname = models.CharField(max_length=30, verbose_name= "Vendor Name")
    businessname = models.CharField(max_length=70)
    address = models.CharField(max_length=150)
    town = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    contact = models.CharField(max_length=100)
    fastconnect = models.IntegerField()
    email = models.EmailField(default="", blank=True)
    website = models.CharField(max_length=30, blank=True)
    # category = models.CharField(max_length=30)
    remark = models.TextField()
    services = models.TextField()
    ad_status = models.CharField(max_length=4)
    user_status = models.CharField(max_length=4)
    column_status = models.CharField(max_length=30, default="")
    f2 = models.CharField(max_length=30, default="")
    f3 = models.CharField(max_length=30, default="")
    entry_via = models.CharField(max_length=4, default="sys")

    category= models.ManyToManyField(ServiceModel)

    class Meta:
        db_table = "tb_vendor"
    def __str__(self):
        return self.businessname
        

# Advertisement
class AdvertiseModel(models.Model):
    ad_image = models.ImageField(upload_to='images/')
    ad_state = models.CharField(max_length=20)
    ad_for_client = models.ForeignKey(VendorModel, on_delete=models.CASCADE, related_name= "client_ad")
    ad_post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "advertisement"


class StatesofCountryModel(models.Model):
    statename = models.CharField(max_length=100)
    state_abbreviation = models.CharField(max_length=5)
    cityname = models.CharField(max_length=100)
    city_abbreviation = models.CharField(max_length=5)

    class Meta:
        db_table = "stateofcountry"

    def __str__(self):
        return self.statename

    
        
