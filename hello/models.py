from django.db import models
 
class Visit(models.Model): 
 created_at = models.DateTimeField(auto_now_add=True) 


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
