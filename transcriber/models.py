from django.db import models
from django.urls import reverse


class Transcriber(models.Model):
    name = models.CharField(max_length=128, default='', verbose_name='Название интервью')
    audio_source = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Путь до файла', null=True)
    transcribe_text = models.TextField(verbose_name='Текст интервью', null=True)
    slug = models.SlugField(unique=True, verbose_name='URL')
    profile = models.ForeignKey('profiles.Profile', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Транскрибатор'
        verbose_name_plural = 'Транскрибаторы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('transcriber', kwargs={'transcriber_slug': self.slug, 'profile_slug': self.profile.slug})
