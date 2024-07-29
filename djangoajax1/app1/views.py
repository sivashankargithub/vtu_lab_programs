from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse

def json_time(request):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return JsonResponse({'param1': current_time})

def live_time(request):
    return render(request, 'app1/index.html')
