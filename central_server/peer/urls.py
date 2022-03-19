
from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.PeerListView.as_view(),
        name="peer-list"
    ),
    path(
        "peer/<int:pk>",
        views.PeerDetailView.as_view(),
        name="peer-detail"
    ),

    path(
        "create",
        views.PeerCreateView.as_view(),
        name="peer-create"
    ),
    path(
        "peer/<int:pk>/delete",
        views.PeerDeleteView.as_view(),
        name="peer-delete",
    ),
    path(
        "login",
        views.PeerLoginView.as_view(),
        name="login"
    ),
]
