from django.shortcuts import render

from main.models import Experience

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