from django.contrib import admin

# Register your models here.
from App.models import StudentInfo, ClassInfo

admin.site.site_title = "云毕业典礼后台"
admin.site.site_header = "云毕业典礼后台"


class StudentAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'age', 'pic_url', 'class_name')
    list_filter = ()
    search_fields = ('name', 'number')
    fieldsets = (
        (None, {
            'fields': (
                'number',
                'name',
                'pic_url',
                'class_name',
                'age',
            )
        }),
    )


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'pic_url', 'audio_url', 'class_des')
    list_filter = ()
    search_fields = ('class_name', 'class_number')
    fieldsets = (
        (None, {
            'fields': (

                'class_name',
                'pic_url',
                'audio_url',
                'class_des',
            )
        }),
    )


admin.site.register(StudentInfo, StudentAdmin)
admin.site.register(ClassInfo, ClassAdmin)
