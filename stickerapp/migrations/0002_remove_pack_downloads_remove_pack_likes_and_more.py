# Generated by Django 4.1.10 on 2023-10-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='downloads',
        ),
        migrations.RemoveField(
            model_name='pack',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='pack',
            name='watched',
        ),
        migrations.AddField(
            model_name='pack',
            name='downloads',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pack',
            name='likes',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pack',
            name='watched',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
