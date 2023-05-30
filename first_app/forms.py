from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label="Username")
    file = forms.FileField()
    # email = forms.EmailField(label="Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField(label="Weight")
    # balance = forms.DecimalField()
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEAL = [('P', 'Pepperoni'), ('C', 'Cheese'), ('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)
