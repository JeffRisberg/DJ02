from django.http import HttpResponse

from django.http.response import HttpResponse

from django.template import Context, loader

from .models import Charity

def index(request):
    return HttpResponse("Hello, world. You're at the giving index.")

def homepage(request):
    charity_list = Charity.objects.all()
    template = loader.get_template('giving/charity_list.html')
    context = Context({'charity_list': charity_list})
    output = template.render(context)
    return HttpResponse(output)