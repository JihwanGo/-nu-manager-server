from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Preschool, Class, User, Teacher, Child


class PreschoolSerializer(ModelSerializer):
    class Meta:
        model = Preschool
        fields = (
            'id',
            'name',
        )


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User(
            full_name=validated_data['name'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class TeacherSerializer(UserSerializer):
    class_id = serializers.IntegerField(source='assigned_class.id')

    class Meta:
        model = Teacher
        fields = (
            'full_name',
        )


class ChildSerializer(ModelSerializer):
    assigned_class = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all()
    )
    profile_thumbnail = HyperlinkedSorlImageField(
        '128x128',
        options={'crop': 'center'},
        source='profile_photo',
        read_only=True
    )

    class Meta:
        model = Child
        fields = (
            'id',
            'assigned_class',
            'name',
            'gender',
            'birthday',
            'address',
            'parent_relationship',
            'parent_phone_number',
            'profile_photo',
            'profile_thumbnail',
        )
        read_only_fields = (
            'id',
        )


class ClassSerializer(ModelSerializer):
    preschool_name = serializers.CharField(source='preschool.name')
    class_name = serializers.CharField(source='name')

    class Meta:
        model = Class
        fields = (
            'id',
            'preschool_name',
            'class_name',
        )

# class ParentSerializer(UserSerializer):
#     class Meta:
#         model = Parent
#         fields = (
#             'full_name',
#             'relationship',
#             'phone_number',
#         )
