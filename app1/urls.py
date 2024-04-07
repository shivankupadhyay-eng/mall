from django.urls import path
from app1 import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . tokens import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(serializer_class=CustomTokenRefreshSerializer), name='token_refresh'),
    path('employees/', views.EmployeeListCreate.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroy.as_view(), name='employee-retrieve-update-destroy'),
    path('product/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('product/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('customer/', views.CustomerListCreate.as_view(), name='customer-list-create'),
    path('customer/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
    path('bills/', views.BillListCreate.as_view(), name='bill-list-create'),
    path('bills/<int:pk>/', views.BillRetrieveUpdateDestroy.as_view(), name='bill-retrieve-update-destroy'),
]
