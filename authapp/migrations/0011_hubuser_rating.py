# Generated by Django 3.1.7 on 2021-05-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_remove_hubuser_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubuser',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='рейтинг пользователя'),
        ),
    ]
