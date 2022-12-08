# Generated by Django 4.1.3 on 2022-12-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_delete_nutrition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('serving_size', models.CharField(default=0, max_length=5)),
                ('total_content', models.CharField(default=0, max_length=5)),
                ('calories', models.CharField(default=0, max_length=5)),
                ('protein', models.CharField(default=0, max_length=5)),
                ('fat', models.CharField(default=0, max_length=5)),
                ('carbohydrate', models.CharField(default=0, max_length=5)),
                ('sugars', models.CharField(default=0, max_length=5)),
                ('dietary_fiber', models.CharField(default=0, max_length=5)),
                ('calcium', models.CharField(default=0, max_length=5)),
                ('iron', models.CharField(default=0, max_length=5)),
                ('potassium', models.CharField(default=0, max_length=5)),
                ('sodium', models.CharField(default=0, max_length=5)),
                ('vitamin', models.CharField(default=0, max_length=5)),
                ('cholesterol', models.CharField(default=0, max_length=5)),
                ('total_fat', models.CharField(default=0, max_length=5)),
            ],
        ),
    ]