from django.contrib import admin

from .models import UserInfo, Post, PostTree, Company, Intention

admin.site.register(UserInfo)
admin.site.register(Post)
admin.site.register(PostTree)
admin.site.register(Company)
admin.site.register(Intention)
