# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import json
from apps.home.models import UserDetails
from .post_form import CreateNewPost
import os
from django.core.files.storage import FileSystemStorage

# from django.forms.models import model_to_dict


@login_required(login_url="/login/")
def index(request):

    default_data = {'overall': {'New Viewers': '01', 'Views': '01', 'followers': '01', 'New Views pct': '01', 'Views Pct': '01', 'follow pct': '00'}, 'Analytics':{'TP': '01', 'TWH': '00', 'WL': [00, 00, 00, 00, 00, 00, 00, 00, 00, 0]}}
    default_data = json.dumps(default_data)

    try:
        print(request.user)
        print("\n\n", UserDetails.objects.filter(name=request.user))
        stat = json.loads([col.post.replace("'", '"') for col in UserDetails.objects.filter(name=request.user)][0])
        print( stat, type(stat), sep="\n")
        # print(data_dic)
        # print("\n\n", request.user)
    except Exception as e:
        stat = default_data
        print(stat)
        pass

    stat = json.dumps(stat)
    context = {'segment': 'index', 'stat': stat}

    html_template = loader.get_template('home/index.html')
    # return render(context,request,"home/index.html", data)
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def Create_NewPost(request):
    # pass
    # print(os.cu)
    context = {'segment': 'index'}

    form = CreateNewPost(request.POST or None)
    # print("ding", form)
    if request.method == "POST":
        print(request.FILES['vd'])
        # print(form.is_valid(),)

        if form.is_valid():
            try:
                Title = form.cleaned_data.get("Title")
                Description = form.cleaned_data.get("Desc")
                myfile = request.FILES['vd']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                print(uploaded_file_url)

                print("djang",  Title, Description,uploaded_file_url)

            except Exception as e:
                pass

            # with open(f"video/file/{Title}.mp4", 'wb+') as destination:
            #     for chunk in video.chunks():
            #         destination.write(chunk)

    # html_template = loader.get_template('home/login.html')

    return render(request, "home/NewPost.html", {"form": form, "msg": "msg"})
    # return HttpResponse(html_template.render(context, request))

