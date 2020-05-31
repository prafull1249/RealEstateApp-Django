from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from listings.choices import *
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = { 'listings': listings}
    return render(request, 'pages/index.html', context)

def about(request):
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    realtors = Realtor.objects.all
    
    return render(request, 'pages/about.html', {"mvp_realtor": mvp_realtor, "realtors": realtors})

def search(request):

    listings = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)
    
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__icontains=city)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    context = {
        'price_choices' : price_choices,
        'bedroom_choices' : bedroom_choices,
        'state_choices' : state_choices,
        'listings' : listings,
        'values' : request.GET
    }
    return render(request, 'pages/search.html', context)