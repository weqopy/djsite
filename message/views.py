from django.shortcuts import render
from .models import UserMessage


def getform(request):
    # objects.all()获取所有，filter()筛选
    # all_message = UserMessage.objects. all()
    all_message = UserMessage.objects.filter(name='bobb')
    for message in all_message:
        # 直接输出内容
        # print(message.name)
        message.delete()

    # POST方法
    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     email = request.POST.get('email', '')
    #     address = request.POST.get('address', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.save()
    return render(request, 'message/message_form.html')
