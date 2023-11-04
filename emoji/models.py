from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
import os

# category class
class Category(models.Model):
    catname = models.CharField(max_length=50)
    titleImage = models.ImageField(blank=True,upload_to='titleImage')

    
    def __str__(self):
        return self.catname

def pack_directory_path(instance, filename):
    # This function generates the directory path for the pack files
    return f'packs/{instance.pack_identifier}/{filename}'

class Pack(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    animated_sticker_pack = models.BooleanField(default=False)
    pack_identifier = models.CharField(max_length=50, null=True)
    tag_name = models.CharField(max_length=50)
    tray_image_filelink = models.ImageField(blank=True, upload_to=pack_directory_path)
    tray_image_fileName = models.CharField(max_length=50)
    STATUS_CHOICES = (
        (0, 'Regular'),
        (1, 'Trending'),
        (2, 'Featured'),
        (3, 'Festive'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    bannner_image = models.ImageField(default="defualt/banner.png", upload_to=pack_directory_path)
    featured_image = models.ImageField(default="defualt/featured.png", upload_to=pack_directory_path)
    sticker_list_size = models.IntegerField(blank=True)
    premium = models.BooleanField(default=False)
    avoid_cache = models.BooleanField(default=False)
    publisher_name = models.CharField(max_length=50, blank=True)
    publisher_email = models.EmailField(blank=True)
    publisher_website_zip = models.FileField(blank=True, upload_to=pack_directory_path)
    license_Agreement_Link = models.URLField(blank=True)
    privacy_policy = models.TextField(blank=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isNew = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_pack', blank=True)
    watched = models.ManyToManyField(User, related_name='watched_pack', blank=True)
    downloads = models.ManyToManyField(User, related_name='downloaded_pack', blank=True)
    description = models.CharField(max_length=70, default="Download this Amazing Pack")
    

    def save(self, *args, **kwargs):
        # Generate the pack name folder
        pack_directory = f'packs/{self.pack_identifier}'
        if not os.path.exists(pack_directory):
            os.makedirs(pack_directory)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.pack_identifier

def sticker_directory_path(instance, filename):
    # This function generates the directory path for the sticker files
    pack_identifier = instance.pack.pack_identifier
    return f'packs/{pack_identifier}/{filename}'

class StickerList(models.Model):
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    sticker_name = models.CharField(max_length=50,null=True)
    sticker = models.FileField(upload_to=sticker_directory_path)
    def save(self, *args, **kwargs):
     if self.sticker:
        self.sticker_name = self.sticker.name
        
     super(StickerList, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.sticker_name


class Report(models.Model):
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()

