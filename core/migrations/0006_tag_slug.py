# Generated by Django 2.0 on 2018-01-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180105_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.CharField(default='vigil', max_length=255),
            preserve_default=False,
        ),
    ]
