from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils.translation import gettext as _


class HomeView(TemplateView):
    template_name = 'index.html'

    def HomeView(request):
        output = _('StatusMsg')
        data = {'langs': ['img/en.png', 'img/sk.png', 'img/ru.png', 'img/cs.png', 'img/uk.png', 'img/de.png']}
        return render(output, context=data)