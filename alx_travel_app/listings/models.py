from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking for {self.listing.title} by {self.user_name}"

class Review(models.Model):
    listing = models.ForeignKey(Listing, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for {self.listing.title} by {self.user_name}"
