from django.db import models

class Teaching(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=4000, default='', null=True, blank=True)
    subtitle = models.FileField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='teachings/audio/', max_length=400, blank=True, null=True)
    image = models.ImageField(upload_to='teachings/images', max_length=400, blank=True, null=True)

    def __str__(self):
            return f"{self.title}"
    


# name
# desc
# date
# file