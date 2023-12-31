# Generated by Django 4.2.2 on 2023-07-06 07:49

from django.db import migrations, models
import stickerapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0067_alter_pack_downloads_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='bannner_image',
            field=models.ImageField(default='defualt/banner.png', upload_to=stickerapp.models.pack_directory_path),
        ),
        migrations.AddField(
            model_name='pack',
            name='featured_image',
            field=models.ImageField(default='defualt/featured.png', upload_to=stickerapp.models.pack_directory_path),
        ),
        migrations.AddField(
            model_name='pack',
            name='status',
            field=models.IntegerField(choices=[(0, 'Regular'), (1, 'Trending'), (2, 'Featured'), (3, 'Festive')], default=0),
        ),
    ]
