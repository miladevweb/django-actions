from typing import Any
from django.db import models
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import User
from apps.pyrebase import storage
from django.shortcuts import get_object_or_404

class HomeView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        print(users)
        user_data = [
            {
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'thumbnail_url': user.thumbnail.url,
            }
            for user in users
        ]
        return JsonResponse(user_data, safe=False)
    
class UsersView(ListView):
    model = User
    ordering = ('id',)

class CreateUserView(CreateView):
    model = User
    fields = ('username', 'email', 'first_name', 'thumbnail', 'password', 'last_name',)

    def form_valid(self, form):
        filename = f"thumbnails/user/{self.request.user.username}/{form.cleaned_data['thumbnail'].name}"
        storage.child(filename).put(form.cleaned_data['thumbnail'], 'idToken')
        url = storage.child(filename).get_url('idToken')
        
        form.instance.thumbnail = url
        self.object = form.save()
        return super().form_valid(form)
    
class UpdateUserView(UpdateView):
    model = User
    fields = ('username', 'email', 'first_name', 'thumbnail', 'password', 'last_name',)
    template_name = 'user/update_user.html'

    def get_object(self):
        self.request.user = get_object_or_404(User, pk=self.kwargs['pk'])
        return super().get_object()

    def form_valid(self, form):
        if form.cleaned_data['thumbnail'] == None:
            form.instance.thumbnail_url = self.request.user.thumbnail_url
            form.save()
            return super().form_valid(form)
        else:
            filename = f"thumbnails/user/{self.request.user.username}/{form.cleaned_data['thumbnail'].name}"
            storage.child(filename).put(form.cleaned_data['thumbnail'], 'idToken')
            url = storage.child(filename).get_url('idToken')
            
            form.instance.thumbnail = url
            self.object = form.save()
            return super().form_valid(form)

