from django.shortcuts import render

# Create your views here.
def handlesignup(request):
    return render(request,'auth/signup.html')