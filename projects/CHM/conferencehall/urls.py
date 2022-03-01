from django.urls import path

from conferencehall.views import  add_conference_hall, delete_conference_hall, fetch_conference_halls, update_conference_hall

urlpatterns = [
    path('fetchconferencehalls', fetch_conference_halls ),
    path('addconferencehalls/', add_conference_hall ),
    path('deleteconferencehalls/<int:id>', delete_conference_hall),
    path('updateconferencehalls/<int:id>', update_conference_hall)
]
