from rest_framework import serializers
from .models import CartItem, Order, OrderItem
from food.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'item', 'quantity']


class OrderItemWriteSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all())

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']


class OrderItemReadSerializer(serializers.ModelSerializer):
    item = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemReadSerializer(many=True, read_only=True)
    item_data = OrderItemWriteSerializer(many=True, write_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ['id', 'user', 'address', 'created_at', 'status', 'items', 'item_data']  # 👈 added 'item_data'
        read_only_fields = ['id', 'created_at', 'status']

    def create(self, validated_data):
        item_data_list = validated_data.pop('item_data')  
        order = Order.objects.create(**validated_data)
        for item_data in item_data_list:
            OrderItem.objects.create(order=order, **item_data)
        return order


