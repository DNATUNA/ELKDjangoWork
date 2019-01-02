from django.contrib import admin

# Register your models here.

from .models import LogInfo
from .models import HostInfo
from .models import AppInfo
from .models import MonthlyTranInfo

admin.site.register(LogInfo)
admin.site.register(HostInfo)
admin.site.register(AppInfo)
admin.site.register(MonthlyTranInfo)
