from django.contrib import admin
from .models import *

from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','catname')



@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_id', 'sticker_list_size', 'preview_tray_image', 'pack_identifier', 'tag_name', 'updatedAt',
                    'tray_image_fileName',  'premium','user', 'avoid_cache', 'publisher_name',
                    'publisher_email', 'publisher_website_zip', 'license_Agreement_Link', 'privacy_policy')
    search_fields = ('id', 'tag_name', 'pack_identifier','publisher_email')

    def preview_tray_image(self, obj):
        if obj.tray_image_filelink:
            return format_html('<img src="{}" width="50px" height="50px" />', obj.tray_image_filelink.url)
        return ''
    preview_tray_image.short_description = 'Tray Image Preview'  # Set the column header name

    

    
@admin.register(StickerList)
class StickerListAdmin(admin.ModelAdmin):
    list_display = ('id','pack', 'sticker_name', 'preview_tray_image')
    search_fields = ('id', 'sticker_name')
    def preview_tray_image(self, obj):
        if obj.sticker:
            return format_html('<img src="{}" width="50px" height="50px" />', obj.sticker.url)
        return ''
    preview_tray_image.short_description = 'Tray Image Preview' 


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id','pack','user','reason')    

