from django.urls import path
from product import views

urlpatterns = [
    path('categories/',views.CategoryListAPIView.as_view(),name='categories_list'),
    path('categories/<int:id>/',views.CategoryDetailListAPIView.as_view(),name='categories_details'),
    path('products/',views.ProductListAPIView.as_view(),name='products_list'),
    path('products/<int:id>/',views.ProductDetailListAPIView.as_view(),name='products_details'),
    path('reviews/',views.ReviewListAPIView.as_view(),name='reviews_list'),
    path('reviews/<int:id>/',views.ReviewDetailListAPIView.as_view(),name='reviews_details'),
]