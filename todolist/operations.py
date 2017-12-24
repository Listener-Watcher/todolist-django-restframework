from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import *
from datetime import datetime
# Create your views here.

def delete(request, id):
    if request.user.is_authenticated():
        Item.objects.filter(user=request.user,id=id).delete()
        item_all = Item.objects.all().filter(user=request.user).order_by("finished")
        context = {
            'item_all':item_all,
        }
        return render(request, 'board.html', context)
    else:
        return redirect('/accounts/login')

def finished(request, id):
    if request.user.is_authenticated():
        item = Item.objects.filter(user=request.user,id=id)
        if item[0].finished == "INCOMPLETE":
            item.update(finished="COMPLETE")
        else:
            item.update(finished="INCOMPLETE")
        item_all = Item.objects.all().filter(user=request.user).order_by("finished")
        context = {
            'item_all':item_all,
        }
        return render(request, 'board.html', context)
    else:
        return redirect('/accounts/login')

def edit(request, id):
    if request.user.is_authenticated():
        item = Item.objects.filter(user=request.user,id=id)[0]
        if item.end == None:
            item.end = datetime.now
        form = ItemForm(request.POST or None, instance=item)
        context = {
    		"form": form
    	}
        if form.is_valid():
            form.save()
            return redirect('/board')
        return render(request, 'edit.html', context)
    else:
        return redirect('/accounts/login')