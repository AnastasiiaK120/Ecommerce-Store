# Generated by Django 3.2.7 on 2021-09-28 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]