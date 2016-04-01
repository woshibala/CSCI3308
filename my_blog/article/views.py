from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from article.models import Article,User
from article.forms import SearchForm
from django.views.decorators.csrf import csrf_protect
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
	return render_to_response("index.html")  

def login(request):
	return render(request,"login.html",{'state': ""})

def signup(request):
	return render(request,"signup.html",{'state':""})

def add(request):
	return render_to_response("add.html")

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

@csrf_protect
def login_return(request):
	if User.objects.filter(email=request.GET['email']).count() == 0:
		return render(request,"login.html",{'state':"User doesn't exist!"})
	if User.objects.filter(email=request.GET['email']).count() == 1:
		u = User.objects.get(email=request.GET['email'])	
		if u.password == request.GET['password']:
			#if info correct go to index
			request.session['uid'] = u.id
			return render(request,'index_login.html',{'username':u.username})
		else:
			#if password incorrect return error message
			content = 'Please enter the correct password!'
			return render(request,"login.html",{'state':content})
	else:#if find more than one user
		return HttpResponse("More than one user found! Error!")


