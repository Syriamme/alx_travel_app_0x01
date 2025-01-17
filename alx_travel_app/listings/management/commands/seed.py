from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
import random
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample listings
        listings = [
            {"title": "Cozy Beach House", "description": "A lovely beach house with a great view.", "price_per_night": 150, "location": "Malibu"},
            {"title": "Mountain Retreat", "description": "A peaceful retreat in the mountains.", "price_per_night": 120, "location": "Colorado"},
            {"title": "City Apartment", "description": "An apartment in the heart of the city.", "price_per_night": 100, "location": "New York"},
        ]
        
        for listing_data in listings:
            listing = Listing.objects.create(**listing_data)
            self.stdout.write(f"Listing {listing.title} created!")

            # Create sample bookings for each listing
            for _ in range(random.randint(1, 5)):  # Random number of bookings per listing
                user_name = f"User{random.randint(1, 100)}"
                check_in_date = date.today() + timedelta(days=random.randint(1, 30))
                check_out_date = check_in_date + timedelta(days=random.randint(1, 7))
                Booking.objects.create(
                    listing=listing,
                    user_name=user_name,
                    check_in_date=check_in_date,
                    check_out_date=check_out_date
                )

            # Create sample reviews for each listing
            for _ in range(random.randint(1, 3)):  # Random number of reviews per listing
                user_name = f"User{random.randint(1, 100)}"
                rating = random.randint(1, 5)
                comment = f"Great place! Rating: {rating}/5."
                Review.objects.create(
                    listing=listing,
                    user_name=user_name,
                    rating=rating,
                    comment=comment
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample data!'))
