# Generated by Django 3.1.2 on 2020-11-28 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201128_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='draft',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='draft', to='api.proposaldraft'),
        ),
    ]
