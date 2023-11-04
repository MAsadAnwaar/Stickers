from rest_framework import viewsets
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.db.models import Q
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth import authenticate
from rest_framework.response import Response 
from rest_framework.views import APIView

from rest_framework import filters,views
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.response import Response


# Create your views here.
from django.conf import settings
from urllib.parse import urljoin
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


from rest_framework import permissions
from django.contrib.auth import login
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


 

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pack

from knox.auth import TokenAuthentication

class AddLikeToPack(APIView):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, pack_id):
        pack = get_object_or_404(Pack, pk=pack_id)
        user = request.user

        if pack.likes.filter(id=user.id).exists():
            # User has already liked the pack, remove the like
            pack.likes.remove(user)
            return Response({'message': 'Like removed.'}, status=status.HTTP_200_OK)
        else:
            # User has not liked the pack, add the like
            pack.likes.add(user)
            return Response({'message': 'Like added.'}, status=status.HTTP_200_OK)

class PackDetailView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pack_id):
        pack = get_object_or_404(Pack, pk=pack_id)
        user = request.user

        # Check if the user has already downloads the pack
        if pack.downloads.filter(id=user.id).exists():
            return Response({'message': 'You have already downloads this pack.'}, status=status.HTTP_200_OK)
        else:
            # User has not downloads the pack, add the watch and increment the downloads count
            pack.downloads.add(user)
            pack.save()
            return Response({'message': 'Pack details retrieved and downloads.'}, status=status.HTTP_200_OK)




from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Category, Pack
from .serializers import Category_Serializer, PackSerializer

# class catListAPIView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = Category_Serializer
class catListAPIView(generics.ListAPIView):
    serializer_class = Category_Serializer

    def get_queryset(self):
        # excluded_categories = ["Religion"]
        excluded_categories = ["Events", "Religion"]
        return Category.objects.exclude(catname__in=excluded_categories)
# class CategoryDetailsAPIView(generics.RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = Category_Serializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)

#         packs = Pack.objects.filter(cat_id=instance).exclude(pack_status=0)
#         packs_serializer = PackSerializer(packs, many=True, context={'request': request})

#         data = serializer.data
#         data['packs'] = packs_serializer.data

#         return Response(data)

import random
class CategoryDetailsAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # You can filter packs by id here
        packs = Pack.objects.filter(cat_id=instance, id__gte=0)  # Change id__gte to filter by a different criterion

        # Exclude packs with pack_status=0
        packs = packs.exclude(pack_status=0)

        # Shuffle the list of packs
        packs = list(packs)
        random.shuffle(packs)

        packs_serializer = PackSerializer(packs, many=True, context={'request': request})

        data = serializer.data
        data['packs'] = packs_serializer.data

        return Response(data)
class PackDetailsAPIView(generics.RetrieveAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'pack_pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # user = request.user

        # # Check if the user has already watched the pack
        # if instance.watched.filter(id=user.id).exists():
        #     return super().retrieve(request, *args, **kwargs)
        # else:
        #     # User has not watched the pack, add the watch
        #     instance.watched.add(user)
        #     instance.save()

        return super().retrieve(request, *args, **kwargs)


    

# class packListAPIView(APIView):
#     def get(self, request):
#         packs = Pack.objects.all()
#         serializer = PackSerializer(packs, many=True, context={'request': request})
#         data = serializer.data

#         # Add full file/image URLs to the response
#         for pack_data in data:
#             # Add full URL for tray_image_filelink
#             tray_image_filelink = pack_data.get('tray_image_filelink')
#             if tray_image_filelink:
#                 pack_data['tray_image_filelink'] = request.build_absolute_uri(tray_image_filelink)

#             # Add full URLs for sticker_list
#             sticker_list = pack_data.get('sticker_list', [])
#             for sticker_data in sticker_list:
#                 sticker_file = sticker_data.get('sticker')
#                 if sticker_file:
#                     sticker_data['sticker'] = request.build_absolute_uri(sticker_file)

#             # Add full URL for publisher_website_zip
#             publisher_website_zip = pack_data.get('publisher_website_zip')
#             if publisher_website_zip:
#                 publisher_website_zip = urljoin(settings.MEDIA_URL, publisher_website_zip)
#                 pack_data['publisher_website_zip'] = request.build_absolute_uri(publisher_website_zip)

#         return Response(data)
#         # return Response({'Pack': data})
# class packListAPIView(generics.ListAPIView):
#     # queryset = Pack.objects.all()
#     # serializer_class = PackSerializer

#     serializer_class = PackSerializer

#     def get_queryset(self):
#         return Pack.objects.all()

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'packs': serializer.data})  
# class packListAPIView(generics.ListAPIView):
#     serializer_class = PackSerializer

#     def get_queryset(self):
#         # Filter packs where pack_status is not equal to 0
#         return Pack.objects.exclude(pack_status=0)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'packs': serializer.data})
from django.core.cache import cache  # Import the cache module
from rest_framework import generics
from rest_framework.response import Response

class packListAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        # Filter packs where pack_status is not equal to 0
        return Pack.objects.exclude(pack_status=0)

    def list(self, request, *args, **kwargs):
        cache_key = 'pack_list_cache'  # Define a unique cache key
        cached_data = cache.get(cache_key)  # Attempt to retrieve data from the cache

        if not cached_data:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = {'packs': serializer.data}

            # Cache the data for a day (24 hours)
            cache.set(cache_key, data, 60 * 60 * 24)

            return Response(data)
        else:
            return Response(cached_data)
      
class TrendingListAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        return Pack.objects.filter(status=1).exclude(pack_status=0)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'packs': serializer.data})

class EmojiListAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        return Pack.objects.filter(cat_id=29)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'packs': serializer.data})


class FeaturedListAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        return Pack.objects.filter(status=2).exclude(pack_status=0)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'packs': serializer.data})
        
class FestiveListAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        return Pack.objects.filter(status=3).exclude(pack_status=0)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'packs': serializer.data})

class AnimatedListAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        return Pack.objects.filter(animated_sticker_pack=True).exclude(pack_status=0)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'packs': serializer.data})

# from django.db.models import Sum

# class UserListAPIView(generics.ListAPIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     serializer_class = PackSerializer

#     def get_queryset(self):
#         user = self.request.user
#         return Pack.objects.filter(user=user)

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)

#         total_likes = Pack.objects.filter(user=request.user).aggregate(total_likes=Sum('likes')).get('total_likes')

#         response_data = {
#             'packs': serializer.data,
#             'total_pack_count': queryset.count(),
#             'total_likes': total_likes if total_likes else 0
#         }

#         return Response(response_data)
        
from django.db.models import Sum
from django.db.models import Count

class UserListAPIView(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PackSerializer

    def get_queryset(self):
        user = self.request.user
        return Pack.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        total_likes = Pack.objects.filter(user=request.user).aggregate(total_likes=Sum('likes')).get('total_likes')
        total_watched = queryset.aggregate(total_watched=Count('watched')).get('total_watched')
        total_downloads = queryset.aggregate(total_downloads=Count('downloads')).get('total_downloads')

        response_data = {
            'packs': serializer.data,
            'total_pack_count': queryset.count(),
            'total_likes': total_likes if total_likes else 0,
            'total_watched': total_watched if total_watched else 0,
            'total_downloads': total_downloads if total_downloads else 0
        }

        return Response(response_data)
        
class Usercreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny ,)



# class packListAPIView(generics.ListAPIView):
#     # queryset = Pack.objects.all()
#     # serializer_class = PackSerializer

#     serializer_class = PackSerializer

#     def get_queryset(self):
#         return Pack.objects.all()

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response({'packs': serializer.data})





class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['reason',]
    
    def create(self, request, *args, **kwargs):
        pack = request.data.get('pack')
        user = request.data.get('user')
        if Report.objects.filter(pack=pack, user=user).exists():
            return Response({"error": "You have already reported this pack."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

from .forms import StickerListForm

from django.views import View
# views.py

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import StickerListForm

def upload_sticker_list(request, pack_id):
    pack = Pack.objects.get(id=pack_id)

    if request.method == 'POST':
        form = StickerListForm(request.POST, request.FILES)
        if form.is_valid():
            # Save each selected image as a StickerList instance
            for sticker_file in request.FILES.getlist('sticker'):
                StickerList.objects.create(pack=pack, sticker=sticker_file)
            
            messages.success(request, 'StickerList images uploaded successfully.')
            return render(request, 'upload.html', {'form': form, 'pack': pack})
        else:
            messages.error(request, 'Error uploading StickerList images. Please try again.')
    else:
        form = StickerListForm()

    return render(request, 'upload.html', {'form': form, 'pack': pack})



class CountrytagDetailsAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']

        # Filter the Pack objects based on the tag_name in countrytag and religiontag
        packs_with_countrytag = Pack.objects.filter(countrytag__countrytag=tag_name)
        # packs_with_religiontag = Pack.objects.filter(religiontag__religiontag=tag_name)

        # Combine the two querysets to get unique packs with the specified tag_name
        # queryset = (packs_with_countrytag | packs_with_religiontag).distinct()
        queryset = (packs_with_countrytag).distinct()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'packs': serializer.data})
    

class ReligiontagDetailsAPIView(generics.ListAPIView):
    serializer_class = PackSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']

        # Filter the Pack objects based on the tag_name in countrytag and religiontag
        # packs_with_countrytag = Pack.objects.filter(countrytag__countrytag=tag_name)
        packs_with_religiontag = Pack.objects.filter(religiontag__religiontag=tag_name)

        # Combine the two querysets to get unique packs with the specified tag_name
        # queryset = (packs_with_countrytag | packs_with_religiontag).distinct()
        queryset = (packs_with_religiontag).distinct()

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'packs': serializer.data})



class CountrytagListAPIView(generics.ListAPIView):
    queryset = countrytag.objects.all()
    serializer_class = Countrytag_Serializer

class ReligiontagListAPIView(generics.ListAPIView):
    queryset = religiontag.objects.all()
    serializer_class = Religiontag_Serializer