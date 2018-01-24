from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.generics import \
    ListAPIView, \
    ListCreateAPIView, \
    RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import Class, Teacher
from .serializers import ChildSerializer, ClassSerializer


def find_class(self):
    class_id = self.kwargs.get('class_id')
    selected_class = get_object_or_404(Class, id=class_id)
    teacher = get_object_or_404(Teacher, username=self.request.user.username)
    if selected_class not in teacher.assigned_class.preschool.classes.all():
        raise NotFound
    return selected_class


class ClassList(ListAPIView):
    serializer_class = ClassSerializer

    def get_queryset(self):
        teacher = get_object_or_404(Teacher, username=self.request.user.username)
        return teacher.assigned_class.preschool.classes


class ClassDetail(RetrieveAPIView):
    serializer_class = ClassSerializer

    def get_object(self):
        selected_class = find_class(self)
        return selected_class


class ChildList(ListCreateAPIView):
    serializer_class = ChildSerializer

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.children


class ChildDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ChildSerializer
    lookup_field = 'id'

    def get_queryset(self):
        selected_class = find_class(self)
        return selected_class.children
