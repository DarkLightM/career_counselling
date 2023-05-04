from django.db import models
from django.urls import reverse


class VkInfo(models.Model):
    client_url = models.CharField(max_length=128, verbose_name='ВК ссылка')
    client_name = models.CharField(max_length=128, verbose_name='Имя в профиле ВК')
    client_surname = models.CharField(max_length=128, verbose_name='Фамилия в профиле ВК')
    nickname = models.CharField(max_length=128, null=True, unique=True, verbose_name='Никнейм в профиле ВК')
    telephone_number = models.CharField(max_length=12, null=True, verbose_name='Телефонный номер')
    birth_date = models.DateField(null=True, verbose_name='Дата рождения')
    sex = models.CharField(max_length=10, null=True, verbose_name='Пол')
    location = models.CharField(max_length=128, null=True, verbose_name='Местоположение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')
    slug = models.SlugField(max_length=128, unique=True, verbose_name="URL", default='')
    profile = models.ForeignKey('profiles.Profile', verbose_name='Ссылка на профиль', null=True, related_name='+',
                                on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Информация из ВК'
        verbose_name_plural = 'Информация из ВК'

    def __str__(self):
        return " ".join([self.client_url])

    def get_absolute_url(self):
        return reverse('vk_home', kwargs={'vk_slug': self.slug, 'profile_slug': self.profile.slug})
