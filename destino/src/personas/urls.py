from django.urls import path
from .views import *

app_name='personas'

urlpatterns = [
    path('agregar/', personaCreateView, name='createPersona'),
    path("<int:myID>/", personasShowObject , name="browsing"),
    path("<int:myID>/delete/", personasDeleteView , name="deleting"),
    path( '', personasListView, name="listing"),
]
