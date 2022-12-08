from django.db import models

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

class Nutrition(models.Model):
    name = models.CharField(max_length=50)    
    serving_size = models.IntegerField(default=0) # 1회 제공량
    total_content = models.IntegerField(default=0) # 총 내용량
    calories = models.IntegerField(default=0) # 에너지(칼로리)
    protein = models.FloatField(default=0) # 단백질
    fat = models.FloatField(default=0) # 지방
    carbohydrate = models.FloatField(default=0) # 탄수화물
    sugars = models.FloatField(default=0) # 총 당류
    dietary_fiber= models.IntegerField(default=0) # 총 식이섬유
    calcium = models.IntegerField(default=0) # 칼슘
    iron = models.IntegerField(default=0) # 철
    potassium = models.IntegerField(default=0) # 칼륨
    sodium = models.IntegerField(default=0) # 나트륨
    vitamin = models.IntegerField(default=0) # 비타민
    cholesterol =models.IntegerField(default=0) # 콜레스테롤
    total_fat= models.IntegerField(default=0) # 총 지방산
    