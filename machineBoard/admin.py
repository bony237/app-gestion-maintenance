from django.contrib import admin

from .models import MaintainerTeam, Defaillance, InfoIntervention, Machine

# Register your models here.


class MachineInline(admin.StackedInline):
    model = Machine.infoInterventionAll.through
    extra = 1


class InfoInterventionAdmin(admin.ModelAdmin):
    inlines = [MachineInline]


class MachineAdmin(admin.ModelAdmin):
    filter_horizontal = ("infoInterventionAll",)


admin.site.register(MaintainerTeam)
admin.site.register(Defaillance)
admin.site.register(InfoIntervention, InfoInterventionAdmin)
admin.site.register(Machine, MachineAdmin)
