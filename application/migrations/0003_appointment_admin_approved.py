# Generated by Django 3.2.9 on 2022-06-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]
