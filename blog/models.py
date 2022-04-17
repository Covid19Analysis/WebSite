import django
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
DEFAULT = "twiter"
CATEGORY = (
    ("twitter", "Twitter"),
    ("instagram", "Instagram"),
    ("facebook", "Facebook"),
)


class Post(models.Model):
    user = models.ForeignKey("auth.User", related_name="post",
                             on_delete=models.CASCADE, verbose_name="Kullanıcı")
    title = models.CharField(max_length=120, verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    publish_date = models.DateTimeField(
        verbose_name="Yayın Tarihi", auto_now_add=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="uploads", verbose_name="Resim")
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    grup = models.CharField(choices=CATEGORY, max_length=15,
                            default=DEFAULT, verbose_name="Kategori")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("")

    def get_unique_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-publish_date", "id"]
