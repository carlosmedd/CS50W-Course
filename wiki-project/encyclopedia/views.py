from django.shortcuts import render
from markdown import markdown
from django.urls import reverse

from django.http import HttpResponseRedirect
from django import forms
from . import util
from random import choice

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title:")
    content = forms.CharField(label="",widget=forms.Textarea(attrs={"placeholder":"Content"}))

class EditEntryForm(forms.Form):
    title = forms.CharField(label="Title", disabled=True, required=False)
    content = forms.CharField(label="",widget=forms.Textarea(attrs={"placeholder":"Content"}))

class SearchEntryForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={
        "placeholder":"Search Encyclopedia",
        "class":"search"
        }))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search_form":SearchEntryForm()
    })

def wiki_entry(request, title):
    entry = util.get_entry(title)

    if entry is None:
        return render(request, "encyclopedia/wiki_error.html", {
            "title": title
        })

    return render(request, "encyclopedia/wiki_entry.html", {
        "title": title,
        "entry": markdown(entry)
    })

def create_page(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if title in util.list_entries():
                form.add_error("title", f"The {title} entry already exists.")
                return render(request, "encyclopedia/create_page.html", {
                    "form":form
                })

            util.save_entry(title, f"# {title}\n\n{content}")
            return HttpResponseRedirect(reverse("wiki_entry", args=[title]))

    return render(request, "encyclopedia/create_page.html", {
        "form":NewEntryForm()
    })

def edit_entry(request, title):
    if request.method == "POST":
        form = EditEntryForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(title, f"# {title}\n\n{content}")
            return HttpResponseRedirect(reverse("wiki_entry", args=[title]))
        
        else: 
            return render(request, "encyclopedia/edit_entry.html", {"title":title, "form":form})

    entry = util.get_entry(title)
    entry_content = entry.split("\n",2)[2]

    return render(request, "encyclopedia/edit_entry.html", {
        "title":title,
        "form":EditEntryForm(initial={"title":title, "content":entry_content})
    })

def random_entry(request):
    random_entry = choice(util.list_entries())
    return HttpResponseRedirect(reverse("wiki_entry", args=[random_entry]))

def search_entry(request):
        form = SearchEntryForm(request.GET)

        if form.is_valid():
            title = form.cleaned_data["title"]

            if title in util.list_entries():
                return HttpResponseRedirect(reverse("wiki_entry", args=[title]))
            
            else:
                return render(request, "encyclopedia/search_entry.html", {
                    "entries": [x for x in util.list_entries() if title in x]
                })