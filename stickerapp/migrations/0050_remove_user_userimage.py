# Generated by Django 4.1.5 on 2023-01-17 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0049_alter_pack_is_private_user_alter_approve_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userimage',
        ),
    ]
