from django.contrib import admin
from .models import Choice, Question, OpenQuestion
from django.db.models import TextField

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class OpenInline(admin.TabularInline):
    model = OpenQuestion
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text', 'is_open']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline, OpenInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)