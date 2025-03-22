from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category, Order, Order_Item
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer, OrderItemSerializer
import json
from rest_framework import generics
from rest_framework import status
from django.db.models import Q

@api_view(['GET'])
def display(request):

    routes = [
        'MY FIRST REST RESPONSE ON DJANGO'
    ]

    return Response(routes)


@api_view(['GET', 'PUT', 'DELETE'])
def all_Products(request):
    products = Product.objects.all()
    product_serialzer = ProductSerializer(products, many=True)
    return Response(product_serialzer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def view_product(request, slug):
    product = Product.objects.get(slug=slug)
    product_serializer = ProductSerializer(product, many=False)
    return Response(product_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def all_categories(request):
    category = Category.objects.all()
    category_serializer = CategorySerializer(category, many=True)
    return Response(category_serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def view_category_products(request, slug):
    category_queried = Category.objects.get(slug=slug)
    category_products = Product.objects.filter(category_id=category_queried)

    item = []

    for prod in category_products:
        products = Product.objects.get(slug=prod.slug)
        item.append(products.regular_price)

    products_serializer = ProductSerializer(category_products, many=True)
    print(item)
    return Response(products_serializer.data)


class OrderView(generics.CreateAPIView):
    order_queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemView(generics.CreateAPIView):
    item_queryset = Order_Item.objects.all()
    serializer_class = OrderItemSerializer


@api_view(['GET'])
def search_products(request):
    query = request.query_params.get("search")
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class SearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get("searchview", None)
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(slug__icontains=query))
        return products