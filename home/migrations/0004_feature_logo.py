# Generated by Django 3.2 on 2021-04-10 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homeservices_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='logo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
    ]
