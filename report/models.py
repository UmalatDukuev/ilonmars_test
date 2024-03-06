from django.db import models

# Create your models here.

class Scientist(models.Model):
    planet = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    scientist_id = models.ForeignKey('Scientist', on_delete=models.CASCADE)

class ReceivedReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    absolut_path = models.CharField(max_length=255)

class SentReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    character_count_max = models.IntegerField()
    character_count_sent = models.IntegerField()
    absolut_path = models.CharField(max_length=255)