# Generated by Django 4.2.7 on 2024-01-03 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_registration_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.registration')),
            ],
        ),
    ]