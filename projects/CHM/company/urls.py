from django.urls import path

from company.views import add_company, delete_company, fetch_companies, update_company

urlpatterns = [
    path('fetchcompanies', fetch_companies ),
    path('addcompanies/', add_company ),
    path('deletecompany/<int:id>', delete_company),
    path('updatecompany/<int:id>', update_company)
]

 