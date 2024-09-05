from django.contrib import admin

# Register your models here.
from .models import *

class my_up(admin.ModelAdmin):
   pass
admin.site.register(My_Upload_file,my_up)

class my_qc(admin.ModelAdmin):
   pass
admin.site.register(my_Qc_data,my_qc)