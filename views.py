from django.shortcuts import render
from django.http import JsonResponse
from rekap_api.models import rekap

# Create your views here.
def rekap_list(request):
    Erekap = rekap.objects.all() # Complex Date
    Erekap_python = list(Erekap.values()) # Python DS
    return JsonResponse({
        'Erekap': Erekap_python
    })