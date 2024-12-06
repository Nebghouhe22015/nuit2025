from django.db import models
class Lalaland(models.Model):
    message = models.CharField(max_length=100, default="Hello World from Lalaland!")
    
    def __str__(self):
        return self.message

class Iur(models.Model):
    useless_data = models.CharField(max_length=100, default="Useless Data")
    
    def __str__(self):
        return self.useless_data

class Stm(models.Model):
    pass
