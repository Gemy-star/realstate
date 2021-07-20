from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.all_projects, name='all-projects'),
    path('states/<int:pk>', views.all_state, name='all-state'),
    path('states/developer/<int:pk>', views.all_state, name='all-state-developer')

]
