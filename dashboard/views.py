from django.shortcuts import render, get_object_or_404
from item.models import Item, Category
from django.contrib.auth.decorators import login_required 

@login_required
def index(request):
    item = Item.objects.filter(created_by=request.user)
    category = Category.objects.all()
    return render(request, 'dashboard/index.html',{
        'items':item,
        'categories':category
    })

