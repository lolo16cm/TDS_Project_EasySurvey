from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import get_object_or_404, render
from create_form.models import Form
from user_auth.models import Profile

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    forms = Form.objects.filter(creator = request.user)
    profile = get_object_or_404(Profile, user=request.user)

    edited_forms = []
    published_forms = []
    republished_forms = []
    closed_forms = []

    for form in forms:
        if form.status.lower() == "edit":
            edited_forms.append(form)
        elif form.status.lower() == "publish":
            published_forms.append(form)
        elif form.status.lower() == "republish":
            republished_forms.append(form)
        elif form.status.lower() == "close":
            closed_forms.append(form)

    return render(request, "easy_survey/index.html", {
        "edit_forms": edited_forms,
        "published_forms": published_forms,
        "republished_forms": republished_forms,
        "closed_forms": closed_forms,
        "role": profile.role
    })

def results(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    forms = Form.objects.filter(creator = request.user)
    all_forms = Form.objects.all()
    published_forms = []
    all_published_forms = []
    republished_forms = []
    all_republished_forms = []
    closed_forms = []

    for form in forms:
        if form.status.lower() == "publish":
            published_forms.append(form)
        elif form.status.lower() == "republish":
            republished_forms.append(form)
        elif form.status.lower() == "close":
            closed_forms.append(form)
    
    for form in all_forms:
        if form.status.lower() == "publish":
            all_published_forms.append(form)
        elif form.status.lower() == "republish":
            all_republished_forms.append(form)

    profile = get_object_or_404(Profile, user=request.user)

    all_forms = Form.objects.all()
    published_forms = []
    all_published_forms = []
    republished_forms = []
    all_republished_forms = []
    closed_forms = []

    for form in forms:
        if form.status.lower() == "publish":
            published_forms.append(form)
        elif form.status.lower() == "republish":
            republished_forms.append(form)
        elif form.status.lower() == "close":
            closed_forms.append(form)
    
    for form in all_forms:
        if form.status.lower() == "publish":
            all_published_forms.append(form)
        elif form.status.lower() == "republish":
            all_republished_forms.append(form)
    
    return render(request, "easy_survey/results.html", {
        "forms": forms,
        "published_forms": published_forms,
        "republished_forms": republished_forms,
        "closed_forms": closed_forms,
        "all_published_forms": all_published_forms,
        "all_republished_forms": all_republished_forms,
        "role": profile.role
    })

def published(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    all_forms = Form.objects.all()
    all_published_forms = []
    
    for form in all_forms:
        if form.status.lower() == "publish":
            all_published_forms.append(form)

    return render(request, "easy_survey/published.html", {
        "all_published_forms": all_published_forms,
    })

def republished(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    all_forms = Form.objects.all()
    all_republished_forms = []
    
    for form in all_forms:
        if form.status.lower() == "republish":
            all_republished_forms.append(form)
    
    return render(request, "easy_survey/republished.html", {
        "all_republished_forms": all_republished_forms,
    })