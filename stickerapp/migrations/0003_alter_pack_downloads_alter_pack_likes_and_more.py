# Generated by Django 4.1.10 on 2023-10-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0002_remove_pack_downloads_remove_pack_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pack',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pack',
            name='watched',
            field=models.IntegerField(default=0),
        ),
    ]
