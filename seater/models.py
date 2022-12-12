from django.db import models
 
# Create your models here.
class student(models.Model):
    studentID = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=30)
    front = models.BooleanField(default=False)
 
    class Meta:
        db_table = 'student'
 
    def __str__(self):
        return f'{self.fName}-{self.lName}-{self.studentID}'


class restriction(models.Model):
    studentID = models.ForeignKey(student, on_delete=models.CASCADE, related_name='student_id_set')
    badID = models.ForeignKey(student, on_delete=models.DO_NOTHING, related_name='bad_id_set')
 
    class Meta:
        db_table = 'restriction'

    def __str__(self):
        return f'{self.studentID}-{self.badID}'