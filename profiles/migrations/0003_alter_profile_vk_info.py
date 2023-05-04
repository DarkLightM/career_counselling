# Generated by Django 4.1.7 on 2023-04-25 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vk_info', '0001_initial'),
        ('profiles', '0002_client_profile_alter_client_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='vk_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='vk_info.vkinfo', verbose_name='URL страницы ВК'),
        ),
    ]