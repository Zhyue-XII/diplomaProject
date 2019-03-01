from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Article, Diary, Image, Message, Discuss


def index_view(request):
    top_article = Article.objects.filter(top=1)[0]
    diary_list = Diary.objects.all()[0:3]
    photos = Image.objects.all().order_by('-id')[0:8]
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
    article = Article.objects.get(id=article_id)
    article.visit += 1
    article.save()
    discuss = Discuss.objects.filter(article_id=article_id).values('user', 'issue_time', 'text')
    data = discuss.annotate().all()
    if data:
        return render(request, 'article_desc.html', {'article': article, 'data': data})
    else:
        return render(request, 'article_desc.html', {'article': article, 'mess': '还没有人评论哦'})


@csrf_exempt
def submit_discuss(request):
    id = request.POST.get('id')
    text = request.POST.get('text')
    dis = Discuss.objects.create(text=text, article_id=id)
    dis.save()
    return JsonResponse({'code': 200, 'mess': '提交成功'})


def photos_list(request):
    day = Image.objects.values('date_time').order_by('-date_time')
    print(day)
    return render(request, 'picture.html', {'data': day})

