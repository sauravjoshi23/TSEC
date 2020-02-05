from django import forms

club_choices = (
    ("Coding", "Coding"),
    ("Dance", "Dance"),
    ("Drama", "Drama"),
    ("Music", "Music"),
    ("Public Speaking", "Public Speaking"),
    ("Electronics", "Electronics"),
    ("Visual Arts", "Visual Arts"),
    ("Frisbee", "Frisbee"),
    ("Other", "Other"),
)

city_choices = (
    ("Mumbai", "Mumbai"),
    ("Pune", "Pune"),
    ("Other", "Other"),
)

class FormOne(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=200)
    clubs = forms.ChoiceField(choices=club_choices)
    city = forms.ChoiceField(choices=city_choices)
