from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('departments/', views.DepartmentList.as_view(), name='department_list'),
    path('departments/<int:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    path('items/', views.ItemList.as_view(), name='item_list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='item_detail')
]
