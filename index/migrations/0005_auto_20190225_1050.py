# Generated by Django 2.0.9 on 2019-02-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='picture/%Y/%m/%d'),
        ),
    ]
