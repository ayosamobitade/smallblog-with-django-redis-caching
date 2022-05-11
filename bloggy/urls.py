
from django.urls import path


from bloggy.views import bloggyView, phoneView


urlpatterns = [
    path("", bloggyView.as_view(), name = "bloggy"),
    path("/<slug>", phoneView.as_view(), name = "phone")
]