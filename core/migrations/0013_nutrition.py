# Generated by Django 4.1.3 on 2022-12-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_delete_nutrition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('serving_size', models.IntegerField(default=0)),
                ('total_content', models.IntegerField(default=0)),
                ('calories', models.IntegerField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('fat', models.FloatField(default=0)),
                ('carbohydrate', models.FloatField(default=0)),
                ('sugars', models.FloatField(default=0)),
                ('dietary_fiber', models.IntegerField(default=0)),
                ('calcium', models.IntegerField(default=0)),
                ('iron', models.IntegerField(default=0)),
                ('potassium', models.IntegerField(default=0)),
                ('sodium', models.IntegerField(default=0)),
                ('vitamin', models.IntegerField(default=0)),
                ('cholesterol', models.IntegerField(default=0)),
                ('total_fat', models.IntegerField(default=0)),
            ],
        ),
    ]
