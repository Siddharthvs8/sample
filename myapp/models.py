from django.db import models
class Stud(models.Model):

    stud_name=models.TextField(max_length=100)
    roll_no=models.IntegerField(default=0)
    std=models.IntegerField(default=0)
