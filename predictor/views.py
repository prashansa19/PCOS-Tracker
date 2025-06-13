from django.shortcuts import render,redirect
from .forms import GeneralForm,MedicalForm
from .models import PatientInfo
import joblib
import numpy as np
from django.forms.models import model_to_dict

# Create your views here.
def home_page(request):
    return render(request,'predictor/home.html')

def general_create_view(request):
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            instance=form.save()
            return redirect('result_view',pk=instance.pk)
    else:
        form = GeneralForm()  
    
    return render(request, 'predictor/general.html', {'form': form})

def medical_create_view(request):
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            instance=form.save()
            return redirect('result_view',pk=instance.pk)
    else:
        form = MedicalForm()  
    
    return render(request, 'predictor/medical.html', {'form': form})

from django.shortcuts import get_object_or_404

def result_view(request, pk):
    instance = get_object_or_404(PatientInfo, pk=pk)
    form_data = {
        field.verbose_name: getattr(instance, field.name)
        for field in instance._meta.fields[1:]
        if getattr(instance, field.name) not in [None, '', []]
    }
    input_data = np.array([list(form_data.values())], dtype=float)
    print('-----------------------------------\nlen of input array:'+str(input_data.shape))
    if input_data.shape[1]==23:
        model = joblib.load('predictor_23.pkl')
        prediction = model.predict(input_data).tolist()
    else:
        model = joblib.load('predictor_40.pkl')
        prediction = model.predict(input_data).tolist()
    if prediction:
        result="You results are positive. You have PCOS"
    else:
        result="You results are Negative. You don't have PCOS."
    context={
        'form_data': form_data,
        'result': result
    }
    return render(request, 'predictor/result.html', context)
