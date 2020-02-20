from django.contrib import admin

# Register your models here.

from .models import *

class ChoiceInline(admin.StackedInline):
    model = Choices
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choices,ChoiceAdmin)
admin.site.register(User)
