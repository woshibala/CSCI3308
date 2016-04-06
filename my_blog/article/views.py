from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from article.models import Article,User
from article.forms import SearchForm
import datetime
# Create your views here.


def home(request):
	return HttpResponse("this is home in view")

def detail(request, myargv):
	#return HttpResponse("this is my argv %s" % myargv)
	post = Article.objects.all()#[int(myargv)]
	aaa = ""
	for i in post:
		aaa += ("title = %s, category = %s, content = %s" % (i.title, i.category, i.content))
		aaa += "<br/>"
	return HttpResponse(aaa)

def search(request):
	return render_to_response("search.html")

def search_return(request):
	tit = request.GET['title']
	cate = request.GET['category']
	con = request.GET['content']
	a = Article(title=tit,category=cate,content=con)
	a.save()
	content = {
	 "tit" : tit,
	 "cate":cate,
	 "con" :con,
	 "ret" : request.GET['q']}
	return render(request,"search_return.html",content)

def index(request):
	post_list = Article.objects.all()   
	return render(request,"index.html",{"post_list":post_list})

def login(request):
	return render(request,"login.html",{'state': ""})

def signup(request):
	return render(request,"signup.html",{'state':""})

def add(request):
	return render(request,"add.html")

def add_return(request):
	username = request.session['username']
	tit = request.GET['title']
	cate = request.GET['category']
	cont = request.GET['content']
	#need cookie to identify user
	#dt = datetime.datetime.now() default is now!
	a = Article(title=tit,category=cate,content=cont,username=username)
	a.save()
	content = {
	  'title':tit,
	  'category':cate,
	  'datetime':datetime.datetime.now(),
	  'content': cont,
	  'username':username,
	  #still need to add username here
	}
	return render(request,"add_success.html",content)



def signup_return(request):
	uname = request.GET['username']
	e_mail = request.GET['email']
	if User.objects.filter(email=request.GET['email']).count() == 0:
		pwd = request.GET['password']
		uid = User.objects.count()
		u = User(username=uname,email=e_mail,password=pwd,user_id=uid)
		u.save()
		content = {
	 	 	'username':uname
		}
		return render(request,'index_login.html',content)
	else:#every email can only signup once
		return render(request,"signup.html",{'state': "User already exist!"})

def back_home(request):
	post_list = Article.objects.all()
	return render(request,'index_login.html',{"post_list":post_list})


@csrf_protect
def login_return(request):
	if User.objects.filter(email=request.GET['email']).count() == 0:
		return render(request,"login.html",{'state':"User doesn't exist!"})
	if User.objects.filter(email=request.GET['email']).count() == 1:
		u = User.objects.get(email=request.GET['email'])	
		if u.password == request.GET['password']:
			#if info correct go to index
			request.session['uid'] = u.id
			post_list = Article.objects.all()
			request.session['username'] = u.username
			return render(request,'index_login.html',{"post_list":post_list})
		else:
			#if password incorrect return error message
			content = 'Please enter the correct password!'
			return render(request,"login.html",{'state':content})
	else:#if find more than one user
		return HttpResponse("More than one user found! Error!")


