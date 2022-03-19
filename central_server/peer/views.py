from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)
from .models import Peer, Member

class PeerListView(ListView):
    model = Peer
    queryset = Peer.objects.exclude(p_no=1).order_by("-date_created")

class PeerDetailView(DetailView):
    model = Peer

class PeerCreateView(SuccessMessageMixin, CreateView):
    model = Peer
    fields = ["p_title", 'p_key', 'p_ip', 'member']
    success_url = reverse_lazy("peer-list")
    success_message = "Your new peer was created!"

class PeerDeleteView(SuccessMessageMixin, DeleteView):
    model = Peer
    success_url = reverse_lazy("peer-list")
    success_message = "Your peer was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

class PeerLoginView(SuccessMessageMixin, CreateView):
    model = Member
    fields = ["m_id", 'm_pw']
    success_url = reverse_lazy("peer-list")
    success_message = "Login success!"
    error_message = "Login failed!"
    def login(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        messages.error(self.request, self.error_message)
        return super().login(request, *args, **kwargs)
