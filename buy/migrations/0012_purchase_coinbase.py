# Generated by Django 2.0.6 on 2018-06-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0011_purchase_stripe'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='coinbase',
            field=models.DateTimeField(null=True),
        ),
    ]
