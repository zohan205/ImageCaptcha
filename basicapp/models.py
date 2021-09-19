from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to="my_image")
    age_choice = (
            ('Child','Child'),
            ('Teenager','Teenager'),
            ('Adult','Adult'),
            ('Senior Adult','Senior Adult')
        )
    age = models.CharField(max_length=100,choices=age_choice, default='Child')
    gender_choice = (
            ('Male','Male'),
            ('Female','Female'),
        )
    gender = models.CharField(max_length=100,choices=gender_choice,default='Male')
