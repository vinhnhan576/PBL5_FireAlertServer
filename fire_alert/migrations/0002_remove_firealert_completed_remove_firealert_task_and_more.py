# Generated by Django 4.1.7 on 2023-02-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fire_alert', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firealert',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='firealert',
            name='task',
        ),
        migrations.RemoveField(
            model_name='firealert',
            name='updated',
        ),
        migrations.AddField(
            model_name='firealert',
            name='img',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='firealert',
            name='isFire',
            field=models.BooleanField(default=False),
        ),
    ]
