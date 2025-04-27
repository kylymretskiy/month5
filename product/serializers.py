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
    reviews = ReviewSerializer(many=True)
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