from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from rest_framework import status,generics
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import ItemSerializer
INCREASE = ''
DECREASE = '-'
sort_by = {'priority':INCREASE, 'deadline':DECREASE}
def index(request):
	if request.user.is_authenticated():
		item_all = Item.objects.all().filter(user=request.user).order_by("begin","finished")
		context = {
			'item_all':item_all,
		}
	else:
		return redirect('/accounts/login')
		
def details(request,id):
	if request.user.is_authenticated():
		item = Item.objects.get(id=id)
		context= {
		'item':item,
		}
		return render(request,'details.html',context)
	else:
		return redirect('/accounts/login')
		
def add(request):
	if request.user.is_authenticated():
		form = ItemForm(request.POST or None)
		context = {
			"form":form
		}
		if form.is_valid():
			form.save()
			item = Item.objects.filter(title=form.data['title'])
			item.update(user=request.user)
			print form.data
			return redirect('/board')
		return render(request,'add.html',context)
	else:
		return redirect('/accounts/login')

def board(request):
    global sort_by, INCREASE, DECREASE
    if request.user.is_authenticated():
        KEY = ''
        if request.method == "POST":
            KEY = request.POST.get("priority")
            if KEY is None:
                KEY = request.POST.get("deadline")
            if KEY == 'priority' or KEY == 'deadline':
                if sort_by[KEY] == INCREASE:
                    sort_by[KEY] = DECREASE
                else:
                    sort_by[KEY] = INCREASE
            else:
                KEY = ''
        if KEY != '':
            print sort_by[KEY] + KEY
            item_all = Item.objects.all().filter(user=request.user).order_by("finished", sort_by[KEY] + KEY)
        else:
            item_all = Item.objects.all().filter(user=request.user).order_by("begin","finished")
        context = {
            'item_all':item_all,
        }
        return render(request, 'board.html', context)
    else:
        return redirect('/accounts/login')


class ItemList(generics.ListCreateAPIView):
    def get(self, request, format=None):
        item = Item.objects.all().order_by('begin')
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)
    @permission_classes((IsAdminUser, ))
    def Item(self, request, format=None):
        user = request.user
        serializer = ItemSerializer(data=request.data, context={'user':user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_REQUEST)
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer