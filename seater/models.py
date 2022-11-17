from django.db import models
 
# Create your models here.
class student(models.Model):
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=30)
    limitNum = models.IntegerField()
 
    class Meta:
        db_table = 'student'
 
    def __str__(self):
        return f'{self.fName}-{self.lName}-{self.limitNum}'