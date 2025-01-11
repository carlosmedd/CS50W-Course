from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment
from .forms import *




def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings":listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
        
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            image_url = form.cleaned_data["image_url"]
            category = form.cleaned_data["category"]
            creator = request.user

            listing = Listing(title=title, description=description, price=price, image_url=image_url, category=category, creator=creator)
            listing.save()
            return HttpResponseRedirect(reverse("listing", args=[listing.id]))

        else:
            return render(request, "auctions/create_listing.html", {
                "form":form
            })

    return render(request, "auctions/create_listing.html", {
        "form":ListingForm()
    })

def listing_view(request, id_listing):
    listing = Listing.objects.get(pk=id_listing)

    if listing.current_bid():
        bid_owner = listing.current_bid().user == request.user
    else:
        bid_owner = False
    
    return render(request, "auctions/listing.html", {
        "listing":listing,
        "listing_owner": request.user.is_authenticated and request.user == listing.creator,
        "len_bids":len(listing.bids.all()),
        "bid_form":PlaceBidForm(),
        "is_in_watchlist": request.user.is_authenticated and listing in request.user.watchlist.all(),
        "bid_owner":bid_owner,
        "comments": listing.comments.all()
    })

def close_listing(request, id_listing):
    listing = Listing.objects.get(pk=id_listing)

    if listing.creator == request.user:
        listing.is_active = False
        listing.save()
        return HttpResponseRedirect(reverse("listing", args=[id_listing]))
    
    return HttpResponseBadRequest("Invalid request method.")

@login_required
def comment(request, id_listing):
    if request.method == "POST":
        content = request.POST["content"]
        listing = Listing.objects.get(pk=id_listing)
        new_comment = Comment(content=content, user=request.user, listing=listing)
        new_comment.save()
        
        return HttpResponseRedirect(reverse("listing", args=[id_listing]))

@login_required
def place_bid(request, id_listing):
    if request.method == "POST":
        form = PlaceBidForm(request.POST)
        listing = Listing.objects.get(pk=id_listing)
        user = request.user

        if form.is_valid():
            amount = form.cleaned_data["amount"]

            if amount > listing.price:
                bid = Bid(listing=listing, user=user, amount=amount)
                bid.save()
                listing.price = amount
                listing.save()
                return HttpResponseRedirect(reverse("listing", args=[id_listing]))
            
            else:
                form.add_error("amount", "The bid must be higher than the current price.")
                
        return render(request, "auctions/listing.html", {
        "listing":listing,
        "bid_form":form
    })

    else:
        return HttpResponseBadRequest("Invalid request method.")

def categories_view(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def category_view(request, id_category):
    category = Category.objects.get(pk=id_category)
    listings = category.listings.all()
    return render(request, "auctions/index.html", {
        "listings":listings
    })

def user_listings(request, id_user):
    user = User.objects.get(pk=id_user)
    listings = user.listings.all()

    return render(request, "auctions/index.html", {
        "listings":listings
    })

@login_required
def watchlist(request):
    listings = request.user.watchlist.all()
    print(listings)
    return render(request, "auctions/watchlist.html", {
        "listings":listings
    })

@login_required
def add_to_watchlist(request, id_listing):
    listing = Listing.objects.get(pk=id_listing)
    request.user.watchlist.add(listing)
    return HttpResponseRedirect(reverse("listing", args=[id_listing]))

@login_required
def remove_from_watchlist(request, id_listing):
    listing = Listing.objects.get(pk=id_listing)
    request.user.watchlist.remove(listing)
    return HttpResponseRedirect(reverse("listing", args=[id_listing]))