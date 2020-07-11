from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Itinerary
from .forms import ItineraryForm

@login_required
def itineraries(request):
    return render(request, 'itinerary/itineraries.html')


@login_required
def itinerary(request , itinerary_id):
    return render(request, 'itinerary/itinerary.html')


@login_required
def itinerary_add(request, inquiry_id):
    canAdd = ''
    itineraries = request.user.itineraries.all().count()
    if itineraries >= 50 and request.user.userprofile.plan == 'basic':
        canAdd = 'You can\'t have more than 50 itineraries when you\'re on basic'

    if request.method == 'POST':
        form = ItineraryForm(request.POST)

        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.created_by = request.user
            itinerary.inquiry_id = inquiry_id
            itinerary.save()
            messages.success(request, 'The itinerary was added!!')
            return redirect('inquiry', inquiry_id=inquiry_id)
    else:
        form = ItineraryForm()

    context = {
        'form': form,
        'canAdd': canAdd
    }
    return render(request, 'itinerary/itinerary_add.html', context)


@login_required
def itinerary_edit(request, inquiry_id, itinerary_id):
    itinerary = Itinerary.objects.filter(created_by=request.user).get(pk=itinerary_id)

    if request.method == 'POST':
        form = ItineraryForm(request.POST, instance=itinerary)

        if form.is_valid():
            form.save()
            messages.success(request, 'The itinerary was edited!!')
            return redirect('inquiry', inquiry_id=inquiry_id)
    else:
        form = ItineraryForm(instance=itinerary)

    context = {
        'form': form,
        'itinerary': itinerary
    }

    return render(request, 'itinerary/itinerary_edit.html', context)


@login_required
def itinerary_delete(request, inquiry_id, itinerary_id):
    itinerary = Itinerary.objects.filter(created_by=request.user).get(pk=itinerary_id)
    itinerary.delete()
    messages.success(request, 'The itinerary was deleted!!')
    return redirect('inquiry', inquiry_id=inquiry_id)
