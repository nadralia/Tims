from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Itinerary

@csrf_exempt
def api_delete_itinerary(request, itinerary_id):
    itinerary = request.user.itineraries.all().get(pk=itinerary_id)
    itinerary.delete()

    return JsonResponse({'success': True})


@csrf_exempt
def api_increase_visits(request, itinerary_id):
    itinerary = request.user.itineraries.all().get(pk=itinerary_id)
    itinerary.visits = itinerary.visits + 1
    itinerary.save()

    return JsonResponse({'success': True})   

