from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from article.models import Article
from article.forms import SearchForm
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
	return render_to_response("login.html")

def signup(request):
	return render_to_response("signup.html")