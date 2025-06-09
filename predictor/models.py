from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class PatientInfo(models.Model):
    age = models.IntegerField( verbose_name="Age (yrs)",validators=[MinValueValidator(0)])
    weight = models.FloatField( verbose_name="Weight (Kg)",validators=[MinValueValidator(0)])
    height = models.FloatField( verbose_name="Height (Cm)",validators=[MinValueValidator(0)])
    bmi = models.FloatField( verbose_name="BMI")
    blood_group = models.IntegerField( verbose_name="Blood Group",
                                      choices=[(11,'A+'),(12,'A-'),(13,'B+'),(14,'B-'),
                                    (15,'O+'),(16,'O-'),(17,'AB+'),(18,'AB-')])
    pulse_rate = models.IntegerField( verbose_name="Pulse rate (bpm)")
    rr = models.IntegerField( verbose_name="RR (breaths/min)")
    hb = models.FloatField(null=True, blank=True, verbose_name="Hemoglobin (g/dl)")
    cycle = models.IntegerField( verbose_name="Cycle (R/I)", choices=[(2,'Regular'),(4,'Irregular')])
    cycle_length = models.IntegerField( verbose_name="Cycle length (days)")
    marriage_status_years = models.FloatField(null=True, blank=True, verbose_name="Marriage Status (Yrs)",validators=[MinValueValidator(0)])
    pregnant = models.IntegerField( verbose_name="Pregnant (Y/N)", choices=[(1,'Yes'),(0,'No')])
    num_abortions = models.IntegerField( verbose_name="No. of abortions")
    beta_hcg_1 = models.FloatField(null=True, blank=True, verbose_name="I beta-HCG (mIU/mL)")
    beta_hcg_2 = models.FloatField(null=True, blank=True, verbose_name="II beta-HCG (mIU/mL)")
    fsh = models.FloatField(null=True, blank=True, verbose_name="FSH (mIU/mL)")
    lh = models.FloatField(null=True, blank=True, verbose_name="LH (mIU/mL)")
    fsh_lh_ratio = models.FloatField(null=True, blank=True, verbose_name="FSH/LH")
    hip = models.IntegerField( verbose_name="Hip (inch)",validators=[MinValueValidator(0)])
    waist = models.IntegerField( verbose_name="Waist (inch)",validators=[MinValueValidator(0)])
    waist_hip_ratio = models.FloatField( verbose_name="Waist:Hip Ratio")
    tsh = models.FloatField(null=True, blank=True, verbose_name="TSH (mIU/L)")
    amh = models.FloatField(null=True, blank=True, verbose_name="AMH (ng/mL)")
    prl = models.FloatField(null=True, blank=True, verbose_name="PRL (ng/mL)")
    vit_d3 = models.FloatField(null=True, blank=True, verbose_name="Vit D3 (ng/mL)")
    prg = models.FloatField(null=True, blank=True, verbose_name="PRG (ng/mL)")
    rbs = models.FloatField(null=True, blank=True, verbose_name="RBS (mg/dl)")
    weight_gain = models.IntegerField( verbose_name="Weight gain (Y/N)", choices=[(1,'Yes'),(0,'No')])
    hair_growth = models.IntegerField( verbose_name="Body hair growth (Y/N)", choices=[(1,'Yes'),(0,'No')])
    skin_darkening = models.IntegerField( verbose_name="Skin darkening (Y/N)", choices=[(1,'Yes'),(0,'No')])
    hair_loss = models.IntegerField( verbose_name="Hair loss (Y/N)", choices=[(1,'Yes'),(0,'No')])
    pimples = models.IntegerField( verbose_name="Pimples (Y/N)", choices=[(1,'Yes'),(0,'No')])
    fast_food = models.FloatField( verbose_name="Fast food (Y/N)", choices=[(1,'Yes'),(0,'No')])
    regular_exercise = models.IntegerField( verbose_name="Regular Exercise (Y/N)", choices=[(1,'Yes'),(0,'No')])
    bp_systolic = models.IntegerField( verbose_name="BP Systolic (mmHg)")
    bp_diastolic = models.IntegerField( verbose_name="BP Diastolic (mmHg)")
    follicle_no_l = models.IntegerField(null=True, blank=True, verbose_name="Follicle No. (L)")
    follicle_no_r = models.IntegerField(null=True, blank=True, verbose_name="Follicle No. (R)")
    avg_f_size_l = models.FloatField(null=True, blank=True, verbose_name="Avg. F size (L) (mm)")
    avg_f_size_r = models.FloatField(null=True, blank=True, verbose_name="Avg. F size (R) (mm)")
    endometrium = models.FloatField(null=True, blank=True, verbose_name="Endometrium (mm)")

    def __str__(self):
        return f"Patient {self.id} - Age {self.age}"