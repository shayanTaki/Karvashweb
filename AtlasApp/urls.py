from django.urls import path
from . import views
urlpatterns = [

    path("", views.index, name="AtlasApp"),
    # path("e", views.nav, name="BlogPegasus"),

]
