from rest_framework import serializers
from api.models import Product, Rating

from django.contrib.auth import get_user_model


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


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_superuser(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", )
