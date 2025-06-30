from django.urls import path

from .views.project_view import ProjectView

urlpatterns = [
    path('' , ProjectView.as_view() , name='home')
]