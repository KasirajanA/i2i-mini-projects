from django.urls import path

from seats.views import add_seat, delete_seat, fetch_available_seats, fetch_seats, update_seat


urlpatterns = [
    path('addseat/', add_seat),
    path('displayseats', fetch_seats),
    path('deleteseat/<int:id>', delete_seat),
    path('updateseat/<int:id>', update_seat),
    path('bookingseats/<int:show_id>/<int:customer_id>', fetch_available_seats)
]