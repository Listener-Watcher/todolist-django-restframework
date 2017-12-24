from django.contrib import admin
from .forms import SignUpForm
from .models import SignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	display = ["__unicode","timestamp","updated"]
	form = SignUpForm
	
admin.site.register(SignUp)