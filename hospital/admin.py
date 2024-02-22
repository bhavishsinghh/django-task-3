from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails
from .models import Category, Post
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

# for configuration category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description', 'url', 'add_date')
    search_fields = ('title', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', )
    list_filter = ('cat',)
    list_per_page = 10

    class Media:
        js = ('https://cdn.tiny.cloud/1/9so7xt803zzxkmicnkx2zm43lvizywtjg53okoypybrvoqaq/tinymce/6/tinymce.min.js', 'js/script.js',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

