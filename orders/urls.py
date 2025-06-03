from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import CartItemViewSet, OrderViewSet, OrderItemViewSet
from django.conf import settings
from django.conf.urls.static import static 


router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-items', OrderItemViewSet, basename='orderitem')


urlpatterns = [
    
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
