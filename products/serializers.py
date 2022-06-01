from rest_framework import serializers
from products.models import Product, Rating
# from . import validators


class RatingSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Rating
        fields = [
            'author',
            'product_id',
            'rating'
        ]


class ProductSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(
        max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'rating',
            'updated_at'
        ]

    def validate_name(self, value):
        qs = Product.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                f"{value} is already a product name.")
        return value
