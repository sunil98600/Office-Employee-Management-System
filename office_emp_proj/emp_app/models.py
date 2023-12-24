from django.db import models

# Create your models here.
class Departments(models.Model):
  name=models.CharField(max_length=255,null=False)
  location= models.CharField(max_length=100)
   
  def __str__(self):
    return self.name
  
class Role(models.Model):
  name=models.CharField(max_length=255,null=False)
  
  def __str__(self):
    return self.name
  
class Employee(models.Model):
  firstname=models.CharField(max_length=255)
  lastname=models.CharField(max_length=255)
  dept = models.ForeignKey(Departments,on_delete=models.CASCADE)
  salary=models.IntegerField(default=0)
  bonus=models.IntegerField(default=0)
  role=models.ForeignKey(Role,on_delete=models.CASCADE)
  phone = models.IntegerField(default=0)
  hire_date=models.DateField()
  
  
  def __str__(self):
    return "%s %s %s " %(self.firstname , self.lastname, self.phone)
  