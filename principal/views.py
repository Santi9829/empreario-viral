from django.shortcuts import render, redirect

from django.utils import timezone
# Create your views here.

def redirect_view(request):
	context = {
		'date': timezone.now(),
		'referencia':'Esta es la fecha',
	}
	return render(request, "login.html", context)