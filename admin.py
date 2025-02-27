from django.contrib import admin
from .models import Car, Location, Rental, Review

admin.site.register(Car)
admin.site.register(Location)
admin.site.register(Rental)
admin.site.register(Review)
# Register your models here.


admin.site.site_header = "Car Rental"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Dashboard"