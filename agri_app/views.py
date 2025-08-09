from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Crop, Listing, Feedback, DiseaseScan
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os, pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def home(request):
    crops = Crop.objects.all()[:6]
    return render(request, 'home.html', {'crops': crops})

def market(request):
    crops = Crop.objects.all()
    q = request.GET.get('q')
    if q:
        crops = crops.filter(name__icontains=q)
    return render(request, 'market.html', {'crops': crops})

def schemes(request):
    # load schemes from a JSON file if provided, else show sample
    schemes = [
        {'title': 'Pradhan Mantri Kisan Samman Nidhi', 'desc': 'Income support for farmers.'},
        {'title': 'Soil Health Card', 'desc': 'Soil testing and advisory.'},
    ]
    return render(request, 'schemes.html', {'schemes': schemes})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    listings = Listing.objects.filter(farmer=request.user)
    return render(request, 'dashboard.html', {'listings': listings})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@csrf_exempt
def feedback_submit(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        Feedback.objects.create(user=request.user if request.user.is_authenticated else None, message=msg)
        return JsonResponse({'status':'ok'})
    return JsonResponse({'status':'bad'}, status=400)

@csrf_exempt
def disease_scan(request):
    if request.method == 'POST' and request.FILES.get('image'):
        img = request.FILES['image']
        scan = DiseaseScan.objects.create(image=img)
        # load demo model
        model_path = os.path.join(BASE_DIR, 'disease_model', 'disease_model_demo.pkl')
        result = 'unknown'
        confidence = 0.0
        try:
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            # demo: model is a dict mapping filenames to labels for sample images
            # in production, replace with actual model.predict
            label = model.get('default_label', 'healthy')
            result = label
            confidence = 0.85
        except Exception as e:
            result = 'error'
        scan.result = result
        scan.confidence = confidence
        scan.save()
        return JsonResponse({'result': result, 'confidence': confidence})
    return JsonResponse({'status':'bad'}, status=400)
