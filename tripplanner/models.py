from django.db import models
import datetime


class Station(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Line(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class StationOrder(models.Model):
    station_from = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='from+')
    station_to = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='to+')
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    distance = models.IntegerField()

    def __str__(self):
        return f'{self.station_from} -> {self.station_to};'


class Service(models.Model):
    fee = models.IntegerField(default=1)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.line}: {self.fee}'


class TimetableData(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date_time = models.TimeField()
    delay = models.DurationField(default=datetime.timedelta)

    def __str__(self):
        return f'{self.service.line} ({self.station}): {self.date_time}'
