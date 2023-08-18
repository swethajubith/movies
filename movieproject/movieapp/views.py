
from . models import Movie1
from . forms import movie_form
from django.shortcuts import render,redirect

def index(request):
    movie=Movie1.objects.all()
    return render(request,"index.html",{'movielist':movie})
def detail(request,mid):
     movie=Movie1.objects.get(id=mid)
     return render(request,"detail.html",{'mo':movie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img= request.FILES['img']
        movie=Movie1(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,"add.html")
def update(request,id):
  mov=Movie1.objects.get(id=id)
  form=movie_form(request.POST or None,request.FILES,instance=mov)
  if form.is_valid():
      form.save()
      return redirect('/')
  return render(request,"edit.html",{'form':form,'movie':mov})

def delete(request,id):
    if request.method=="POST":
        movie=Movie1.objects.get(id=id)
        movie.delete()
        return redirect('/')

    return render(request,"delete.html")


