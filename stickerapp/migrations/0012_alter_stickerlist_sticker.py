# Generated by Django 4.1.5 on 2023-01-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0011_rename_sticker_list_size_pack_sticker_list_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickerlist',
            name='sticker',
            field=models.FileField(max_length=30, upload_to=''),
        ),
    ]
