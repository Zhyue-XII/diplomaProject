# Generated by Django 2.0.9 on 2019-02-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='记录', max_length=50)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': '足迹',
                'verbose_name_plural': '足迹',
            },
        ),
        migrations.AlterField(
            model_name='discuss',
            name='img',
            field=models.TextField(),
        ),
    ]
