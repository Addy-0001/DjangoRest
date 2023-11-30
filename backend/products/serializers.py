from rest_framework import serializers
from .models import Product

#A good thing about this is that you can have multiple serializers for the same model. 
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        print(obj.id)
        # obj.user -> user.username
        return obj.get_discount
