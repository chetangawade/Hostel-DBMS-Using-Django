# Generated by Django 4.0.3 on 2022-05-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0002_girls'),
    ]

    operations = [
        migrations.AddField(
            model_name='boys',
            name='gender',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='girls',
            name='gender',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
