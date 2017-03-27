
from django.conf.urls import url
from hey import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
]