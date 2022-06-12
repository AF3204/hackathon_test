from django.contrib import admin
from .models import BusinessUnit, Mill, User, ActivityLog, Task, TaskHandover, Position, Shifts

admin.site.register(BusinessUnit)
admin.site.register(Mill)
admin.site.register(User)
admin.site.register(ActivityLog)
admin.site.register(Task)
admin.site.register(TaskHandover)
admin.site.register(Position)
admin.site.register(Shifts)