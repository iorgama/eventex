#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from subscription.forms import SubscriptionForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from subscription.models import Subscription
from debian.debtags import reverse
 

#def inscricao(request):
#    if request.method == 'POST':
#        form = SubscriptionForm(request.POST)
#        if form.is_valid():
#            form.save()
#            messages = (u'Inscrição realizada com sucesso;', u'Aguarde até que sua solicitação de cadastro seja aprovada')
#            return render_to_response('index.html',{'messages':messages }, context_instance=RequestContext(request))
#    else:
#        form = SubscriptionForm()
#    return render_to_response('subscription/subscription_form.html',{'form': form, 'title' : u'Preencha Sua Inscrição'}, context_instance=RequestContext(request))

def inscricao(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            send_mail(
                subject = u'Inscrição no EventeX',
                message = u'Obrigado por se inscrever no EventeX!',
                from_email = 'contato@eventex.com',
                recipient_list = ['iorgama.p@gmail.com'],
            )
            return sucesso(request, subscription.pk)
#            messages = (u'Inscrição realizada com sucesso;', u'Aguarde até que sua solicitação de cadastro seja aprovada')
#            return render_to_response('index.html',{'messages':messages, 'subscription': subscription.pk}, context_instance=RequestContext(request))
    else:
        form = SubscriptionForm()
    return render_to_response('subscription/subscription_form.html',{'form': form, 'title' : u'Preencha Sua Inscrição'}, context_instance=RequestContext(request))

def sucesso(request, nr_item):
    try:
        subscription = Subscription.objects.get(pk=nr_item)
    except Subscription.DoesNotExist:
        raise Http404
    return render_to_response('subscription/success.html', {'subscription': subscription}, context_instance=RequestContext(request))
