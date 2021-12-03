from django.urls import path
from . import views
from .views import HomeView, ApplicationsView, ApplicationDetailView, AddApplicationView, AddNoteView, UpdateApplicationView
# AddInterviewView


urlpatterns = [
      path('', HomeView.as_view(), name='home'),
      path('applications/', ApplicationsView.as_view(), name='applications'),
            #pk is the primary of each application entry key number i.e. app 1 app2 etc
      path('application/<int:pk>', ApplicationDetailView.as_view(), name='application-detail'),
      path('add_application/', AddApplicationView.as_view(), name='add_application'),
      path('application/<int:pk>/update/', UpdateApplicationView.as_view(), name='application_update'),
      path('application/<int:pk>/add_note/', AddNoteView.as_view(), name='add_note'),
      # path('application/<int:pk>/add_interview/', AddInterviewView.as_view(), name='add_interview'),

     ]
