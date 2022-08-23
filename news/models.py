from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, name="title", verbose_name="Наименование")
    content = models.TextField(name="content", verbose_name="Контент")
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, name="created_at", verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, name="updated_at", verbose_name="Изменено")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", name="photo", blank=True, verbose_name="Фото")
    is_published = models.BooleanField(default=True, name="is_published", verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title}"
