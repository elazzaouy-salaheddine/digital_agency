# Generated by Django 3.2 on 2021-04-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_intro_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeservices',
            name='logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
