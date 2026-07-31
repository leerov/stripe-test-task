from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:item_id>', views.item_detail, name='item_detail'),
    path('buy/<int:item_id>', views.buy_item, name='buy_item'),
    path('order/<int:order_id>/buy', views.buy_order, name='buy_order'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]