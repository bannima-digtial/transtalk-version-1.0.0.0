# Generated by Django 5.0.6 on 2024-07-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0018_alter_vendormodel_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendormodel',
            name='payment',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vendormodel',
            name='profile_status',
            field=models.CharField(default='SHOW', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='vendormodel',
            name='subscription_period',
            field=models.CharField(default='SHOW', max_length=10, null=True),
        ),
    ]
