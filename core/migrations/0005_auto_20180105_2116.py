# Generated by Django 2.0 on 2018-01-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
