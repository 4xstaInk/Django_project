from django.conf.urls import url 
from tutors import views 
 
urlpatterns = [ 
    url(r'^api/tutors$', views.tutor_list),
    url(r'^api/tutors/(?P<pk>[0-9]+)$', views.tutor_detail),
    url(r'^api/tutors/published$', views.tutor_list_published)
]