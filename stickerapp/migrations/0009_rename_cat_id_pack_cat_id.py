# Generated by Django 4.1.5 on 2023-01-10 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0008_remove_cat_cat_name_cat_catname_alter_subcats_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='Cat_id',
            new_name='cat_id',
        ),
    ]
