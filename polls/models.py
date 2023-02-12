from django.db import models
from django.contrib import admin
# Create your models here.
class Question(models.Model):
  question_text = models.CharField('Texto de pregunta',max_length=200)
  pub_date = models.DateTimeField('Fecha de publicación')

  @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

  def __str__(self) -> str:
    return self.question_text

  def was_published_recently(self):
    return False

class Choice(models.Model):
  question = models.ForeignKey(Question,on_delete=models.CASCADE,verbose_name='Pregunta')
  choice_text = models.CharField('Texto elegido',max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self) -> str:
    return self.choice_text


class User(models.Model):
  name = models.CharField('Nombre del usuario',max_length=20)
  age = models.IntegerField()
  birthday = models.DateField()
  