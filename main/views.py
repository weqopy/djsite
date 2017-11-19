from django.shortcuts import render


def index(request):
    string_1 = 'Django Learning'
    list_1 = ['HTML', 'Django', 'Python']
    dict_1 = {'first_name': 'Alice', 'last_name': 'Emmy'}
    list_2 = map(str, range(10))
    if_num = 99
    # 字典调用
    # 'string_1': string_1, 后者对应 home 中变量，前者对应 html 文件中变量
    context = {
        'string_1': string_1,
        'list_1': list_1,
        'dict_1': dict_1,
        'list_2': list_2,
        'if_num': if_num
    }
    return render(request, 'main/index.html', context)
