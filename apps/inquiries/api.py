from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Inquiry

@csrf_exempt
def api_delete_inquiry(request, inquiry_id):
    inquiry = request.user.inquiries.all().get(pk=inquiry_id)
    inquiry.delete()

    return JsonResponse({'success': True})
