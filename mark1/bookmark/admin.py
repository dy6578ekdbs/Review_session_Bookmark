from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.

@admin.register(Bookmark)

class BookmarkAdmin(admin.ModelAdmin):  
    list_display = ('id', 'title', 'url');  #여기 파트 1도 모르겟네 왜 그동안 코딩한거랑 다르게 생겻지 
