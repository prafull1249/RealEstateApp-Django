from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 2)
    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)
    context = { 'listings': paged_listings}

    return render(request, 'pages/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = { 'listing': listing}

    return render(request, 'pages/listing.html', context)