from django.contrib import admin

from .models import Performance
# Register your models here.
@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    '''Admin View for Student Performance '''

    list_display = ('student', 'predicted_class')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    readonly_fields = ('predicted_class',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)