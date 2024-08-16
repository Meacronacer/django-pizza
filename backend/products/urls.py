
from django.urls import path
from .views import ProductApiView, ProductGroupApiView

urlpatterns = [
    path('products-list/', ProductGroupApiView.as_view())
]