from django.db import models

# Create your models here.

def validate_email(value):
    if email.endswith('.com'):
        raise forms.ValidationError("Invalid email adress")

class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(validators=[validate_email])
    Phone = models.CharField(max_length=10)
    Message = models.TextField()

    def __str__(self):
          return  self.Name 