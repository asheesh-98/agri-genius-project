from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from agri_app.models import Crop, Listing

class Command(BaseCommand):
    help = 'Load sample crops, users and listings'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        u, _ = User.objects.get_or_create(username='farmer1')
        if not u.has_usable_password():
            u.set_password('farmer123')
            u.save()
        crops = [
            {'name': 'Wheat', 'category':'Cereal', 'description':'High quality wheat', 'avg_price':25.0},
            {'name': 'Rice', 'category':'Cereal', 'description':'Basmati rice', 'avg_price':40.0},
            {'name': 'Tomato', 'category':'Vegetable', 'description':'Fresh tomatoes', 'avg_price':15.0},
        ]
        for c in crops:
            Crop.objects.get_or_create(name=c['name'], defaults=c)
        # create listing
        crop = Crop.objects.first()
        Listing.objects.get_or_create(farmer=u, crop=crop, quantity=100, price=2000.0)
        self.stdout.write(self.style.SUCCESS('Sample data loaded.'))
