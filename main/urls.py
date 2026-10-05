from django.urls import path

from main.views import show_main, show_experience, save_experience, create_experience_ajax, get_experiences_json, delete_experience, toggle_star_experience, show_education, save_education, create_education_ajax, get_educations_json, delete_education, register, login_user, logout_user, toggle_star_education

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
	path("experience/save/", save_experience, name="create_experience"),
	path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
	path("experience/<uuid:experience_id>/save/", save_experience, name="update_experience"),
	path("api/experiences/", get_experiences_json, name="get_experiences_json"),
	path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
	path("experience/<uuid:experience_id>/star/", toggle_star_experience, name="toggle_star_experience"),
	path("education/", show_education, name="show_education"),
	path("education/add/", save_education, name="create_education"),
	path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
	path("education/<uuid:education_id>/save/", save_education, name="update_education"),
	path("api/educations/", get_educations_json, name="get_educations_json"),
	path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
	path("education/<uuid:education_id>/star/", toggle_star_education, name="toggle_star_education"),
	path("register/", register, name="register"),
	path("login/", login_user, name="login"),
	path("logout/", logout_user, name="logout"),
]