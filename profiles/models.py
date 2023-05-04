from django.db import models
from django.urls import reverse

from analytics.models import Analytics
from vk_info.models import VkInfo


class Client(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    surname = models.CharField(max_length=128, verbose_name='Фамилия')
    second_name = models.CharField(max_length=128, verbose_name='Отчество')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    telephone_number = models.CharField(max_length=12, unique=True, verbose_name='Телефонный номер', null=True)
    email = models.CharField(max_length=128, unique=True, verbose_name='Почта', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    slug = models.SlugField(max_length=128, unique=True, verbose_name='URL')
    profile = models.ForeignKey('Profile', on_delete=models.PROTECT, verbose_name='Ссылка на профиль', related_name='+',
                                null=True)

    class Meta:
        verbose_name = 'Информация о клиенте'
        verbose_name_plural = 'Информация о клиенте'

    def __str__(self):
        return " ".join([self.surname, self.name, self.second_name])

    def get_absolute_url(self):
        return reverse('client', kwargs={'client_slug': self.slug, 'profile_slug': self.profile.slug})


class Profile(models.Model):
    name = models.CharField(max_length=128, null=True, verbose_name='Название профиля')
    vk_info = models.ForeignKey('vk_info.VkInfo', on_delete=models.PROTECT, verbose_name='URL страницы ВК', null=True,
                                related_name='+')
    analytics = models.ForeignKey('analytics.Analytics', on_delete=models.PROTECT,
                                  verbose_name='Название страницы аналитики',
                                  null=True, related_name='+')
    client = models.ForeignKey('Client', on_delete=models.PROTECT, verbose_name='ФИО клиента', null=True,
                               related_name='+')
    slug = models.SlugField(max_length=128, verbose_name='URL', unique=True, default='')

    class Meta:
        verbose_name = 'Информация о профиле'
        verbose_name_plural = 'Информация о профиле'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile', kwargs={'profile_slug': self.slug})
