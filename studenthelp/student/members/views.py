from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  template = loader.get_template('main.html')
  currentlogin=Member.objects.all().values()
  context={
    'members':currentlogin
    }
  return HttpResponse(template.render(context, request))