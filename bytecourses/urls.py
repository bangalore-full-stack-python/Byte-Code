from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^paths/$', views.paths, name='paths'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^codechefs/$', views.codechefs, name='codechefs'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^courses/course_template/$', views.course_template, name='course_template'),
    url(r'^courses/course_template/topic_template/$', views.topic_template, name='topic_template'),

]
