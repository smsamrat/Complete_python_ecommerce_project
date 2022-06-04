from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('search/', views.SearchProduct, name='SearchProduct'),
    path('category/<str:slug>/', views.categoryfetchItem, name='category'),
    path('category/<str:cat_slug>/<str:prod_slug>/', views.productDetails, name='product_details'),

]