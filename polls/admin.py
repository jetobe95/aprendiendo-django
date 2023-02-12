from django.contrib import admin
from .models import Question, Choice,User
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Informacion de la pregunta',{'fields':['question_text']}),
    ('Date information',{'fields':['pub_date']})
  ]
  inlines = [ChoiceInline]
  list_display = ('question_text', 'pub_date','was_published_recently')
  list_filter=['pub_date','question_text']
  search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Information about Choice',{'fields':['question','choice_text']}),
    ('Information about votes',{'fields':['votes']}),
  ]

  list_display = ('choice_text','votes')



admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(User)