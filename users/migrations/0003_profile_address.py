# Generated by Django 3.2.4 on 2021-07-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210702_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Not entered', max_length=50),
        ),
    ]
