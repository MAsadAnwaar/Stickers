# Generated by Django 4.1.5 on 2023-01-10 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0003_alter_stickerlist_sticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickerlist',
            name='sticker',
            field=models.ImageField(upload_to=''),
        ),
    ]
