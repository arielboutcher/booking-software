# Generated by Django 3.0.4 on 2020-03-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alabooking', '0003_auto_20200321_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timeToBeUsedFrom',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='timeToBeUsedTo',
            field=models.TimeField(null=True),
        ),
    ]
