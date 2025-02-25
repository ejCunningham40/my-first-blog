from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path(
        "favicon.ico", RedirectView.as_view(url="/static/favicon.ico", permanent=True)
    ),
]
