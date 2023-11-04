# Generated by Django 4.1.5 on 2023-01-13 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0019_pack_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='liked',
        ),
        migrations.AddField(
            model_name='pack',
            name='liked',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Like', to='stickerapp.user'),
        ),
    ]
