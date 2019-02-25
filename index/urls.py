from django.urls import path
from django.views.generic import TemplateView
from .views import index_view, article_tab, article_desc

urlpatterns = [
    path('', index_view, name='index_view'),
    path('impress', TemplateView.as_view(template_name='impress.html')),
    path('article', article_tab, name='article_tab'),
    path('picture', TemplateView.as_view(template_name='picture.html')),
    path('article_desc', article_desc, name='article_desc')
]
