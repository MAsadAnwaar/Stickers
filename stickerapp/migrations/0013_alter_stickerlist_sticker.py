# Generated by Django 4.1.5 on 2023-01-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0012_alter_stickerlist_sticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickerlist',
            name='sticker',
            field=models.FileField(upload_to='media/storesticker'),
        ),
    ]
