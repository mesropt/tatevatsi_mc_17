import csv
from datetime import datetime

from django.contrib import admin
from django.http import HttpResponse

from actor.models import Actor


class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'date_of_birth')
    list_filter = ('oscar', 'gender')
    search_fields = ('first_name', 'last_name')
    fieldsets = (('Actor', {'fields': ('first_name', 'last_name', 'gender', 'oscar',
                                       'age', 'date_of_birth', 'image')}),
                 ('Movie', {'fields': ('movie',)}))
    filter_horizontal = ('movie',)
    # actions = ['download_csv']

    # @admin.action(description='Download CSV')
    # def download_csv(self, request, queryset):
    #     opts = self.model._meta
    #     content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = content_disposition
    #     writer = csv.writer(response)
    #     fields = [field for field in opts.get_fields() if not \
    #         field.many_to_many and not field.one_to_many and field.name != 'image']
    #
    #     writer.writerow([field.verbose_name for field in fields])
    #
    #     for obj in queryset:
    #         data_row = []
    #         for field in fields:
    #             value = getattr(obj, field.name)
    #             if isinstance(value, datetime):
    #                 value = value.strftime('%d/%m/%Y')
    #             data_row.append(value)
    #         writer.writerow(data_row)
    #     return response


admin.site.register(Actor, ActorAdmin)
