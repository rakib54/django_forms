from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label="Username", widget=forms.Textarea(
        attrs={'placeholder': "Your name"}))
    # file = forms.FileField()
    email = forms.EmailField(label="Email")
    age = forms.IntegerField()
    weight = forms.FloatField(label="Weight")
    balance = forms.DecimalField()
    birthdate = forms.CharField(widget=forms.DateInput(attrs={'type': "date"}))
    appointment = forms.CharField(
        widget=forms.DateInput(attrs={'type': "datetime-local"}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('C', 'Cheese'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL)
