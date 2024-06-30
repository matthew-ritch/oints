from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/checkbalance/<str:oint_id>/<str:address>", views.checkbalance, name="checkbalance"),
    path("api/mint_oints_to_address/<str:oint_id>/<str:address>/<int:amount>/<str:company_api_key>", views.mint_oints_to_address, name="mint_oints_to_address"),
]
