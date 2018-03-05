from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'libraryfront/index.html',)

def redirect(request):
    return HttpResponseRedirect('。/index/'),
