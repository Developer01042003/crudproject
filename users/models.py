from django.db import models
from django.contrib.auth.models import User

# Create your models here.





from django.db import models
from django.contrib.auth.models import User

class FormSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    campname = models.CharField(max_length=25)

    idname = models.CharField(max_length=100)

    amount = models.FloatField(default=0.00)

    approve = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.campname
    # Add other fields for the form submission (e.g., form data, timestamp, etc.)





