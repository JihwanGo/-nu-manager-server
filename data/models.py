from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from sorl.thumbnail.fields import ImageField

from registration.models import Class, Child


class Curriculum(models.Model):
    title = models.CharField(
        max_length=100,
    )
    month = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
    )
    week = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '교과 과정'
        verbose_name_plural = '교과 과정'


class Course(models.Model):
    curriculum = models.ForeignKey(
        to=Curriculum,
        verbose_name='교과 과정',
    )
    linked_class = models.ForeignKey(
        to=Class,
        verbose_name='학급',
        related_name='courses',
    )
    done = models.BooleanField(
        verbose_name='진행 여부',
        default=False,
    )

    class Meta:
        verbose_name = '수업'
        verbose_name_plural = '수업'

    def __str__(self):
        return '{} ({})'.format(self.curriculum.title, self.linked_class.name)

    def title(self):
        return self.curriculum.title


class Album(models.Model):
    title = models.CharField(
        verbose_name='제목',
        max_length=100,
    )
    linked_class = models.ForeignKey(
        to=Class,
        verbose_name='반',
        related_name='albums',
    )
    date = models.DateField(
        verbose_name='생성 날짜',
        auto_now_add=True,
    )
    course = models.ForeignKey(
        to=Course,
        verbose_name='수업',
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{} ({})'.format(self.title, self.linked_class.name)

    class Meta:
        verbose_name = '앨범'
        verbose_name_plural = '앨범'


class Photo(models.Model):
    album = models.ForeignKey(
        to=Album,
        on_delete=models.CASCADE,
        verbose_name='앨범',
        related_name='photos',
    )
    tagged_children = models.ManyToManyField(
        to=Child,
        verbose_name='학생',
        related_name='photos',
        blank=True,
    )
    image = ImageField(
        verbose_name='사진 경로',
        upload_to='photos',
    )

    class Meta:
        verbose_name = '사진'
        verbose_name_plural = '사진'


class AbstractMessage(models.Model):
    date = models.DateField(
        verbose_name='날짜',
        auto_created=True,
    )
    title = models.CharField(
        verbose_name='제목',
        max_length=100,
    )
    content = models.TextField(
        verbose_name='내용',
    )

    class Meta:
        abstract = True


class Announcement(AbstractMessage):
    linked_class = models.ForeignKey(
        to=Class,
        verbose_name='반',
        related_name='announcements',
    )


class Event(AbstractMessage):
    linked_class = models.ForeignKey(
        to=Class,
        verbose_name='반',
        related_name='events',
    )
