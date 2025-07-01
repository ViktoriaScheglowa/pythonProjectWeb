from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Загаловок",
        help_text="Введите заголовок блога",
    )

    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое блога",
    )

    preview = models.ImageField(
        upload_to="blog/preview",
        verbose_name="Изображение",
        help_text="Загрузите изображение блога",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Отметьте, если пост опубликован",
    )

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Количество раз, когда пост был просмотрен",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["-created_at"]