# Generated by Django 4.1.7 on 2023-06-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0058_pack_isnew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='avoid_cache',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pack',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]