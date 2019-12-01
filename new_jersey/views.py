from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from . import models
from . import forms


def home(request):
    form = forms.LienForm()
    return render(request, 'new_jersey/home.html', dict(form=form, application_for_css="new_jersey"))


def lien_search(request):
    if request.GET:
        url = request.build_absolute_uri()
        url = url[url.find('?'):]
        data_raw = dict(request.GET)
        if data_raw.get('csrfmiddlewaretoken', False):
            data_raw.pop('csrfmiddlewaretoken')
        data = {}
        for key, value in data_raw.items():
            if not value[0] == '':
                data[key] = value[0]
        if len(data.keys()) == 0:
            return HttpResponseRedirect(reverse("new_jersey:home"))
        liens = models.Lien.objects.filter(**data)
        return render(request, 'new_jersey/lien_search.html',
                      dict(liens=liens, url=url, application_for_css='new_jersey'))
    else:
        return HttpResponseRedirect(reverse("new_jersey:home"))


def lien_detail(request, lien_id):
    lien = get_object_or_404(models.Lien, lien_id=lien_id)
    lien_form = forms.LienUpdateForm(instance=lien)
    sub_form = forms.SubForm()
    if request.method == 'POST':
        sub_form = forms.SubForm(request.POST)
        lien_form = forms.LienUpdateForm(instance=lien, data=request.POST)
        if sub_form.is_valid():
            sub = sub_form.save(commit=False)
            sub.lien = lien
            sub.save()
            messages.add_message(request, messages.SUCCESS, "Sub successfully added!")
            return HttpResponseRedirect(reverse("new_jersey:lien_detail", kwargs={
                "lien_id": lien.lien_id
            }))
        elif lien_form.is_valid():
            lien = lien_form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully Saved")
            return HttpResponseRedirect(reverse("new_jersey:lien_detail", kwargs={
                "lien_id": lien.lien_id
            }))
    return render(request, 'new_jersey/lien_detail.html',
                  dict(lien=lien, lien_form=lien_form, sub_form=sub_form, application_for_css='new_jersey'))

