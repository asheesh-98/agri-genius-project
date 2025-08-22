from django.views.generic import View
from django.http import HttpResponse
import os

class FrontendAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'frontend', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                "This URL is only used for the React app. Build your React app and try again.",
                status=501,
            )
