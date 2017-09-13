from django.shortcuts import render
from django.views import generic

def index(request):
	return render(
		request,
		'index.html',
		context={},
	)
def paths(request):
	return render(
		request,
		'paths.html',
		context={},
	)
def courses(request):
	return render(
		request,
		'courses.html',
		context={},
	)
def codechefs(request):
	return render(
		request,
		'codechefs.html',
		context={},
	)
def signin(request):
	return render(
		request,
		'signin.html',
		context={},
	)
def course_template(request):
	return render(
		request,
		'course_template.html',
		context={},
	)
def topic_template(request):
	return render(
		request,
		'topic_template.html',
		context={},
	)
