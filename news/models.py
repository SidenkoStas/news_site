from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, name="title",
                             verbose_name="Наименование категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse("news:get_category",
                       kwargs={"category_id": self.pk})

    def __str__(self):
        return f"{self.title}"


class News(models.Model):
    title = models.CharField(max_length=50, name="title",
                             verbose_name="Наименование")
    content = models.TextField(name="content", verbose_name="Контент")
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, name="created_at",
                                      verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, name="updated_at",
                                      verbose_name="Изменено")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", name="photo",
                              blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, name="is_published",
                                       verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,
                                 verbose_name="Категория")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("news:view_news",
                       kwargs={"news_id": self.pk})

    def __str__(self):
        return f"{self.title}"
