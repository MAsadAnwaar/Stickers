# Generated by Django 4.1.5 on 2023-01-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0033_remove_like_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike')], default='Like', max_length=10),
        ),
    ]
