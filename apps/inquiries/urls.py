from django.urls import path

from .views import inquiries, inquiry, inquiry_add, inquiry_edit, inquiry_delete

from .api import api_delete_inquiry

urlpatterns = [
    path('inquiries', inquiries, name='inquiries'),
    path('inquiries/add/', inquiry_add, name='inquiry_add'),
    path('inquiries/<int:inquiry_id>', inquiry, name='inquiry'),
    path('inquiries/<int:inquiry_id>/edit/', inquiry_edit, name='inquiry_edit'),
    path('inquiries/<int:inquiry_id>/delete/', inquiry_delete, name='inquiry_delete'),

    path('api/delete_inquiry/<int:inquiry_id>/', api_delete_inquiry, name='api_delete_inquiry'),
]