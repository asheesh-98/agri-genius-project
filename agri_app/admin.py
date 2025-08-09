from django.contrib import admin
from .models import Crop, Listing, Feedback, DiseaseScan

admin.site.register(Crop)
admin.site.register(Listing)
admin.site.register(Feedback)
admin.site.register(DiseaseScan)
