#!/usr/bin/env python
#coding:utf-8

from django import forms

class Alogin(forms.Form):
    username = forms.CharField(error_messages={'required': ('用户名不能为空.'), 'invalid': ('用户名格式错误')})
    email = forms.EmailField(required=True, error_messages={'required': ('邮箱不能为空.'), 'invalid': ('邮箱格式错误')})
    ip = forms.GenericIPAddressField(error_messages={'required': ('IP不能为空.'), 'invalid': ('IP格式错误')})

