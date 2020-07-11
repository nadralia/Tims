from django.urls import path

from .views import itineraries, itinerary, itinerary_add, itinerary_edit, itinerary_delete

from .api import api_delete_itinerary,api_increase_visits

urlpatterns = [
    path('itineraries', itineraries, name='itineraries'),
    path('inquiries/<int:inquiry_id>/add_itinerary/', itinerary_add, name='itinerary_add'),
    path('inquiries/<int:inquiry_id>/edit_itinerary/<int:itinerary_id>/', itinerary_edit, name='itinerary_edit'),
    path('inquiries/<int:inquiry_id>/delete_itinerary/<int:itinerary_id>/', itinerary_delete, name='itinerary_delete'),
    
    path('api/delete_itinerary/<int:itinerary_id>/', api_delete_itinerary, name='api_delete_itinerary'),
    path('api/increase_visits/<int:itinerary_id>/', api_increase_visits, name='api_increase_visits'),
]