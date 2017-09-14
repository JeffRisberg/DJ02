from django.http.response import HttpResponse

from django.template import Context, loader

from .models import Charity, Donor

def index(request):
    return HttpResponse("Hello, Welcome to the Giving Application")


def charity_list_view(request):
    charity_list = Charity.objects.all()
    template = loader.get_template('giving/charity_list.html')
    context = Context({'charity_list': charity_list})
    output = template.render(context)
    return HttpResponse(output)


def donor_list_view(request):
    donor_list = Donor.objects.all()
    template = loader.get_template('giving/donor_list.html')
    context = Context({'donor_list': donor_list})
    output = template.render(context)
    return HttpResponse(output)