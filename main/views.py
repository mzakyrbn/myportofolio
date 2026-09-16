from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Experience
from main.models import Education
from main.forms import EducationForm
from portofolio import settings

def show_main(request):
    context = {
        "name": "Muhammad Zaky Robbani",
        "npm": "2506597712",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "CS student at Universitas Indonesia thats only just started coding after done doing the uni test. "
            "Due to having a gaming hobby on early age, my interest are slowly evolving into wanting to understand "
            "how game works and that lead me into taking career in computer world which is align with my interest."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Zaky Robbani",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_educations_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Muhammad Zaky Robbani",
        "education_list": educations,
        "title_query": title_query,
	}
    return render(request, "education.html", context)

def create_education(request):

	provided_key = request.headers.get("X-Admin-Key")

	if provided_key != settings.ADMIN_FEATURE_KEY:
		return JsonResponse(
			{"error": "Unauthorized"},
			status=401
		)

	form = EducationForm(request.POST or None)

	if request.method == "POST" and form.is_valid():
		form.save()
		messages.success(request, "Education baru berhasil ditambahkan!")
		return redirect("main:show_education")

	context = {
		"name": "jeff",
		"form": form,
	}
	return render(request, "educations_form.html", context)

def get_educations_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(title__icontains=title_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Laporan edukasi berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")