from django.db import models

class student(models.Model):
    Hallticket_NO=models.IntegerField()
    student_name=models.CharField(max_length=20)
    TELUGU=models.IntegerField()
    HINDI=models.IntegerField()
    ENGLISH=models.IntegerField()
    MATHS=models.IntegerField()
    SCIENCE=models.IntegerField()
    SOCIAL=models.IntegerField()

    def __str__(self):
        return self.student_name
