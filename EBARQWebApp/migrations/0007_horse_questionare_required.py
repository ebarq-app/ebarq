# Generated by Django 2.1 on 2018-10-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EBARQWebApp', '0006_addperformance_owner_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='horse',
            name='questionare_required',
            field=models.BooleanField(default=True),
        ),
    ]
