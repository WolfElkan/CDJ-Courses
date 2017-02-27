# - - - - - DEPENDENCIES - - - - -

from django.shortcuts import render, redirect
from .models import Course

# - - - - - HELPER FUNCTIONS - - - - -

def seshinit(request, sesh, val=''):
	if sesh not in request.session:
		request.session[sesh] = val

def copy(source, keys=False):
	this = {}
	if not keys:
		keys = source.keys()
	for key in keys:
		this[key] = source[key]
	return this

# - - - - - DEVELOPER VIEWS - - - - -

def dbgui(request):
	seshinit(request,'command')
	context = {
		# Models
		'command': request.session['command']
	}
	return render(request, "main/dbgui.html", context)

def hot(request):
	command = request.POST['command']
	request.session['command'] = command
	exec(command)
	return redirect ('/dbgui')

def nuke(request):
	User.objects.all().delete()
	Message.objects.all().delete()
	Comment.objects.all().delete()
	return redirect ('/dbgui')

# - - - - - APPLICATION VIEWS - - - - -

def index(request):
	context = {
		"courses": Course.objects.all()
	}
	return render(request, "main/index.html", context)

def courses_create(request):
	Course.objects.create(
		course_name = request.POST['course_name'],
		description = request.POST['description']
	)
	return redirect('/')

def courses_delete(request,id):
	course = Course.objects.get(id=id)
	if request.method == "GET":
		context = {
			"course_name": course.course_name,
			"description": course.description
		}
		return render(request, "main/confirm.html", context)
	elif request.method == "POST":
		course.delete()
		return redirect('/')
	else:
		print "Someone's making up HTTP verbs"
		return redirect('/')






























