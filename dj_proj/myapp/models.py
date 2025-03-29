from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Название новости')
    content = models.TextField(verbose_name='Новость')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title