from django.contrib import admin
from .models import team, phaseSelectionModel, manageTeam


class teamAdmin(admin.ModelAdmin):
    list_display = ("team_name", "team_leader_github")
    search_fields = ("team_name", "team_leader_github")


class selectionAdmin(admin.ModelAdmin):
    list_display = ("team", "section1", "section2", "section3", "section4", "final")
    search_fields = ("team__team_name", "section1", "section2", "section3", "section4", "final")


class manageAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    search_fields = ("user__username", "role")


admin.site.register(team, teamAdmin)
admin.site.register(phaseSelectionModel, selectionAdmin)
admin.site.register(manageTeam, manageAdmin)
