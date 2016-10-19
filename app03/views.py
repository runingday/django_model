#encoding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, HttpResponse


# Create your views here.

from app03 import forms

def index(request):

    ret = {'data': None, 'error': ""}
    obj = forms.Alogin()

    ret['data'] = obj

    if request.method == 'POST':
        #ip、正则表达式检查是否IP
        #email/正则表达式检查是否是email
        checkForm = forms.Alogin(request.POST)
        checkResult = checkForm.is_valid()

        if checkResult:
            #输入全部正确,通过验证
            pass
        else:
            firstErrorMsg = checkForm.errors.as_data().values()[0][0].messages[0]
            ret['error'] = firstErrorMsg
            ret['data'] = checkForm

    return render_to_response('app03/index.html', ret )
