# Generated by Django 3.0.8 on 2020-07-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='rating',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]