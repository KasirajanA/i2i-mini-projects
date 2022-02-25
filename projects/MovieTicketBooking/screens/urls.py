from django.urls import path

from screens.views import add_screen, delete_screen, fetch_screens, update_screen


urlpatterns = [
    path('addscreen/', add_screen),
    path('displayscreens', fetch_screens),
    path('deletescreen/<int:id>', delete_screen),
    path('updatescreen/<int:id>', update_screen),
]