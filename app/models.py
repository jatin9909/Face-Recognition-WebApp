from django.db import models

# Create your models here.
class FaceRecognition(models.Model):
    id = models.AutoField(primary_key=True)
    record_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')


    def __str__(self):
        return str(self.record_date)