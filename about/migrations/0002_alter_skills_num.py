# Generated by Django 3.2 on 2021-04-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='num',
            field=models.FloatField(),
        ),
    ]