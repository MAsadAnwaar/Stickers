# Generated by Django 4.1.5 on 2023-01-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0047_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]
