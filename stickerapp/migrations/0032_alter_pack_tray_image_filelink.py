# Generated by Django 4.1.5 on 2023-01-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0031_alter_pack_publisher_website_zip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='tray_image_filelink',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]