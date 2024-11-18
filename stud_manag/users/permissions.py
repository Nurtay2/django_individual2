from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    """Allows access only to students"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'


class IsTeacher(BasePermission):
    """Allows access only to teachers"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'teacher'


class IsAdmin(BasePermission):
    """Allows access only to admins"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsStudentOrAdmin(BasePermission):
    """Allows access to students and admins"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'student' or request.user.role == 'admin'
        )


class IsTeacherOrAdmin(BasePermission):
    """Allows access to teachers and admins"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'teacher' or request.user.role == 'admin'
        )
