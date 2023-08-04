from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor', 'categoria', 'data')
    list_filter = ('categoria',)
    list_editable = ('categoria',)

admin.site.register(Post, PostAdmin)
