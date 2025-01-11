from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # authentication
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # listing
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<int:id_listing>", views.listing_view, name="listing"),
    path("listing/<int:id_listing>/place_bid", views.place_bid, name="place_bid"),
    path("listing/<int:id_listing>/close", views.close_listing, name="close_listing"),
    path("listing/<int:id_listing>/comment", views.comment, name="comment"),

    # filters
    path("categories", views.categories_view, name="categories"),
    path("categories/<int:id_category>", views.category_view, name="category"),
    path("user/<int:id_user>", views.user_listings, name="user_listings"),

    # watchlist
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/add/<int:id_listing>", views.add_to_watchlist, name="add_to_watchlist"),
    path("watchlist/remove/<int:id_listing>", views.remove_from_watchlist, name="remove_from_watchlist")
]
