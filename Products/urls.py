from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderView, OrderItemView, SearchView


urlpatterns = [
    path('', views.display, name="api"),
    path('products', views.all_Products, name="all_products"),
    path('product/<slug:slug>', views.view_product, name="view_products"),
    path('category', views.all_categories, name="all_categories"),
    path('category/<slug:slug>', views.view_category_products, name="category_products"),
    path('order', OrderView.as_view(), name="create_order"),
    path('order_items', OrderItemView.as_view(), name="create_order_items"),
    path('search_results', views.search_products, name="search-results"),
    path('search_view', SearchView.as_view(), name="search-view")
]
