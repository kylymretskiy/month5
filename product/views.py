from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category , Product , Review
from .serializers import CategorySerializer , ProductSerializer , ReviewSerializer

@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories,many=True).data
    return Response(data=data,
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def category_detail_api_view(request, id):
     try:
         category = Category.objects.get(id=id)
     except Category.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Category does not exist!'})
     data = CategorySerializer(category).data
     return Response(data=data)


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Product does not exist!'})
    data = ProductSerializer(product).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review does not exist!'})
    data = ReviewSerializer(review).data
    return Response(data=data)