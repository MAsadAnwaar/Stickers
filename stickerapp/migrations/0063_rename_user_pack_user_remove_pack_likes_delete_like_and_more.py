# Generated by Django 4.1.7 on 2023-06-24 07:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stickerapp', '0062_remove_pack_sub_cats_id_alter_pack_avoid_cache_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='User',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='pack',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='pack',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_pack', to=settings.AUTH_USER_MODEL),
        ),
    ]