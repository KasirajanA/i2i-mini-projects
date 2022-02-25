from django.urls import path

from tickets.views import add_ticket, delete_ticket, fetch_tickets


urlpatterns = [
    path('ticket/', add_ticket),
    path('displayticket/<int:customer_id>', fetch_tickets),
    path('cancelticket/<int:id>', delete_ticket),
]