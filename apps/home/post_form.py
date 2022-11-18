# -*- encoding: utf-8 -*-
"""
Copyright (c) Hack
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.db.models import  UserDetails


class CreateNewPost(forms.Form):
    Title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "form-control form-control-lg"
            }
        ))
    Desc = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "form-control text-primary",
                "rows": "3"
            }
        ))

    # vd = forms.FileInput()
    vd = forms.CharField(
        widget=forms.FileInput(
            attrs={

                "class": "form-control form-control-lg text-primary",
                "accept":"video/mp4,video/x-m4v,video/*",
            }
        ))



# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Username",
#                 "class": "form-control"
#             }
#         ))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder": "Email",
#                 "class": "form-control"
#             }
#         ))
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password",
#                 "class": "form-control"
#             }
#         ))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password check",
#                 "class": "form-control"
#             }
#         ))

    # class Meta:
    #     abstract = True
    #     model = UserDetails
    #     fields = ('Title', 'Description', 'VideoFile', 'HashTags')
