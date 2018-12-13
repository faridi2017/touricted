from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

admin.site.register([Leads,Aspnetusers,Attendance,Leaditems,Company,Aspnetroles,Leadstatus,Profilepics])
