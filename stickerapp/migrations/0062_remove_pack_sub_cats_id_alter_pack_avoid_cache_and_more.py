# Generated by Django 4.1.7 on 2023-06-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0061_pack_description_pack_downloads_pack_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='sub_cats_id',
        ),
        migrations.AlterField(
            model_name='pack',
            name='avoid_cache',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pack',
            name='premium',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='Sub_Category',
        ),
    ]
