# Generated by Django 4.1.5 on 2023-01-16 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0041_rename_cat_category_rename_subcats_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.IntegerField(max_length=10),
        ),
    ]