from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=90, null= False, blank= True)
    email = models.EmailField(max_length=90, null=False, blank= True)
    subject = models.CharField(max_length=90, null=False, blank= True)
    message = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name
