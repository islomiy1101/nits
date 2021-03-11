from django.contrib import admin
from nitc.models import Branch,Course,Register,Teacher,MFY,Course_Part,Sector
# Register your models here.

class BranchAdmin(admin.ModelAdmin):
    list_display=['name','address','contact_number']

class CourseAdmin(admin.ModelAdmin):
    list_display=['name','course_time','payment']

class RegisterAdmin(admin.ModelAdmin):
    list_display=['contact_number','branch','course']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['Branch','fullname','phone']

class MFYAdmin(admin.ModelAdmin):
    list_display=['branch','name']

class Course_PartAdmin(admin.ModelAdmin):
    list_display=['course','name']

class SectorAdmin(admin.ModelAdmin):
    list_display=['branch','name']

admin.site.register(Sector,SectorAdmin)
admin.site.register(Course_Part,Course_PartAdmin)
admin.site.register(MFY,MFYAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Register,RegisterAdmin)


