from django.shortcuts import render, redirect
from django.http import Http404
from .models import Conference, Speaker, Speech, Comment
from .forms import CommentForm
import datetime


def conference(request):
    confs = Conference.objects.all().order_by('date_start').filter(date_start__gte=datetime.datetime.now()).order_by('date_start').reverse()
    return render(request, 'base_conference.html', context={'confs': confs})


def detail(request, cid):
    try:
        conf = Conference.objects.get(pk=cid)
        comments = Comment.objects.filter(conference=conf)
        speeches = Speech.objects.all().filter(conference=conf).order_by('date')
        form = CommentForm(request.POST or None)
        form.user = request.user
        if request.method == "POST":
            if form.is_valid:
                form = form.save(commit=False)
                form.user = request.user
                form.conference = conf
                form.save()
                return redirect(detail, cid)
            else:
                print(form.errors)
    except Conference.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'conf_detail.html', context={'speeches': speeches, 'comments': comments, 'form': form})



def archive(request):
    confs = Conference.objects.all().order_by('date_start').filter(date_start__lt=datetime.datetime.now()).order_by('date_start').reverse()
    return render(request, 'archive.html', context={'confs': confs})

