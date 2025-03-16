from django.db import models

class Teaching(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=4000, default='', null=True, blank=True)
    subtitle = models.FileField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='teachings/audio/', max_length=400, blank=True, null=True)
    image = models.ImageField(upload_to='teachings/images', max_length=400, blank=True, null=True)
    series = models.ManyToManyField('Series', through='SeriesPart', related_name='teaching')

    def __str__(self):
            return f"{self.title}"
    
class Category(models.Model):
      title = models.CharField(max_length=15)

class Series(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=4000, default='', null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='teachings/images', max_length=400, blank=True, null=True)

    class Meta:
         verbose_name = 'Series\''
         verbose_name_plural = 'Series'

    def __str__(self):
         return f'{self.title}'
   
class SeriesPart(models.Model):
    teaching = models.ForeignKey(Teaching, on_delete=models.DO_NOTHING)
    series = models.ForeignKey(Series, on_delete=models.DO_NOTHING, related_name='seriespart')
    position = models.PositiveSmallIntegerField()

    def __str__(self):
         return f'{self.series} - {self.position} {self.teaching}'
    # unique_together = ('book', 'author')


# name
# desc
# date
# file