from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# this funciton is temporary and should not be continued
def show_user_info(request):
    return HttpResponse(request.user.password)