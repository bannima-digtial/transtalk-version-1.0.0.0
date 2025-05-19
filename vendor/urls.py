from django.urls import path
from . import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('', v.Dash.as_view()),
    path('supplier', v.Supplier.as_view(), name="supplier-view"),
    path('supplier/add', v.AddSupplier.as_view(),name="supplier-add"),
    path('supplier/profile/<int:pk>', v.ViewSupplier.as_view()),
    path('supplier/delete/<int:pk>',v.DeleteForm.as_view(), name="su-profile-delete"),
    path('su-delete/<int:pk>',v.DeleteProfile.as_view(), name="su-delete-profile-now"),
    path('supplier/update/<int:pk>',v.UpdateSupplierForm.as_view(), name="profile-update-form"),

    # booking agent
    path('bookingagent', v.BookingAgent.as_view()),
    path('bookingagent/add',v.AddBookingAgent.as_view()),
    path('bookingagent/profile/<int:pk>', v.ViewBookingAgent.as_view()),
    path('bookingagent/update/<int:pk>',v.UpdateBookingAgentForm.as_view(), name="bookingagent-profile-update-form"),
    path('bookingagent/delete/<int:pk>',v.BADeleteForm.as_view(), name="ba-profile-delete"),
    path('ba-delete/<int:pk>',v.BookingagentDeleteProfile.as_view(), name="ba-delete-profile-now"),
    # path('supplier/add', v.AddSupplier.as_view()),
    # path('delete',v.DeleteForm.as_view()),

    #Search
    path('supplier/search', v.searchSupplier.as_view(), name = 'search-supplier'),
    # SearchByName
    path('supplier/search/name', v.searchSupplierByName, name = 'search-supplier-byname'),
    # SearchByMobile
    path('supplier/search/mobile', v.searchSupplierByMobile, name = 'search-supplier-bymobile'),
    # SearchByAddress
    path('supplier/search/address', v.searchSupplierByAddress, name = 'search-supplier-byaddress'),

    #ad
    path('advertise',v.AdView.as_view(),name="advertise"),
    path('advertise/add', v.addAdvertisement.as_view(),name="advertise-add"),
    path('advertise/priority/<int:pk>', v.AdPriority.as_view(),name="advertise-priority"),
    path('advertise/priority/remove/<int:pk>', v.AdPriorityRemove.as_view(),name="advertise-priority-remove"),
    path('advertise/delete/confirm/<int:pk>', v.DeleteADComfirmation.as_view(),name="advertise-delete-confirm"),
    path('advertise/delete/<int:pk>', v.deleteAdvertisement.as_view(),name="advertise-delete"),

    #uploads
    path('upload', v.uploadXL.as_view(), name= "uploadxl"),

    #destination
    path('destination/add', v.DestinationView.as_view(), name="add-destination"),

    #add city with available service category
    path('city-service/', v.CityServiceCategoryView.as_view(), name="city-services"),
    path('city-service/add', v.AddCityServiceCategoryView.as_view(), name="city-services-add"),
    path('city-service/update/<int:pk>', v.UpdateCityServiceCategoryView.as_view(), name="city-services-update"),

    # api call for vendor
    path('api/bookingagent', v.getVendorBA.as_view() ,name = 'api-vendor-bookingagent'),
    path('api/bookingagent/all/<str:city>', v.getVendorBAcity ,name = 'api-vendorcity-bookingagent'),
    path('api/bookingagent/<int:id>', v.getRespVendorBA ,name = 'api-vendorspecific-bookingagent'),
    path('api/supplier', v.getVendorSU.as_view() ,name = 'api-vendor-supplier'),
    path('api/city', v.getVendorCity.as_view() ,name = 'api-city'),
    path('api/categories', v.getServiceCategory.as_view() ,name = 'api-servicecategory'),
    path('api/city-all', v.getAllCity.as_view(), name= 'api-allcity'),
    path('api/town/all/<str:city>', v.getAllTownInCity, name='api-alltownincity'),
    path('api/vendors/all/<str:city>', v.getVendorsInCity,name = 'api-allvendors-city'),
    path('api/town/vendors/<str:town>', v.getAllVendorInTown, name='api-allvendorintown'),
    path('api-search-vendor/<str:city>/<str:destiny>/<str:category>', v.searchVendor, name= 'api-searchvendor'),
    path('api/servicecategory/<str:city>', v.getServiceCategoryInCity, name='api-servicecategory-incity'),
    path('api/servicecategory/id/<int:id>',v.getServiceCategoryDetailsByID, name= "api-servicecategory-byid"),
    path('api-destination/<str:cityinitial>', v.getAllDestination, name= 'api-destination'),
    # show ad by city
    path('api-showadvertise/<str:cityname>', v.getAdbyCity, name= 'api-advertise-bycity'),

]


