from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(null=False)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    
