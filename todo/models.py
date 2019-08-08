from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings

# Create your models here.
PRIORITET = (
    (1, 'low'),
    (2, 'medium'),
    (3, 'hight'),
)


class Tasks(models.Model):
    ''' this is base class from tasks'''
    name = models.CharField(max_length=100)
    prioritet = models.IntegerField(choices=PRIORITET,  default='medium')
    status = models.BooleanField()
    date_create = models.DateField(auto_now_add=True)
    date_close = models.DateField()
    date_dedline = models.DateField()
    progress = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
