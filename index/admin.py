from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Article, Diary, Discuss, Message, Image


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'issue_time', 'visit', 'top', 'image_data']
    search_fields = ['title']
    list_filter = ['author']

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px"/>' % obj.image.url)
    readonly_fields = ('image_data',)  # 必须加这行 否则访问编辑页面会报错
    # 页面显示的字段名称
    image_data.short_description = '文章插图'
    list_per_page = 5


@admin.register(Discuss)
class DiscussAdmin(admin.ModelAdmin):
    list_display = ['user', 'issue_time', 'article', 'text']
    search_fields = ['user']
    list_per_page = 10


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ['title', 'issue_time']
    list_filter = ['issue_time']
    list_per_page = 10


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'issue_time', 'message']
    search_fields = ['name']
    list_filter = ['issue_time']
    list_per_page = 10


@admin.register(Image)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_time', 'image_data')
    search_fields = ['name']
    list_filter = ['date_time']  # 过滤器
    list_per_page = 5

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="100px"/>' % obj.image.url)
    readonly_fields = ('image_data',)
    # 页面显示的字段名称
    image_data.short_description = '相册图片'


admin.site.site_header = '个人网站后台管理'
admin.site.site_footer = '个人网站'
