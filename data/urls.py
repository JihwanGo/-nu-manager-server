from django.conf.urls import url

from registration.views import ChildList, ChildDetail, ClassList, ClassDetail
from .views import \
    CourseList, \
    CourseUpdate, \
    AlbumList, \
    AlbumDetail, \
    PhotoCreate, \
    PhotoUpdate, \
    AnnouncementList, \
    AnnouncementDetail, \
    EventList, \
    EventDetail

urlpatterns = [
    url(r'^$', ClassList.as_view()),
    url(r'^(?P<class_id>\d+)/$', ClassDetail.as_view()),
    url(r'^(?P<class_id>\d+)/children/$', ChildList.as_view()),
    url(r'^(?P<class_id>\d+)/children/(?P<id>\d+)/$', ChildDetail.as_view()),
    url(r'^(?P<class_id>\d+)/courses/$', CourseList.as_view()),
    url(r'^(?P<class_id>\d+)/courses/(?P<id>\d+)/$', CourseUpdate.as_view()),
    url(r'^(?P<class_id>\d+)/albums/$', AlbumList.as_view()),
    url(r'^(?P<class_id>\d+)/albums/(?P<id>\d+)/$', AlbumDetail.as_view()),
    url(r'^(?P<class_id>\d+)/photos/$', PhotoCreate.as_view()),
    url(r'^(?P<class_id>\d+)/photos/(?P<id>\d+)/$', PhotoUpdate.as_view()),
    url(r'^(?P<class_id>\d+)/announcements/$', AnnouncementList.as_view()),
    url(r'^(?P<class_id>\d+)/announcements/(?P<id>\d+)/$', AnnouncementDetail.as_view()),
    url(r'^(?P<class_id>\d+)/events/$', EventList.as_view()),
    url(r'^(?P<class_id>\d+)/events/(?P<id>\d+)/$', EventDetail.as_view()),
]
