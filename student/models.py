from django.db import models


class StudentList(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=150)
    std_class = models.CharField(max_length=150)
    gender = models.CharField(max_length=150)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

