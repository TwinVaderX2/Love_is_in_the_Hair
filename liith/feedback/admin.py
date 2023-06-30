from django.contrib import admin
from . models import Review
# Register your models here.

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 2


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Data information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     inlines = [ChoiceInline]
#     list_filter = ['pub_date']
#     search_fields = ['question_text']


# admin.site.register(Question, QuestionAdmin)

# registers Review on admin page
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','rate','created_at']
    readonly_fields = ['created_at',]