from rest_framework import generics
from rest_framework import permissions, filters
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from statistics import mean
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product, Rating

from products.serializers import ProductSerializer, RatingSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['name', 'price', 'id', 'rating']
    search_fields = ['name', 'price', 'id', 'rating']
    ordering_fields = ['name', 'price', 'id', 'rating']

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        price = serializer.validated_data.get('price')
        serializer.save(name=name, price=price)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        product_id = self.request.data["product_id"]
        product = get_object_or_404(Product, pk=product_id)

        author = self.request.user

        rating_queryset = Rating.objects.filter(product=product,
                                                author=author)

        if rating_queryset.exists():
            raise ValidationError("You Have Already rated this product!")

        serializer.save(product=product, author=author)

        avg_product_rating = mean(list(Rating.objects.filter(
            product=product).values_list('rating', flat=True)))

        product.rating = avg_product_rating
        product.save(update_fields=['rating'])


rating_list_create_view = RatingListCreateAPIView.as_view()
