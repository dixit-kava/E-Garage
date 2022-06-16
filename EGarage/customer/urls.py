
from django.urls import path
from customer import views as cviews


urlpatterns = [
    path('',cviews.chome,name='indexx'),
    path('customer/<str:pk_test>/', cviews.customer, name='customer'),
    path('services',cviews.service,name='service'),
    path('create_order',cviews.createOrder,name='create_order'),
    path('update_order/<str:pk>/', cviews.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', cviews.deleteOrder, name="delete_order"),
]
