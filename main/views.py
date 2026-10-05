from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience, Education
from main.forms import ExperienceForm, EducationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied 
from django.views.decorators.http import require_POST
import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    
    context = {
        "name": "Muhammad Zaky Robbani",
        "npm": "2506597712",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia thats only just started coding after done doing the uni test. "
            "Due to having a gaming hobby on early age, my interest are slowly evolving into wanting to understand "
            "how game works and that lead me into taking career in computer world which is align with my interest."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    editor = is_editor(request.user)
    
    context = {
        "name": "Muhammad Zaky Robbani",
        "title_query": title_query,
        "editor": editor,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)


@login_required(login_url="/login/")
def save_experience(request, experience_id=None):
    if not request.user.is_superuser:
        raise PermissionDenied

    if experience_id is not None:
        experience = get_object_or_404(Experience, id=experience_id)
    else:
        experience = None
        
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()

        if experience:
            messages.success(request, "pengalaman berhasil diubah!")
        else:
            messages.success(request, "pengalaman baru berhasil ditambah!")
            
        return redirect("main:show_experience")

    context = {
           "name": "Muhammad Zaky Robbani",
           "form": form,
    }
    return render(request, "experiences_form.html", context)


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "thumbnail": experience.thumbnail,
                "ended_at": experience.ended_at,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        
    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")


def show_education(request):
    title_query = request.GET.get("title", "").strip()
    editor = is_editor(request.user)
    
    context = {
        "name": "Muhammad Zaky Robbani",
        "title_query": title_query,
        "editor": editor,
        "form": EducationForm(),
    }
    return render(request, "education.html", context)


@login_required(login_url="/login/")
def save_education(request, education_id=None):
    if not request.user.is_superuser:
        raise PermissionDenied

    if education_id is not None:
        education = get_object_or_404(Education, pk=education_id)
    else:
        education = None
             
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()

        if education:
            messages.success(request, "laporan edukasi berhasil diubah!")
        else:
            messages.success(request, "laporan edukasi baru berhasil ditambah!")
    
        return redirect("main:show_education")

    context = {
        "name": "Muhammad Zaky Robbani",
        "form": form,
    }
    return render(request, "educations_form.html", context)


@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan laporan edukasi."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "laporan edukasi berhasil ditambahkan.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


def get_educations_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.prefetch_related('starred_by').all()

    if title_query:
        educations = educations.filter(title__icontains=title_query)

    data = []
    for education in educations:
        starred_users = education.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(education.id),
            "fields": {
                "title": education.title,
                "category": education.category,
                "institution": education.institution,
                "year_start": education.year_start,
                "year_end": education.year_end,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        
    return JsonResponse(data, safe=False)


@login_required(login_url="/login/")
def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Laporan edukasi berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")


@login_required(login_url="/login/")
def toggle_star_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_education")


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Muhammad Zaky Robbani",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Muhammad Zaky Robbani",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


def is_editor(user):
    return user.groups.filter(name='editor').exists()