# Generated by Django 4.1.5 on 2023-01-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0042_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.IntegerField(default=1, max_length=10),
        ),
    ]