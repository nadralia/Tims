# Generated by Django 3.0.7 on 2020-07-02 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itinerary',
            options={'verbose_name_plural': 'itineraries'},
        ),
        migrations.RemoveField(
            model_name='itinerary',
            name='itinerarydescription',
        ),
    ]
