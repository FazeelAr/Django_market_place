from django.shortcuts import render, redirect
from .forms import SignUpForm
from item.models import Category, Item
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request,'index.html', {
        'categories':categories,
        'items': items,
    }) 


def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {
        'form': form,
    })