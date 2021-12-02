from django.urls import path
from .views import HomeView, ApplicationsView, ApplicationDetailView


urlpatterns = [
   
    path('', HomeView.as_view(), name='home'),
    path('applications/', ApplicationsView.as_view(), name='applications'),
    #pk is the primary of each application entry key number i.e. app 1 app2 etc
    path('application/<int:pk>', ApplicationDetailView.as_view(), name='application-detail')
]
