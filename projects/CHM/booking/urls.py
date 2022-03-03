from django.urls import path

from booking.views import add_booking, cancel_booking, get_bookings, get_bookings_by_employee_id


urlpatterns = [
    path('getemployeebooking/<int:id>', get_bookings_by_employee_id),
    path('getbookings', get_bookings),
    path('cancelbooking/<int:id>', cancel_booking),
    path('addbooking/', add_booking)
]
