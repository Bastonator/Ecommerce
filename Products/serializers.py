from .models import Product, Category, Order, Order_Item
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    #order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source='order.id')
    #product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product.slug')

    class Meta:
        model = Order_Item
        fields = '__all__'

    #def create(self, validated_data):
     #   item = Order_Item.objects.create(order=validated_data['order']['id'], product=validated_data['product']['slug'],
      #                                   quantity=validated_data['quantity'], total_price=validated_data['total_price'])

       # return item
