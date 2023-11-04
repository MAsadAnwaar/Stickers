from django.contrib import admin
from .models import *

from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','catname')



@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_id', 'sticker_list_size','pack_status','premium', 'preview_tray_image', 'pack_identifier', 'tag_name', 'updatedAt',
                    'tray_image_fileName',  'user', 'avoid_cache', 'publisher_name',
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

class countrytagAdmin(admin.ModelAdmin):
    list_display = ('id', 'relpack', 'countrytag')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "relpack":
            # Get the primary key (id) of the "Religion" category
            religion_category_id = Category.objects.get(catname="Events").pk
            # Filter the queryset for the pack field to show only the "Religion" packs
            kwargs["queryset"] = Pack.objects.filter(cat_id=religion_category_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(countrytag, countrytagAdmin)


class religiontagAdmin(admin.ModelAdmin):
    list_display = ('id', 'religionpack', 'religiontag')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "religionpack":
            # Get the primary key (id) of the "Events" category
            events_category_id = Category.objects.get(catname="Religion").pk
            # Filter the queryset for the pack field to show only the "Events" packs
            kwargs["queryset"] = Pack.objects.filter(cat_id=events_category_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(religiontag, religiontagAdmin)


# @admin.register(Report)
# class ReportAdmin(admin.ModelAdmin):
#     list_display = ('id','pack','user','reason')    

