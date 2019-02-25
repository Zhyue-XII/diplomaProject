from django.shortcuts import render
from .models import Article, Diary, Image, Message, Discuss


def index_view(request):
    top_article = Article.objects.filter(top=1)[0]
    diary_list = Diary.objects.all()[0:3]
    photos = Image.objects.all()[0: 8]
    msg = Message.objects.all()
    return render(request, 'index.html',
                  {
                      'top_article': top_article,
                      'diary_list': diary_list,
                      'photos': photos,
                      'msg': msg
                  })


def article_tab(request):
    article_list = Article.objects.all()
    return render(request, 'article.html', {'article_list': article_list})


def article_desc(request):
    article_id = request.GET.get('id')
    print(article_id)
    return render(request, 'article_desc.html', {'data': article_desc})
