from django.shortcuts import render
from django.conf import settings
from .forms import SignUpForm
from .models import SignUp
from django.core.mail import send_mail
# Create your views here.
def home(request):
	title = "Sign up and use it now!"
	if request.user.is_authenticated():
		title = "Welcome %s" %(request.user)
	if request.method=="POST":
		print request.POST
	form = SignUpForm(request.POST or None)
	
	context = {
	"template_title":title,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		context={
			"title":"Thank you for registration"
		}
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {
			"queryset":queryset,
		}
	return render(request,"home.html",context)
	
def profile(request):
	if request.user.is_authenticated():
		title = "Welcome %s" %(request.user)
		context = {
			"title":title
		}
		return render(request, "profile.html",context)
	else:
		context={
			"title":"Please sign up/log in first."
		}
		return render(request,"home.html",context)