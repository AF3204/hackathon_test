from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'Grounds Operator':
			return redirect('user-page')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function

# @unauthenticated_user
# @admin_only

# from django.core.mail import send_mail
# from django.conf import settings

# def email(request):
#     subject = 'New Incident Happended'
#     message = ' You look so good Today keep it up ;)'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['receiver@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('redirect to a new page')