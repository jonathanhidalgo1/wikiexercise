from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound,HttpResponse
import re
import random


from . import util


def index(request):
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
                   
def library(request, name):
    test = util.convert_entry(name)
    return render(request, "encyclopedia/library.html", {
        "name":name ,"texts":util.get_entry_html(name)
    })
               
def search(request):
    
    if request.method == "POST":
        searched = request.POST["searched"]        
        r = re.compile(f".*{searched}")
        newlist = list(filter(r.match, util.list_entries())) #match similar names in the search        
        
        for entry in util.list_entries():
            if searched.lower() == entry.lower():
                return HttpResponseRedirect(reverse("library", kwargs={"name":entry})) #redirect dynamic url                     

        if newlist:          
            return render(request, "encyclopedia/search.html", {
                "searchlist": newlist
            })  
                        
        else:
            return HttpResponseNotFound(f'<h1>Page {searched} not found</h1>')
        
def create(request):
    if request.method == "POST":
        title = request.POST["title"] 
        content = request.POST["content"]
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "encyclopedia/create.html")    

def edit(request, name):    
    if request.method == "POST":        
        content = request.POST["content"]
        util.save_entry(name, content)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "encyclopedia/edit.html", {
        "name": name, "texts": util.get_entry(name)
    })
    
def random_page(request):
    entries = util.list_entries() # list of wikis
    selected_page = random.choice(entries)
    return HttpResponseRedirect(reverse("library", kwargs={"name":selected_page}))