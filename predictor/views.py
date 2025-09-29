from django.shortcuts import render,redirect, get_object_or_404
from .forms import GeneralForm,MedicalForm
from .models import PatientInfo, PredictionHistory
import joblib
import numpy as np
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest

def start_page(request):
        return redirect('home')

def home_page(request):
    return render(request,'predictor/home.html')

def general_create_view(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to access this page.")
        return redirect("login")
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            if instance.waist and instance.hip:
                instance.waist_hip_ratio = round(instance.waist / instance.hip, 2)
            instance.save()
            form_data = {
                field.verbose_name: getattr(instance, field.name)
                for field in instance._meta.fields[1:]
                if getattr(instance, field.name) not in [None, '', []]
            }
            input_data = np.array([list(form_data.values())], dtype=float)
            model = joblib.load('ML/predictor_23.pkl')
            prediction = model.predict(input_data).tolist()
            PredictionHistory.objects.create(user=request.user, result=prediction, patient_id=instance.pk, type="General")
            return redirect('result_view',pk=instance.pk)
    else:
        form = GeneralForm()  
    
    return render(request, 'predictor/general.html', {'form': form})

def medical_create_view(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to access this page.")
        return redirect("login")
    if request.method == 'POST':
        form = MedicalForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            if instance.waist and instance.hip:
                instance.waist_hip_ratio = round(instance.waist / instance.hip, 2)
            instance.save()
            form_data = {
                field.verbose_name: getattr(instance, field.name)
                for field in instance._meta.fields[1:]
                if getattr(instance, field.name) not in [None, '', []]
            }
            input_data = np.array([list(form_data.values())], dtype=float)
            model = joblib.load('ML/predictor_40.pkl')
            prediction = model.predict(input_data).tolist()
            PredictionHistory.objects.create(user=request.user, result=prediction, patient_id=instance.pk, type="Medical")
            return redirect('result_view',pk=instance.pk)
    else:
        form = MedicalForm()  
    
    return render(request, 'predictor/medical.html', {'form': form})

def result_view(request, pk):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to view results.")
        return redirect("login")
    instance = get_object_or_404(PatientInfo, pk=pk)
    form_data = {
        field.verbose_name: getattr(instance, field.name)
        for field in instance._meta.fields[1:]
        if getattr(instance, field.name) not in [None, '', []]
    }
    historyinstance = PredictionHistory.objects.filter(patient_id=pk).last()

    context={
        'form_data': form_data,
        'result': "Your results are positive. You have PCOS" if historyinstance.result else "Your results are negative. You dont have PCOS"
    }
    return render(request, 'predictor/result.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request,"User created successfully")
                return redirect('login')
        else:
            messages.info(request,"Passwords do not match")
            return redirect('register')
    return render(request, 'predictor/register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        # Handle registration logic here
        # For example, save user data to the database
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request, 'predictor/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def history(request):
    if not request.user.is_authenticated:
        messages.info(request,"Please login to view your history")
        return redirect('login')
    
    patients = PredictionHistory.objects.filter(user=request.user).order_by('-created_at')
    records=[]
    for patient in patients:
        record = {
            'id': patient.patient_id,
            'result': "Positive" if patient.result else "Negative",
            'type': patient.type,
            'created_at': patient.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        records.append(record)
    context = {
        'records': records
    }
    
    return render(request, 'predictor/history.html', context)

def edit_view(request, type, pk):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to access this page.")
        return redirect("login")
    if type == "General":
        FormClass = GeneralForm
        model_path = 'ML/predictor_23.pkl'
        template_name = 'predictor/general.html'
    elif type == "Medical":
        FormClass = MedicalForm
        model_path = 'ML/predictor_40.pkl'
        template_name = 'predictor/medical.html'
    else:
        return HttpResponseBadRequest("Invalid form type.")

    instance = get_object_or_404(PatientInfo, pk=pk)

    if request.method == 'POST':
        form = FormClass(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)

            # Recalculate waist_hip_ratio if both values exist
            if instance.waist and instance.hip:
                instance.waist_hip_ratio = round(instance.waist / instance.hip, 2)

            instance.save()
            form_fields = [field.name for field in instance._meta.fields[1:]]
            print(f"Form fields: {form_fields}")
            values = [getattr(instance, f) for f in form_fields if getattr(instance, f) not in [None, '', []]]

            try:
                input_data = np.array([values], dtype=float)
                model = joblib.load(model_path)
                prediction = model.predict(input_data).tolist()
            except Exception as e:
                return HttpResponseBadRequest(f"Prediction failed: {str(e)}")

            # Save or update prediction history
            PredictionHistory.objects.update_or_create(
                user=request.user,
                patient_id=instance.pk,
                defaults={'result': prediction, 'type': type.capitalize()}
            )

            return redirect('result_view', pk=instance.pk)
    else:
        form = FormClass(instance=instance)

    return render(request, template_name, {'form': form, 'edit': True})
