from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers  import make_password, check_password 
from django.contrib.auth import login,logout
from .forms import RegisterForm,LoginForm
from .models import Person

# Create your views here.


def registerView(request):
	if request.method =='POST' :
		form = RegisterForm(request.POST)
		if form.is_valid() :
			username = request.POST['username']
			email	 = request.POST['email']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			phone	= request.POST['phone']
			password = make_password(request.POST['password'], salt=None, hasher='default')
			
			user = Person(username=username,password=password,first_name=first_name,last_name=last_name,email=email,phone=phone)
			user.save()

			return HttpResponseRedirect('/login')
	else:
		form=RegisterForm()

	context = {
			'form' : form
	}

	return render(request,'register.html',context)

def loginView(request):
	form = LoginForm()
	context = {
		'form' : form
		}
	
	if request.method== 'POST' :
		form = LoginForm(request.POST)
		if form.is_valid() :
			username= request.POST['username']
			password = request.POST['password']
			
			try:
				user = Person.objects.get(username=username)
			except:
				message = 'incorrect username' #incorrect username
				context['message']=message
				return render(request,'login.html',context)

			if user.check_password(password) and username == user.username:
				
				login(request,user)
				request.session['person_id']= user.id
				return HttpResponseRedirect('/profile')  #login success
			else:
				message = 'incorrect username or password' #incorrect password
				context['message']=message	
		
			return render(request,'login.html',context) # invalid password/username		

	return render(request,'login.html',context)

def signoutView(request):
	if request.user.is_authenticated:
		logout(request)
				
	return HttpResponseRedirect('/login')

def profileView(request):
	if request.user.is_authenticated:
		try:
			person=Person.objects.get(pk=request.session['person_id'])
		except :
			return redirect(loginView)

		if request.method =='POST':
			address = request.POST.get('address')
			gender  = request.POST.get('gender')
			profile_pic = request.POST.get('profile_pic')
			
			if address:
				person.address = address
			if gender:
				person.gender = gender
			if profile_pic:
				person.pic = profile_pic
			print(person.pic,'before')
			person.save()
			print(person.pic)
			
			HttpResponseRedirect('/profile')

		context={
			'person' : person
		}
		return render(request,'profile.html',context)
	else:
		return redirect(loginView)
	



