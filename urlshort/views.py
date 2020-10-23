from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import Url 



def invaronvar(request, hashed_full):
	url = get_object_or_404(Url, hashed_full=hashed_full)
	url.clicking()

	return redirect(url.full)