from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from accounts.models import MyUser


def userLogin(request):
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        if MyUser.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if MyUser.objects.filter(username=u).first().role_id == 2:
                    if user.is_active:
                        login(request, user)
                    kwargs = {'id': request.user.id, 'page': 1}
                    return redirect(reverse('assign', kwargs=kwargs))
                elif MyUser.objects.filter(username=u).first().role_id == 1:
                    if user.is_active:
                        login(request, user)
                    kwargs = {'id': request.user.id, 'page1': 1, 'page2': 1}
                    return redirect(reverse('review', kwargs=kwargs))
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请联系管理员'
    return render(request, 'user.html', locals())
