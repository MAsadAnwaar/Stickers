# Generated by Django 4.2.2 on 2023-06-21 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0050_remove_user_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='User',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stickerapp.user'),
        ),
        migrations.AlterField(
            model_name='pack',
            name='publisher_website_zip',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
