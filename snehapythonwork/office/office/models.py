from calendar import c
from django. db import models 
 
 class office(models.Model):
     company_name = models.CharField(max_langth=200)
     email = models.CharField(max_length=500)
     company_code = models.CharField(max_length=500)
     website = models.models.CharField(max_length=500)
     
     
     def __str__(self):
         return self.name + '' + self.email