from django.urls import path

from shows.views import add_show, add_show_category, delete_show, delete_show_category, fetch_available_shows, fetch_show_category, fetch_shows, update_show, update_show_category


urlpatterns = [
    path('addshow/', add_show),
    path('displayshow', fetch_shows),
    path('deleteshow/<int:id>', delete_show),
    path('updateshow/<int:id>', update_show),
    path('addshowcategory/', add_show_category),
    path('displayshowcategory', fetch_show_category),
    path('deleteshowcategory/<int:id>', delete_show_category),
    path('updateshowcategory/<int:id>', update_show_category),
    path('booking/<int:customer_id>', fetch_available_shows)
]