# Generated by Django 2.0.4 on 2018-05-25 10:53

from django.db import migrations, models
import zad2.models


class Migration(migrations.Migration):

    dependencies = [
        ('zad2', '0008_auto_20180518_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='end_time',
            field=models.DateTimeField(validators=[zad2.models.clean1]),
        ),
        migrations.AlterField(
            model_name='flight',
            name='start_time',
            field=models.DateTimeField(validators=[zad2.models.clean1]),
        ),
    ]