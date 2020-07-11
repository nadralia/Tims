# Generated by Django 3.0.7 on 2020-07-02 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itinerary', '0002_auto_20200702_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to=settings.AUTH_USER_MODEL),
        ),
    ]
