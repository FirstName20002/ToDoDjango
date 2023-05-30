from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название Группы', unique=True)
    description = models.TextField(max_length=300, verbose_name='Описание')

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name


class Task(models.Models):
    URGENCY_CHOICES = (
        ('UI', 'Срочно и важно'),
        ('UNI', 'Срочно, но не важно'),
        ('NUI', 'Не срочно, но важно'),
        ('NUNI', 'Не срочно и не важно'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='posts',
                               verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=300, verbose_name='Описание')
    Priorities = models.CharField(choices=URGENCY_CHOICES, max_length=4, default='UI', verbose_name='Приоритет')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    status = models.BooleanField(default=False, verbose_name='Статус')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Планируемая дата завершения')

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title


class Notes(models.Models):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(max_length=300, verbose_name='Описание')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return self.title
