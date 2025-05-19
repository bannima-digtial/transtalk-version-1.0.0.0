from django.urls import path
from . import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('', v.Dash.as_view()),
    # path('supplier', v.Supplier.as_view(), name="supplier-view"),
    # path('supplier/add', v.AddSupplier.as_view(),name="supplier-add"),
    # path('supplier/profile/<int:pk>', v.ViewSupplier.as_view()),
    # path('supplier/delete/<int:pk>',v.DeleteForm.as_view(), name="su-profile-delete"),
    # path('su-delete/<int:pk>',v.DeleteProfile.as_view(), name="su-delete-profile-now"),
    # path('supplier/update/<int:pk>',v.UpdateSupplierForm.as_view(), name="profile-update-form"),

    # # booking agent
    # path('bookingagent', v.BookingAgent.as_view()),
    # path('bookingagent/add',v.AddBookingAgent.as_view()),
    # path('bookingagent/profile/<int:pk>', v.ViewBookingAgent.as_view()),
    # path('bookingagent/update/<int:pk>',v.UpdateBookingAgentForm.as_view(), name="bookingagent-profile-update-form"),
    # path('bookingagent/delete/<int:pk>',v.BADeleteForm.as_view(), name="ba-profile-delete"),
    # path('ba-delete/<int:pk>',v.BookingagentDeleteProfile.as_view(), name="ba-delete-profile-now"),
    # # path('supplier/add', v.AddSupplier.as_view()),
    # # path('delete',v.DeleteForm.as_view()),

    # #ad
    # path('advertise',v.AdView.as_view(),name="advertise"),

    # # api call for vendor
    # path('api/bookingagent', v.getVendorBA.as_view() ,name = 'api-vendor-bookingagent'),
    # path('api/bookingagent/all/<str:city>', v.getVendorBAcity ,name = 'api-vendorcity-bookingagent'),
    # path('api/bookingagent/<int:id>', v.getRespVendorBA ,name = 'api-vendorspecific-bookingagent'),
    # path('api/supplier', v.getVendorSU.as_view() ,name = 'api-vendor-supplier'),
    # path('api/city', v.getVendorCity.as_view() ,name = 'api-city'),
    # path('api/categories', v.getServiceCategory.as_view() ,name = 'api-servicecategory'),
    # path('api/city-all', v.getAllCity.as_view(), name= 'api-allcity')
]


