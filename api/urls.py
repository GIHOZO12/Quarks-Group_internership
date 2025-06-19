from django.urls import path
from api.views import CreateUserView,GetUserView

urlpatterns=[
    path("users_view/",CreateUserView.as_view(),name="users_view"),
    path("get_user/<str:user_id>/",GetUserView.as_view(),name="get_user")
]