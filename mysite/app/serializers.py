from rest_framework import serializers
from .models import *



class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name']


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year', 'fuel_type', 'transmission', 'mileage', 'price']


class AuctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id', 'car', 'start_price', 'min_price', 'status']


class BidSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = Bid
        fields = ['id', 'auction', 'buyer', 'amount', 'created_at']


class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'seller', 'buyer', 'rating', 'comment']
