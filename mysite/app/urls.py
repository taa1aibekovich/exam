from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user')
router.register(r'car', CarViewSet, basename='car')
router.register(r'auction', AuctionViewSet, basename='auction')
router.register(r'bid', BidViewSet, basename='bid')
router.register(r'feedback', FeedbackViewSet, basename='feedback')
urlpatterns = [
    path('', include(router.urls)),
]
