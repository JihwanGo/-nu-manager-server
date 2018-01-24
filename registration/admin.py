from django.contrib import admin

from .models import Preschool, Class, User, Teacher, Child


@admin.register(Preschool)
class PreschoolAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'region',
    )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'num_teachers',
        'num_children',
    )


class PreschoolListFilter(admin.SimpleListFilter):
    title = '유치원'
    parameter_name = 'preschool'

    def lookups(self, request, model_admin):
        preschools = Preschool.objects.all()
        return [(preschool.id, preschool.name) for preschool in preschools]

    def queryset(self, request, queryset):
        preschool_id = self.value()
        if preschool_id:
            return queryset.filter(assigned_class__preschool__id=preschool_id)
        else:
            return queryset


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'assigned_class',
    )
    list_filter = (
        PreschoolListFilter,
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'full_name',
    )


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'assigned_class',
    )
    list_filter = (
        PreschoolListFilter,
    )


# @admin.register(Parent)
# class ParentAdmin(admin.ModelAdmin):
#     list_display = (
#         'full_name',
#         'child',
#         'relationship',
#     )
