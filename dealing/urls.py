from .views import *
from django.urls import path

urlpatterns=[
    #url to create and list products
    path("products/" ,productpost.as_view(),name="Create-List-products"),
    #url to change or delete products
    path("products/<str:name>/" ,productchange.as_view(),name="Modify-products"),
    #url to create and list orders
    path("delivery/" ,DeliveryListCreateView.as_view(),name="Create-deliveries"),
     #url to delete orders
    path("delivery/delete/<int:reciever_id>/" ,DeliveryUD.as_view(),name="Modify-deliveries"),
    

           ]
