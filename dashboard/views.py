from django.shortcuts import render
from item.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    item = Item.objects.filter(created_by=request.user)
    return render(request, 'index.html',{
        'item':item,
    })