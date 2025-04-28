from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Category, Product , Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = 'id name products_count'.split()

    def get_products_count(self, obj):
        return obj.products.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title description price category reviews average_rating'.split()

    def get_average_rating(self, Product):
        reviews = Product.reviews.all()
        if reviews:
            sum_reviews = sum([review.stars for review in reviews])
            average = sum_reviews / len(reviews)
            return average
        return None

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1 , max_length=255)
    description = serializers.CharField(default='No description')
    price = serializers.IntegerField()
    category_id = serializers.IntegerField(min_value=1)

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id

class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1 , max_length=255)

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1 , max_length=255)
    stars = serializers.IntegerField(min_value=1 , max_value=5)
    product_id = serializers.IntegerField(min_value=1)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Category does not exist')
        return product_id











