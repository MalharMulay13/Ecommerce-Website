# Generated by Django 3.1.7 on 2021-03-15 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_updateorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]