from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    message = "您不是这个评论的作者"

    def safe_methods_or_author(self, request, func):
        if request.method in SAFE_METHODS:
            return True
        return func()

    def has_permission(self, request, view):
        return self.safe_methods_or_author(
            request, lambda: request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return self.safe_methods_or_author(request,
                                           lambda: request.user == obj.author)
