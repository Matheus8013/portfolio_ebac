from django.http import HttpResponse
from django.views import generic

from personal_portfolio.models import Project

class ProjectView(generic.ListView):
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'