from typing import Any
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
import datetime
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name
    
class Employ_info(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    
    dateaddeed = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.emp_id.name

@receiver(post_save,sender =Employee)
def employ_info_add(sender,instance,**kwargs):
    Employ_info.objects.create(emp_id  = instance)



@receiver(pre_save,sender = Employee)
def empl_details(sender,instance,**kwargs):
    print(instance.name)