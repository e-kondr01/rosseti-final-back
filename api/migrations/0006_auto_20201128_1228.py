# Generated by Django 3.1.2 on 2020-11-28 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0005_auto_20201128_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='moderator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moderated_proposals', to=settings.AUTH_USER_MODEL),
        ),
    ]
