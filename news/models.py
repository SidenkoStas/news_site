from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name="Наименование категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse("news:get_category", kwargs={"category_id": self.pk})

    def __str__(self):
        return f"{self.title}"


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name="Наименование")
    content = models.TextField(verbose_name="Контент")
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True,
                              verbose_name="Фото")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name="Категория")
    views = models.IntegerField(default=0,
                                verbose_name="Количество просмотров")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("news:view_news", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title}"
