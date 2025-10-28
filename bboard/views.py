from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.utils import translation
from django.conf import settings

from .models import Bb, Rubric
from .forms import BbForm


class BbCreateView(CreateView):
    template_name = 'bboard/bb_create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def set_language(request):
    lang = request.GET.get('lang', 'ru')

    if lang in [code for code, name in settings.LANGUAGES]:
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang

    return redirect(request.META.get('HTTP_REFERER', 'index'))


def index(request: HttpRequest):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def rubric_bbs(request: HttpRequest, rubric_id: int):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bbs.html', context)