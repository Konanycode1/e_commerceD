from django.shortcuts import render,get_object_or_404, HttpResponse
from store.models import Produit
# Create your views here.

def base(request):
    
    return render(request, 'base.html',)

def index(request):
    produits = Produit.objects.all()

    context = {
        'produits': produits
    }

    return render(request, 'index.html',context)

def produit(request, slug):
    produits = get_object_or_404(Produit, slug=slug )
    context = {
        "produits":produits
    }
    return render(request, 'detail.html', context )
