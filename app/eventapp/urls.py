from django.urls import include, path
from .views import MyFormView

from . import views


urlpatterns = [
    path("createevent/", MyFormView.as_view()),

]