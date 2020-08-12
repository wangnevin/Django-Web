import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse
from assignments.models import Assignment
from accounts.models import MyUser
from sirius.settings import BASE_DIR, MEDIA_ROOT
from type.models import Type


# Create your views here.
def assign(request, id, page):
    user = MyUser.objects.filter(id=id).first()
    assignment = Assignment.objects.filter(user_id=id).order_by('-updated')
    paginator = Paginator(assignment, 10)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        pageInfo = paginator.page(1)
    except EmptyPage:
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'student_info.html', locals())


def info_edit(request):
    id = request.user.id
    if request.method == 'POST':
        name = request.POST.get('name', '')
        class_number = request.POST.get('class_number', '')
        grade = request.POST.get('grade', '')
        telephone = request.POST.get('telephone', '')
        address = request.POST.get('address', '')
        wx = request.POST.get('wx', '')
        qq = request.POST.get('qq', '')
        wb = request.POST.get('wb', '')

        d = {
            'name': name, 'class_number': class_number,
            'grade': grade, 'telephone': telephone,
            'address': address, 'wx': wx,
            'qq': qq, 'wb': wb
        }
        id = request.user.id
        MyUser.objects.filter(id=id).update(**d)
        kwargs = {'id': id, 'page': 1}
        return redirect(reverse('assign', kwargs=kwargs))
    return render(request, 'info_edit.html', locals())


def assign_submit(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        type = request.POST.get('type', '')
        content = request.FILES.get('content', None)
        # f = open(os.path.join(MEDIA_ROOT, content.name), 'wb+')
        # for chunk in content.chunks():
        #     f.write(chunk)
        # f.close()
        id = request.user.id
        type = Type.objects.get(type=type)
        d = {'title': title, 'type': type, 'content': content, 'user_id': id}
        Assignment.objects.create(**d)
        kwargs = {'id': id, 'page': 1}
        return redirect(reverse('assign', kwargs=kwargs))
    return render(request, 'assign_submit.html', locals())


def assign_edit(request, assign_id):
    id = request.user.id
    if request.method == 'POST':
        title = request.POST.get('title', '')
        type = request.POST.get('type', '')
        type = Type.objects.get(type=type)
        content = request.FILES.get('content', None)
        # f = open(os.path.join(MEDIA_ROOT, content.name), 'wb+')
        # for chunk in content.chunks():
        #     f.write(chunk)
        # f.close()

        d = {'title': title, 'type': type, 'content': content, 'user_id': id}
        # Assignment.objects.filter(id=assign_id).update(**d)
        old_name = Assignment.objects.get(id=assign_id).content.name
        old_name = old_name.replace('/', '\\')
        old_file_path = MEDIA_ROOT + '\\' +old_name
        os.system('del {}'.format(old_file_path))
        Assignment.objects.get(id=assign_id).delete()
        Assignment.objects.create(**d)
        kwargs = {'id': id, 'page': 1}
        return redirect(reverse('assign', kwargs=kwargs))
    return render(request, 'assign_edit.html', locals())
