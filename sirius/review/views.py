from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from assignments.models import Assignment
from accounts.models import MyUser
from datetime import datetime


# Create your views here.
# page1: unreviewed
# page2: reviewed
from sirius.settings import MEDIA_ROOT


def review(request, id, page1, page2):
    teacher = MyUser.objects.get(id=id)
    unreviewed_list = Assignment.objects.filter(is_reviewed=False).order_by('-updated')
    reviewed_list = Assignment.objects.filter(is_reviewed=True).order_by('-updated')
    paginator_1 = Paginator(unreviewed_list, 10)
    paginator_2 = Paginator(reviewed_list, 10)
    try:
        pageInfo_1 = paginator_1.page(page1)
        pageInfo_2 = paginator_2.page(page2)
    except PageNotAnInteger:
        pageInfo_1 = paginator_1.page(1)
        pageInfo_2 = paginator_2.page(1)
    except EmptyPage:
        pageInfo_1 = paginator_1.page(paginator_1.num_pages)
        pageInfo_2 = paginator_2.page(paginator_2.num_pages)

    return render(request, 'review.html', locals())


def assign_review(request, assign_id):
    assign = Assignment.objects.get(id=assign_id)
    id = request.user.id
    if request.method == 'POST':
        score = request.POST.get('score', '')
        credit = request.POST.get('credit', '')
        d = {'score': score, 'credit': credit, 'updated': datetime.now(), 'is_reviewed': True}
        Assignment.objects.filter(id=assign_id).update(**d)
        kwargs = {'id': id, 'page1': 1, 'page2': 1}
        return redirect(reverse('review', kwargs=kwargs))
    return render(request, 'assign_review.html', locals())


def assign_download(request, assign_id):
    assign = Assignment.objects.get(id=assign_id)
    name = assign.content.name.replace('/', '\\')
    file_path = MEDIA_ROOT + '\\' + name
    print(file_path)
    try:
        r = HttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename={}'.format(name)
        return r
    except Exception:
        raise Http404('Download error')
