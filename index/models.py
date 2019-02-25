from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField('标题', max_length=50)
    text = models.TextField()
    issue_time = models.DateTimeField('发布时间', auto_now=True)
    visit = models.IntegerField('浏览', default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='作者')
    image = models.ImageField(u'图片', upload_to='article_img')

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = '文章管理'

    def __str__(self):
        return self.title


class Discuss(models.Model):
    text = models.TextField('内容')
    issue_time = models.DateTimeField('发布时间', auto_now=True)
    user = models.CharField('用户名', max_length=50)
    image = models.ImageField(u'图片', upload_to='user_img')
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL, verbose_name='文章标题')

    class Meta:
        verbose_name = '文章评论管理'
        verbose_name_plural = '文章评论管理'

    def __str__(self):
        return self.text


class Diary(models.Model):
    issue_time = models.DateTimeField('发布时间', auto_now=True)
    title = models.CharField('标题', max_length=50, default='记录')
    text = models.TextField()

    class Meta:
        verbose_name = '日记管理'
        verbose_name_plural = '日记管理'

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=50, default='访客')
    issue_time = models.DateTimeField(auto_now=True)
    message = models.TextField()
    img = models.ImageField(u'图片', upload_to='msg_img')

    class Meta:
        verbose_name = '留言板管理'
        verbose_name_plural = '留言板管理'

    def __str__(self):
        return self.name


class Image(models.Model):
    date_time = models.DateTimeField('发布时间', auto_now=True)
    name = models.CharField('照片描述', max_length=30)
    image = models.ImageField(u'图片', upload_to='photos')

    class Meta:
        verbose_name = '照片管理'
        verbose_name_plural = '照片管理'

    def __str__(self):
        return self.name
