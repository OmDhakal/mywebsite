from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .forms import ContactMessageForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


@require_POST
def contact(request):
    form = ContactMessageForm(request.POST)
    if not form.is_valid():
        return HttpResponse('Please check the form fields and try again.', status=400)

    form.save()
    return HttpResponse('OK')
