from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.generics import \
    ListAPIView, \
    CreateAPIView, \
    ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, \
    UpdateAPIView

from registration.models import Class, Teacher
from .models import Photo
from .serializers import \
    CourseSerializer, \
    AlbumSerializer, \
    PhotoSerializerForCreate, \
    PhotoSerializerForUpdate, \
    AnnouncementSerializer, \
    EventSerializer


def find_class(self):
    class_id = self.kwargs.get('class_id')
    selected_class = get_object_or_404(Class, id=class_id)
    teacher = get_object_or_404(Teacher, username=self.request.user.username)
    if selected_class not in teacher.assigned_class.preschool.classes.all():
        raise NotFound
    return selected_class


class CourseList(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.courses


class CourseUpdate(UpdateAPIView):
    serializer_class = CourseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.courses


class AlbumList(ListCreateAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.albums.order_by('date')


class AlbumDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    lookup_field = 'id'

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.albums


class PhotoCreate(CreateAPIView):
    serializer_class = PhotoSerializerForCreate

    def get_queryset(self):
        selected_class = find_class(self)
        return Photo.objects.filter(album__linked_class=selected_class)


class PhotoUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializerForUpdate
    lookup_field = 'id'

    def get_queryset(self):
        selected_class = find_class(self)
        return Photo.objects.filter(album__linked_class=selected_class)


class AnnouncementList(ListCreateAPIView):
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.announcements.order_by('-date')


class AnnouncementDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = AnnouncementSerializer
    lookup_field = 'id'

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.announcements


class EventList(ListCreateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.events.order_by('date')


class EventDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    lookup_field = 'id'

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.events
