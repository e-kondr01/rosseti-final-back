# Generated by Django 3.1.2 on 2020-11-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201128_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='experience',
            field=models.CharField(max_length=128),
        ),
    ]
