from rest_framework.permissions import BasePermission


class CurrentUser(BasePermission):
    """
    仅当前用户可以访问
    """

    def has_permission(self, request, view):
        return str(request.user.uid) == view.kwargs.get('pk', list(view.kwargs.values())[0])
