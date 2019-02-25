from django.shortcuts import render
from .models import Article, Diary, Image, Message


def index_view(request):
    top_article = Article.objects.filter(top=1)[0]
    diary_list = Diary.objects.all()[0:3]
    photos = Image.objects.all()[0: 8]
    msg = Message.objects.all()
    print(photos)
    return render(request, 'index.html',
                  {
                      'top_article': top_article,
                      'diary_list': diary_list,
                      'photos': photos,
                      'msg': msg
                  })
