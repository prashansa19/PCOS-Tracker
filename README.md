# Project Title
Django project

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="number" id="weight" name="weight" step="0.1">
  <input type="number" id="height" name="height" step="0.01">
  <input type="number" id="bmi" name="bmi" step="0.01" readonly>
  <button type="submit">Submit</button>
</form>

<script>
  document.getElementById('weight').addEventListener('input', calculateBMI);
  document.getElementById('height').addEventListener('input', calculateBMI);

  function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    if (weight && height) {
      const bmi = weight / (height * height);
      document.getElementById('bmi').value = bmi.toFixed(2);
    }
  }
</script>
Also make sure user cannot change bmi only auto calculated one
Don’t show ratio in form just form, add it in the backend


model_input = [form.cleaned_data[feature] for feature in FEATURE_ORDER_23]


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set required fields in form only
        self.fields['age'].required = True
        self.fields['weight'].required = True
        # others optional unless you set required=True
