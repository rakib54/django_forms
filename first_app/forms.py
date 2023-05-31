from django import forms
from django.core import validators


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


def len_check(text):
    if (len(text) < 10):
        raise forms.ValidationError("Enter a value at least 10 character")


class Student_Data(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(
        10, message='Enter a name with at least 10 characters')])
    email = forms.CharField(widget=forms.EmailInput,
                            validators=[validators.EmailValidator(message='Enter a valid email')])
    text = forms.CharField(widget=forms.TextInput(), validators=[len_check])


class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_confirm_pass = self.cleaned_data['confirm_password']
        if val_pass != val_confirm_pass:
            raise forms.ValidationError('Password does not match')
