from django.http import HttpResponse

def home(request):
    return HttpResponse("AgriGenius is running successfully from deployment zip!")