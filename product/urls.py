from django.urls import path
from . import views


urlpatterns = [
    # path('product/', views.product),
    path('category-create/<int:pk>/', views.CategoryListView.as_view()),
    path('product-create/<int:pk>/', views.ProductView.as_view()),
]
