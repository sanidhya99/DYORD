from .views import *
from django.urls import path

urlpatterns=[
    path("products/" ,productpost.as_view(),name="Create-List-products"),
    path("products/<str:name>/" ,productchange.as_view(),name="Modify-products"),
    path("delivery/" ,DeliveryListCreateView.as_view(),name="Create-deliveries"),
    # path("delivery/delete/<int:reciever_id>/" ,DeliveryUD.as_view(),name="Modify-deliveries"),
    

           ]