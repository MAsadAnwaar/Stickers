# Generated by Django 4.1.5 on 2023-01-10 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0004_alter_stickerlist_sticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='catname',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pack',
            name='Cat_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='stickerapp.cat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pack',
            name='SubCats_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stickerapp.subcats'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcats',
            name='name',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]