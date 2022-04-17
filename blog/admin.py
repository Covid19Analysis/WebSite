from django.contrib import admin
from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "publish_date", "slug", "user"]
    list_display_links = ["title"]
    list_filter = ["title", "content"]
    # list_editable = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
