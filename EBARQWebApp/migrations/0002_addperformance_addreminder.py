# Generated by Django 2.1 on 2018-10-03 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EBARQWebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('type', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('additional', models.CharField(max_length=250)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EBARQWebApp.Horse')),
            ],
        ),
        migrations.CreateModel(
            name='AddReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('notes', models.CharField(max_length=250)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EBARQWebApp.Horse')),
            ],
        ),
    ]
