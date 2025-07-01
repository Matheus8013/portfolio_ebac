from django.urls import path

from .views.project_view import ProjectView, ProjectDetail

urlpatterns = [
    path('' , ProjectView.as_view() , name='home'),
    path('<slug:slug>/', ProjectDetail.as_view(), name='project_detail'),
]