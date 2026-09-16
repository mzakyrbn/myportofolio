from django.forms import ModelForm, TextInput, Select
from main.models import Education

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
			"title": "education name",
			"category": "education category",
			"institution": "education's organizer",
			"year_start": "education's start year",
			"year_end": "education's end year",
		}

		widgets = {
			"title": TextInput(
				attrs={
					"placeholder": "portofolio website",
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

