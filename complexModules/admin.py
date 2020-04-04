from django.contrib import admin
from .models import scoringModel,submissionModel, gradeModel,currentRound
# Register your models here.

admin.site.register(submissionModel)
admin.site.register(gradeModel)
admin.site.register(scoringModel)
admin.site.register(currentRound)