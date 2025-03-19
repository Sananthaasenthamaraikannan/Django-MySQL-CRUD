from django.db import models

# Create your model (module) models
    
class RegisterForm(models.Model):
    PHASE_CHOICES = [
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ]
    Studyname= models.CharField(max_length=100)
    study_description= models.CharField(max_length=100)
    study_phase= models.CharField(max_length=50,choices=PHASE_CHOICES)
    sponsor_name= models.CharField(max_length=100)
    
    class Meta:
        db_table='datas'