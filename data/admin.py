from django.contrib import admin

from .models import Curriculum, Course, Album, Photo, Announcement, Event


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'month',
        'week',
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'curriculum',
        'linked_class',
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'linked_class',
        'date',
        'course',
    )
    list_filter = (
        'linked_class',
    )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'album',
        'image',
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'linked_class',
        'date',
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'linked_class',
        'date',
    )
