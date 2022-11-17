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
# from django.forms.models import model_to_dict


@login_required(login_url="/login/")
def index(request):

    default_data = {'overall': {'New Viewers': '10', 'Views': '3.6k', 'followers': '19'}}
    default_data = json.dumps(default_data)

    try:
        print(request.user)
        print("\n\n", UserDetails.objects.filter(name=request.user))
        post = json.loads([col.post.replace("'", '"') for col in UserDetails.objects.filter(name=request.user)][0])
        print(post, type(post))
        # print(data_dic)
        # print("\n\n", request.user)
    except Exception as e:
        post = default_data
        pass

    post = json.dumps({'overall': post})
    context = {'segment': 'index', 'data': post}

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
