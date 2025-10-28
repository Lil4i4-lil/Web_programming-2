from django.db import models
from django.utils.translation import gettext_lazy as _


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Товар'))
    content = models.TextField(verbose_name=_('Описание'))
    price = models.FloatField(verbose_name=_('Цена'))
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Опубликовано'))
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name=_('Рубрика'))

    class Meta:
        verbose_name_plural = _('Объявления')
        verbose_name = _('Объявление')
        ordering = ('-published',)


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name=_('Название'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Рубрики')
        verbose_name = _('Рубрика')
        ordering = ('name',)
