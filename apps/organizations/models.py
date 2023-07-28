from django.db import models


class District(models.Model):
    name = models.CharField('Название района', max_length=150)


class Concern(models.Model):
    name = models.CharField('Название сети предприятий', max_length=150)


class Organization(models.Model):
    name = models.CharField('Название предприятия', max_length=150)
    concern = models.ForeignKey(
        Concern,
        on_delete=models.PROTECT,
        related_name='organizations'
    )
    district = models.ManyToManyField(
        District,
        related_name='organizations'
    )



