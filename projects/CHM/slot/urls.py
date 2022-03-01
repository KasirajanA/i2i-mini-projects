from django.urls import path

from slot.views import add_slots, delete_slot, fetch_slots, update_slot

urlpatterns = [
    path('fetchcompanies', fetch_slots ),
    path('addcompanies/', add_slots ),
    path('deletecompany/<int:id>', delete_slot),
    path('updatecompany/<int:id>', update_slot)
]