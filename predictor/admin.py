from django.contrib import admin
from .models import PatientInfo, PredictionHistory
# Register your models here.

admin.site.register(PatientInfo)
admin.site.register(PredictionHistory)