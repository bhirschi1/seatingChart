from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
 
# Create your models here.
class student(models.Model):
    studentID = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=30)
    restrictionNum = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(30)])
 
    class Meta:
        db_table = 'student'
 
    def __str__(self):
        return f'{self.fName}-{self.lName}-{self.restrictionNum}'