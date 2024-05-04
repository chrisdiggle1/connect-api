# Generated by Django 3.2.25 on 2024-05-01 16:41

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(blank=True, null=True, validators=[events.models.validate_event_date]),
        ),
    ]