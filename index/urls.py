from django.urls import path
from django.views.generic import TemplateView
from .views import index_view

urlpatterns = [
    path('', index_view, name="index_view"),
    path('impress', TemplateView.as_view(template_name='impress.html')),
    path('article', TemplateView.as_view(template_name='article.html')),
    path('picture', TemplateView.as_view(template_name='picture.html')),
    path('article_desc', TemplateView.as_view(template_name='article_desc.html'))
]
