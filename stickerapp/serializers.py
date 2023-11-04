from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework.fields import HiddenField
from django.contrib.auth.models import User

# user serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

from rest_framework import serializers
from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# Create serializers
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username','password','email',)
#         extra_kwargs    = {'password':{'write_only': True}}


#         def create(self , validated_data):
#             password = validated_data.pop("password")
#             user = User(**validated_data)
#             user.set_password(password)
#             user.save()
#             return {
#                 "username": user.username,
#                 "email" : user.email,
                
#             }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user






# cateory serializers
class Category_Serializer(serializers.ModelSerializer):
    # SubCats = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='SubCats')
    class Meta:
        
        model = Category
        fields = "__all__"


class Religiontag_Serializer(serializers.ModelSerializer):
    # SubCats = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='SubCats')
    class Meta:
        
        model = religiontag
        fields = "__all__"

class Countrytag_Serializer(serializers.ModelSerializer):
    # SubCats = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='SubCats')
    class Meta:
        
        model = countrytag
        fields = "__all__"

class StickerListSerializer(serializers.ModelSerializer):
    sticker = serializers.SerializerMethodField()

    class Meta:
        model = StickerList
        fields = ['sticker_name', 'sticker']

    def get_sticker(self, obj):
        request = self.context.get('request')
        if obj.sticker and hasattr(obj.sticker, 'url'):
            return request.build_absolute_uri(obj.sticker.url)
        return None




# pack serializers

class PackSerializer(serializers.ModelSerializer):
    cat_id = serializers.StringRelatedField(source='cat_id.catname')
    sticker_list = StickerListSerializer(many=True, read_only=True, source='stickerlist_set')
    likes = serializers.SerializerMethodField()
    watched = serializers.SerializerMethodField()
    downloads = serializers.SerializerMethodField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sticker_list'] = StickerListSerializer(instance.stickerlist_set.all(), many=True, context=self.context).data
        return representation

    def get_likes(self, instance):
        return instance.likes.count()
    def get_downloads(self, instance):
        return instance.downloads.count()
    def get_watched(self, instance):
        return instance.watched.count()

    class Meta:
        model = Pack
        # fields = ['id', 'cat_id', 'user', 'is_private', 'pack_identifier', 'tag_name',
        #           'tray_image_filelink', 'tray_image_fileName', 'sticker_list_size', 'premium', 'avoid_cache',
        #           'animated_sticker_pack', 'is_approved', 'updatedAt', 'isNew',
        #           'publisher_name', 'publisher_email', 'publisher_website_zip', 'license_Agreement_Link',
        #           'privacy_policy', 'sticker_list', 'likes', 'watched', 'downloads', 'description']

        fields = ['id', 'cat_id', 'user', 'is_private','pack_status', 'pack_identifier', 'tag_name',
                  'tray_image_filelink', 'tray_image_fileName', 'sticker_list_size', 'premium', 'avoid_cache',
                  'animated_sticker_pack', 'is_approved', 'updatedAt', 'isNew',
                  'publisher_name', 'publisher_email', 'publisher_website_zip', 'license_Agreement_Link',
                  'privacy_policy', 'status', 'bannner_image', 'featured_image',
                  'sticker_list', 'likes', 'watched', 'downloads', 'description']





   



class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'user', 'pack', 'reason']




