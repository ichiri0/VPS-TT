from django.urls import path
from .views import VPSListCreateView, VPSDetailView

urlpatterns = [
    path("vps/", VPSListCreateView.as_view(), name="vps-list-create"),
    path("vps/<uuid:uid>/", VPSDetailView.as_view(), name="vps-detail"),
]
