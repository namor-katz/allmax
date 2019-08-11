from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from model_utils import Choices


class Tasks(models.Model):
    ''' this is base class from tasks'''
    PRIORITET = Choices(
    ('l', 'low'),
    ('m', 'medium'),
    ('h', 'hight'),
)

    title = models.CharField(max_length=100)
    prioritet = models.CharField(max_length=1, choices=PRIORITET, default=PRIORITET.l)
    text = models.TextField(null=True, blank=True, verbose_name="описание")
    status = models.BooleanField() #open/close
    date_create = models.DateField(auto_now_add=True)
    #date_close = models.DateField() # сделать необязательым временно
    #date_deadline = models.DateField() # то же
    progress = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ['date_create']

    def __str__(self):
        return self.title #так то и без него все отображает.
