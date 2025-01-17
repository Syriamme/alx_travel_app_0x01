from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'created_at']
    
    def validate_price_per_night(self, value):
        """Ensure the price per night is a positive value."""
        if value <= 0:
            raise serializers.ValidationError("Price per night must be a positive value.")
        return value

    def validate_location(self, value):
        """Ensure the location is not empty."""
        if not value:
            raise serializers.ValidationError("Location cannot be empty.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user_name', 'check_in_date', 'check_out_date', 'created_at']

    def validate_user_name(self, value):
        """Ensure the user name is not empty."""
        if not value:
            raise serializers.ValidationError("User name cannot be empty.")
        return value

    def validate(self, data):
        """Ensure the check-out date is after the check-in date."""
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')

        if check_out_date <= check_in_date:
            raise serializers.ValidationError("Check-out date must be after check-in date.")
        return data
