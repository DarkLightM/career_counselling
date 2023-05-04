from django.db import models
from django.urls import reverse


class Analytics(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    grammar = models.ForeignKey(to='Grammar', on_delete=models.CASCADE, verbose_name='Ссылка на таблицу грамматики',
                                null=True)
    vocabulary = models.ForeignKey(to='Vocabulary', on_delete=models.CASCADE, verbose_name='Ссылка на таблицу лексики',
                                   null=True)
    syntax = models.ForeignKey(to='Syntax', on_delete=models.CASCADE, verbose_name='Ссылка на таблицу синтаксиса',
                               null=True)
    profile = models.ForeignKey(to='profiles.Profile', on_delete=models.PROTECT, verbose_name='Ссылка на таблицу профиля',
                                related_name='+')
    slug = models.SlugField(max_length=128, unique=True, verbose_name="URL", null=True)

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализ'

    def __str__(self):
        return " ".join([self.name])

    def get_absolute_url(self):
        return reverse('analytics', kwargs={'analytics_slug': self.slug, 'profile_slug': self.profile.slug})


class Grammar(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    future_verbs = models.PositiveIntegerField(verbose_name='Количество глаголов в будущем времени')
    present_verbs = models.PositiveIntegerField(verbose_name='Количество глаголов в настоящем времени')
    past_verbs = models.PositiveIntegerField(verbose_name='Количество глаголов в прошедшем времени')
    perfect_verbs = models.PositiveIntegerField(verbose_name='Количество глаголов совершенного вида')
    continuous_verbs = models.PositiveIntegerField(verbose_name='Количество глаголов несовершенного вида')
    subjunctive_verbs = models.PositiveIntegerField(
        verbose_name='Количество глаголов в форме сослагательного наклонения')
    diminutive_morphemes = models.PositiveIntegerField(verbose_name='Количество уменьшительно-ласкательном морфем')
    active_voice = models.PositiveIntegerField(verbose_name='Количество глаголов в активном залоге')
    passive_voice = models.PositiveIntegerField(verbose_name='Количество глаголов в пассивном залоге')
    slug = models.SlugField(max_length=128, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Грамматика'
        verbose_name_plural = 'Грамматика'

    def __str__(self):
        return " ".join([self.name])

    def get_absolute_url(self):
        return reverse('grammar', kwargs={'grammar_slug': self.slug})


class Vocabulary(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    nouns = models.PositiveIntegerField(verbose_name='Количество существительных')
    verbs = models.PositiveIntegerField(verbose_name='Количество глаголов')
    adjectives = models.PositiveIntegerField(verbose_name='Количество прилагательных')
    professional_vocabulary = models.PositiveIntegerField(verbose_name='Количество профессиональной лексики')
    expressive_vocabulary = models.PositiveIntegerField(verbose_name='Количество экспрессивной лексики')
    diminutive_words = models.PositiveIntegerField(verbose_name='Количество уменьшительно-ласкательных слов')
    personal_pronouns = models.PositiveIntegerField(verbose_name='Количество личных местоимений')
    numerals = models.PositiveIntegerField(verbose_name='Количество числительных')
    slug = models.SlugField(max_length=128, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Лексика'
        verbose_name_plural = 'Лексика'

    def __str__(self):
        return " ".join([self.name])

    def get_absolute_url(self):
        return reverse('vocabulary', kwargs={'vocabulary_slug': self.slug})


class Syntax(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    questions = models.PositiveIntegerField(verbose_name='Количество вопросительных предложений')
    comparative_turnovers = models.PositiveIntegerField(verbose_name='Количество сравнительных оборотов')
    slug = models.SlugField(max_length=128, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Синтаксис'
        verbose_name_plural = 'Синтаксис'

    def __str__(self):
        return " ".join([self.name])

    def get_absolute_url(self):
        return reverse('syntax', kwargs={'syntax_slug': self.slug})


class IStatements(models.Model):
    text = models.TextField(verbose_name='Текст высказывания')
    syntax = models.ForeignKey(to='Syntax', on_delete=models.PROTECT, verbose_name='Ссылка на таблицу синтаксиса',
                               null=True)
