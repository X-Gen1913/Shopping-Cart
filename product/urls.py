from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    url(r'^add_to_cart/(?P<item_id>[-\w]+)/$',views.add_to_cart,name='add_to_cart'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$',views.delete_from_cart, name='delete_item'),
    path('cart/',views.order_details,name="order_summary"),
    path('product/new/', views.product_new, name='product_new'),

]

