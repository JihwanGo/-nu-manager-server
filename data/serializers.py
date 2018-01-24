from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from registration.models import Child, Class
from .models import Curriculum, Course, Album, Photo, Announcement, Event


class CurriculumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = (
            'title',
            'month',
            'week',
        )


class CourseSerializer(HyperlinkedModelSerializer):
    title = serializers.CharField(
        source='curriculum.title',
        read_only=True,
    )
    month = serializers.IntegerField(
        source='curriculum.month',
        read_only=True,
    )
    week = serializers.IntegerField(
        source='curriculum.week',
        read_only=True,
    )

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'month',
            'week',
            'done',
        )
        read_only_fields = (
            'id',
        )


class PhotoSerializerForCreate(HyperlinkedModelSerializer):
    album = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(),
    )
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={'crop': 'center'},
        source='image',
        read_only=True
    )

    class Meta:
        model = Photo
        fields = (
            'id',
            'album',
            'image',
            'thumbnail',
        )
        read_only_fields = (
            'id',
        )

    def create(self, validated_data):
        photo = Photo.objects.create(
            album=validated_data['album'],
            image=validated_data['image'],
        )
        photo.save()
        return photo


class PhotoSerializerForUpdate(HyperlinkedModelSerializer):
    tagged_children = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Child.objects.all(),
    )

    class Meta:
        model = Photo
        fields = (
            'tagged_children',
        )


class PhotoSerializer(HyperlinkedModelSerializer):
    tagged_children = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Child.objects.all(),
    )
    thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={'crop': 'center'},
        source='image',
        read_only=True
    )

    class Meta:
        model = Photo
        fields = (
            'id',
            'tagged_children',
            'image',
            'thumbnail',
        )
        read_only_fields = (
            'id',
            'image',
        )


class AlbumSerializer(HyperlinkedModelSerializer):
    linked_class = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all()
    )
    course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        allow_null=True,
    )
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Album
        fields = (
            'id',
            'linked_class',
            'title',
            'course',
            'photos',
        )
        read_only_fields = (
            'id',
        )


class AnnouncementSerializer(HyperlinkedModelSerializer):
    linked_class = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all()
    )

    class Meta:
        model = Announcement
        fields = (
            'id',
            'linked_class',
            'date',
            'title',
            'content',
        )
        read_only_fields = (
            'id',
        )


class EventSerializer(HyperlinkedModelSerializer):
    linked_class = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all()
    )

    class Meta:
        model = Event
        fields = (
            'id',
            'linked_class',
            'date',
            'title',
            'content',
        )
        read_only_fields = (
            'id',
        )
