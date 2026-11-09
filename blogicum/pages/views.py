from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    temlate = 'pages/index.html'
    # return render(request, temlate)
    return JsonResponse({'temlate': temlate})
