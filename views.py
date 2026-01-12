from django.http import HttpResponse

def home(request):
    return HttpResponse("Users service is running")
