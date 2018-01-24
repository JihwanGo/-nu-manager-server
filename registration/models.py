from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail.fields import ImageField


class User(AbstractUser):
    full_name = models.CharField(
        verbose_name='이름',
        max_length=50,
    )

    def __str__(self):
        return self.full_name

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '전체 사용자'


class Preschool(models.Model):
    REGIONS = [
        ('SE', '서울'),
        ('BS', '부산'),
        ('DG', '대구'),
        ('IC', '인천'),
        ('GJ', '광주'),
        ('DJ', '대전'),
        ('US', '울산'),
        ('SJ', '세종'),
        ('GG', '경기'),
        ('GW', '강원'),
        ('CB', '충북'),
        ('CN', '충남'),
        ('JB', '전북'),
        ('JN', '전남'),
        ('GB', '경북'),
        ('GN', '경남'),
        ('JJ', '제주'),
    ]

    name = models.CharField(
        verbose_name='이름',
        max_length=50,
    )
    region = models.CharField(
        verbose_name='지역',
        max_length=2,
        choices=REGIONS,
    )

    def __str__(self):
        return '{} ({})'.format(self.name, self.region)

    class Meta:
        verbose_name = '유치원'
        verbose_name_plural = '유치원'


class Class(models.Model):
    name = models.CharField(
        verbose_name='이름',
        max_length=20,
    )
    preschool = models.ForeignKey(
        to=Preschool,
        verbose_name='소속 유치원',
        related_name='classes',
    )

    def __str__(self):
        return self.preschool.name + ' ' + self.name

    def num_teachers(self):
        return self.teachers.count()

    num_teachers.short_description = '선생님의 수'

    def num_children(self):
        return self.children.count()

    num_children.short_description = '학생의 수'

    class Meta:
        verbose_name = '반'
        verbose_name_plural = '반'


class Teacher(User):
    assigned_class = models.ForeignKey(
        to=Class,
        verbose_name='반',
        related_name='teachers',
    )

    class Meta:
        verbose_name = '선생님'
        verbose_name_plural = '선생님'

    def preschool(self):
        return self.assigned_class.preschool

    preschool.short_description = '유치원'


class Child(models.Model):
    RELATIONSHIP_TYPES = [
        ('F', '아버지'),
        ('M', '어머니'),
        ('GF', '할아버지'),
        ('GM', '할머니'),
        ('O', '기타'),
    ]
    GENDER_OPTIONS = [
        ('M', '남'),
        ('F', '여'),
    ]

    name = models.CharField(
        verbose_name='이름',
        max_length=50,
    )
    gender = models.CharField(
        verbose_name='성별',
        max_length=1,
        choices=GENDER_OPTIONS,
    )
    assigned_class = models.ForeignKey(
        to=Class,
        verbose_name='반',
        related_name='children',
    )
    birthday = models.DateField()
    address = models.CharField(
        verbose_name='주소',
        max_length=100,
        blank=True,
        null=True,
    )

    parent_relationship = models.CharField(
        verbose_name='관계',
        max_length=2,
        choices=RELATIONSHIP_TYPES,
    )
    parent_phone_number = PhoneNumberField(
        verbose_name='휴대폰 번호',
    )
    profile_photo = ImageField(
        verbose_name='프로필 사진',
        upload_to='profiles',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = '학생'
        verbose_name_plural = '학생'

    def __str__(self):
        return self.name

# class Parent(User):
#     RELATIONSHIP_TYPES = [
#         ('F', '아버지'),
#         ('M', '어머니'),
#         ('GF', '할아버지'),
#         ('GM', '할머니'),
#         ('O', '기타'),
#     ]
#     children = models.ManyToManyField(
#         to=Child,
#         verbose_name='아이',
#         related_name='parents',
#     )
#     relationship = models.CharField(
#         verbose_name='관계',
#         max_length=2,
#         choices=RELATIONSHIP_TYPES,
#     )
#     phone_number = PhoneNumberField(
#         verbose_name='휴대폰 번호',
#     )
#
#     class Meta:
#         verbose_name = '학부모'
#         verbose_name_plural = '학부모'
