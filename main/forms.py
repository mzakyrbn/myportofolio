from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateField
from main.models import Experience, Education
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

class ExperienceForm(ModelForm):
	class Meta:
		model = Experience
		fields = [
			"title",
			"description",
			"category",
			"thumbnail",
			"ended_at",
		]

		labels = {
			"title": "experience's name",
			"description": "experience's description",
			"category": "experience category",
			"thumbnail": "experience's thumbnail",
			"ended_at": "date the experience end",
		}

		widgets = {
			"title": TextInput(
				attrs={
					"placeholder": "main job",
					"maxlength": 255,
				}
			),
			"description": Textarea(
				attrs={
					"placeholder": "tell your story",
					"rows": 3,
				}
			),
			"category": Select(
				attrs={
					"placeholder": "full-time,part-time,volunteer,etc.",
					"class": "experience-category",
				}
			),
			"thumbnail": URLInput(
				attrs={
					"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
				}
			),
			"ended_at": TextInput(
				attrs={
					"placeholder": "format: YYYY-MM-DD HH:MM",
					"maxlength": 31,
				}
			)
		}

class EducationForm(ModelForm):
	class Meta:
		model = Education
		fields = [
			"title",
			"category",
			"institution",
			"year_start",
			"year_end",
		]

		labels = {
			"title": "education's name",
			"category": "education's category",
			"institution": "education's organizer",
			"year_start": "education's start year",
			"year_end": "education's end year",
		}

		widgets = {
			"title": TextInput(
				attrs={
					"placeholder": "official name",
					"maxlength": 255,
				}
			),
			"category": Select(
				attrs={
					"placeholder": "pick 'formal' or 'informal'",
					"class": "education-category",
				}
			),
			"institution": TextInput(
				attrs={
					"placeholder": "name of the institution",
					"maxlength": 255,
				}
			),
			"year_start": TextInput(
				attrs={
					"placeholder": "enter the year the education start",
					"maxlength": 15,
				}
			),
			"year_end": TextInput(
				attrs={
					"placeholder": "valid if same as start year",
					"maxlength": 15,
				}
			)
		}

		def clean_title(self):
			title = strip_tags(self.cleaned_data["title"]).strip()
			if not title:
				raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
			return title

		def clean_tech_stack(self):
			return strip_tags(self.cleaned_data["tech_stack"]).strip()

		def clean_description(self):
			return strip_tags(self.cleaned_data["description"]).strip()

