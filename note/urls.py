from django.urls import path
from .views import add_note_view

app_name = "note"
urlpatterns = [
    path('add-note/', add_note_view, name="add-note"),
]
