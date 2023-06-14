from django.urls import path, include
from .views import *

app_name = 'home'


urlpatterns = [
    # swagger private UI
    path('role/', include([
        path('', RoleListCreateAPIView.as_view(), name="role_list"),

    ])),
    path('user/', include([
        path('', UserListCreateAPIView.as_view(), name="user_list"),

    ])),
]