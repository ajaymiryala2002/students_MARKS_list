from django.contrib import admin
from marks_list.models import student

class studentADMIN(admin.ModelAdmin):
   list_display=['Hallticket_NO','student_name','TELUGU','HINDI','ENGLISH','MATHS','SCIENCE','SOCIAL']
admin.site.register(student,studentADMIN)
