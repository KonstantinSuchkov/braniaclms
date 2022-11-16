# from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from mainapp.models import News


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexViewView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context["news_title"] = "новостной заголовок для задания № 3"
        # context["news_preview"] = "Описания новости с помощью цикла!"
        # context["range"] = range(5)
        # return context
        context = super().get_context_data(**kwargs)
        context['object_list'] = News.objects.filter(deleted='False')
        return context
