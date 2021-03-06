# Generated by Django 2.0.4 on 2018-06-01 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zad2', '0009_auto_20180525_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaneCrew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='plane',
            name='crew',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='zad2.PlaneCrew'),
            preserve_default=False,
        ),
    ]
