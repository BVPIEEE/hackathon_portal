from django.contrib import admin
from .models import team, phaseSelectionModel, manageTeam


class teamAdmin(admin.ModelAdmin):
    list_display = ("team_name", "team_leader_github")
    search_fields = ("team_name", "team_leader_github")


class selectionAdmin(admin.ModelAdmin):
    list_display = ("team", "round")
    search_fields = ("team__team_name", "round")


class manageAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    search_fields = ("user__username", "role")


admin.site.register(team, teamAdmin)
admin.site.register(phaseSelectionModel, selectionAdmin)
admin.site.register(manageTeam, manageAdmin)
