from django import forms
from .models import PatientInfo

class GeneralForm(forms.ModelForm):
    class Meta:
        model=PatientInfo
        fields=["age", "weight", "height", "bmi", "blood_group", "pulse_rate", "rr", 
                "cycle", "cycle_length", "pregnant", "num_abortions", 
                "hip", "waist", "waist_hip_ratio", "weight_gain", "hair_growth",
                "skin_darkening", "hair_loss", "pimples", "fast_food", 
                "regular_exercise", "bp_systolic", "bp_diastolic",]
        widgets = {
            'bmi': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'waist_hip_ratio': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }

class MedicalForm(forms.ModelForm):
    class Meta:
        model=PatientInfo
        fields='__all__'
        widgets = {
            'bmi': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'waist_hip_ratio': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }