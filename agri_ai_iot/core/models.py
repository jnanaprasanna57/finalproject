from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SensorData(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    soil_moisture = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Prediction(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    irrigation_required = models.CharField(max_length=20)
    fertilizer_recommendation = models.CharField(max_length=200)
    yield_prediction = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
