# Generated by Django 4.1.7 on 2023-03-28 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='Название интервью')),
                ('audio_source', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Путь до файла')),
                ('transcribe_text', models.TextField(null=True, verbose_name='Текст интервью')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='profiles.profile')),
            ],
            options={
                'verbose_name': 'Транскрибатор',
                'verbose_name_plural': 'Транскрибаторы',
            },
        ),
    ]
