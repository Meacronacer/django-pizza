from rest_framework import generics, status
from .models import Product
from .serializers import ProductSerializer, ProductGroupSerializer
from rest_framework.response import Response


class ProductGroupApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

    def get(self, request, *args, **kwargs):
      response = super().get(request, *args, **kwargs)
      group = {product["product_type"]: [] for product in response.data}
      {group[product["product_type"]].append(product) for product in response.data}

      return Response(group, status=status.HTTP_200_OK)   


class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'
