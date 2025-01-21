from django.db import models
from datetime import timedelta

class Track(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class LapTime(models.Model):
    track = models.ForeignKey(Track, related_name='lap_times', on_delete=models.CASCADE)
    time = models.CharField(max_length=12)
    date = models.DateField()
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.track.name} - {self.date} - {self.time}"