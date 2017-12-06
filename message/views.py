from django.shortcuts import render

# Create your views here.
def getfrom(request):
    return render(request, 'message/message_form.html')
