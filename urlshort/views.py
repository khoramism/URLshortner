from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import Url 

from django.views import generic
from .forms import UrlForm

def invaronvar(request, hashed_full):
	url = get_object_or_404(Url, hashed_full=hashed_full)
	url.clicking()

	return redirect(url.full)


def bede(request):
	if request.method == 'POST':
		form = UrlForm(request.Post)
		if form.is_valid():
			
			url = form.cleaned_data['url']
			created_url = Url.objects.create(full=url)
			context = {
				"created_url" : created_url,
				'form':form
			}
	else:	
		form = UrlForm()
		context = {
			'form': form
		}
	return render(request, 'urlshort/show.html', context)



