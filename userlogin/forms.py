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

decision_dict = (
    ("Accept", "Accept"),
    ("Reject", "Reject"),
)

class FormOne(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=200)
    clubs = forms.ChoiceField(choices=club_choices)
    city = forms.ChoiceField(choices=city_choices)
    address = forms.CharField( max_length=200, widget=forms.Textarea(attrs={"rows" : 3, "cols" : 90}) )


class FormTwo(forms.Form):
    experience = forms.CharField(label="Please describe your past experience in this field.", widget=forms.Textarea(attrs={"rows" : 7, "cols" : 90}))
    why_aims = forms.CharField(label="Why do want to do this and what do you hope to achieve ?", widget=forms.Textarea(attrs={"rows" : 7, "cols" : 90}))

class DecisionForm(forms.Form):
    decision = forms.ChoiceField(choices=decision_dict)

class AttendanceForm(forms.Form):
    email = forms.EmailField()

