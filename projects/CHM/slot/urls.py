from django.urls import path

from slot.views import add_slots, delete_slot, fetch_slots, update_slot

urlpatterns = [
    path('fetchslots', fetch_slots ),
    path('addslots/', add_slots ),
    path('deleteslot/<int:id>', delete_slot),
    path('updateslot/<int:id>', update_slot)
]