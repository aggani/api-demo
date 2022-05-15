from django.contrib import admin
from .models import Article

# Register your models here.
#way1: simpler and basic one
#admin.site.register(Article)

#way2: to design the panel
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
