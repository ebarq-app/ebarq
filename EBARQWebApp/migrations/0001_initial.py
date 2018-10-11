# Generated by Django 2.1 on 2018-10-11 07:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('event', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('additional', models.CharField(max_length=250)),
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
            ],
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whorl', models.ImageField(upload_to='')),
                ('side_face', models.ImageField(upload_to='')),
                ('full_side', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6)),
                ('date_of_birth', models.DateField()),
                ('weight', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1700), django.core.validators.MinValueValidator(150)])),
                ('height', models.IntegerField(validators=[django.core.validators.MaxValueValidator(250), django.core.validators.MinValueValidator(50)])),
            ],
        ),
        migrations.CreateModel(
            name='HorseOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('display_image', models.ImageField(default='user.png', upload_to='')),
                ('contact_number', models.CharField(blank=True, default='0000000000', max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{10}$')])),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EBARQWebApp.Horse')),
            ],
        ),
        migrations.AddField(
            model_name='horse',
            name='horse_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EBARQWebApp.HorseOwner'),
        ),
        migrations.AddField(
            model_name='addreminder',
            name='horse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EBARQWebApp.Horse'),
        ),
        migrations.AddField(
            model_name='addperformance',
            name='horse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EBARQWebApp.Horse'),
        ),
    ]
