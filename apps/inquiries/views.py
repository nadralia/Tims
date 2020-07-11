from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Inquiry
from .forms import InquiryForm


@login_required
def inquiries(request):
    inquiries = request.user.inquiries.all()

    context = {
        'inquiries': inquiries
    }
    return render(request, 'inquiries/inquiries.html', context)


@login_required
def inquiry(request , inquiry_id):
    inquiry = Inquiry.objects.get(pk=inquiry_id)

    itinerariesstring= ''
    for itinerary in inquiry.itineraries.all():
        editurl = reverse('itinerary_edit', args=[inquiry.id, itinerary.id])
        b = "{'id':'%s', 'itineraryname': '%s', 'numberadults':'%s', 'numberchildren':'%s', 'editurl':'%s', 'visits':'%s'}," % (itinerary.id, itinerary.itineraryname,itinerary.numberadults,itinerary.numberchildren,editurl,itinerary.visits)

        itinerariesstring = itinerariesstring + b

    context = {
        'inquiry': inquiry,
        'itinerariesstring': itinerariesstring
    }
    return render(request, 'inquiries/inquiry.html', context)


@login_required
def inquiry_add(request):
    canAdd = ''

    inquiries = request.user.inquiries.all().count()

    if inquiries >= 50 and request.user.userprofile.plan == 'pro':
        canAdd = 'You can\'t have more than 50 inquiries when you\'re on pro'
    
    if inquiries >= 5 and request.user.userprofile.plan == 'basic':
        canAdd = 'You can\'t have more than 5 inquiries when you\'re on basic'

    if request.method == 'POST':
        form = InquiryForm(request.POST)

        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.created_by = request.user
            inquiry.save()
            messages.success(request, 'The inquiry was added!!')

            return redirect('inquiries')
    else:
        form = InquiryForm()

    context = {
        'form': form,
        'canAdd': canAdd
    }

    return render(request, 'inquiries/inquiry_add.html', context)


@login_required
def inquiry_edit(request, inquiry_id):
    inquiry = Inquiry.objects.filter(created_by=request.user).get(pk=inquiry_id)

    if request.method == 'POST':
        form = InquiryForm(request.POST, instance=inquiry)

        if form.is_valid():
            inquiry.save()
            messages.success(request, 'The inquiry has been edited!!')
            return redirect('inquiries')
    else:
        form = InquiryForm(instance=inquiry)

    context = {
        'form': form,
        'inquiry': inquiry
    }

    return render(request, 'inquiries/inquiry_edit.html', context)


@login_required
def inquiry_delete(request, inquiry_id):
    inquiry = Inquiry.objects.filter(created_by=request.user).get(pk=inquiry_id)

    inquiry.delete()

    messages.success(request, 'The inquiry was deleted !!')
    return redirect('inquiries')
