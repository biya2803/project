# Generated by Django 4.2.7 on 2023-12-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_mycart'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
