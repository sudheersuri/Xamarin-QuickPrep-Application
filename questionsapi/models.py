from django.db import models

class subjects(models.Model):
    subjectname=models.CharField(max_length=30)
    class Meta:
        db_table='Subjects'
        unique_together=(('subjectname','id'))
        
# Create your models here.
class Questions(models.Model):
    subject=models.ForeignKey(subjects,on_delete=models.CASCADE)
    question=models.CharField(max_length=500)
    answer=models.CharField(max_length=1000)
    class Meta:
        db_table='Questions'

