# Generated by Django 4.1.5 on 2023-01-13 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0020_remove_pack_liked_pack_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='liked',
        ),
    ]