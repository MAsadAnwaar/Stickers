# Generated by Django 4.1.5 on 2023-01-10 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stickerapp', '0010_rename_subcats_id_pack_sub_cats_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='sticker_List_size',
            new_name='sticker_list_size',
        ),
        migrations.RenameField(
            model_name='pack',
            old_name='tray_Image_FileName',
            new_name='tray_image_fileName',
        ),
        migrations.RenameField(
            model_name='pack',
            old_name='tray_Image_FileLink',
            new_name='tray_image_filelink',
        ),
    ]
