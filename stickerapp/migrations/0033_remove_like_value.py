# Generated by Django 4.1.5 on 2023-01-13 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0032_alter_pack_tray_image_filelink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
    ]
