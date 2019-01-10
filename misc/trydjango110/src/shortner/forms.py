from django import forms
from django.core.validators import URLValidator
from django.core.validators import ValidationError

# Another way of validating the fields in addition to clean (form-level) and clean_url_1234 (field-level)
def validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError('Invalid url')
    return value

def validate_url_ending_with_dot_come(value):
    if not str(value).endswith('.com'):
        raise ValidationError('Not ending with .com')
    return value


class SubmitUrlForm(forms.Form):
    url_1234 = forms.CharField(label='Field #1')

    # USING THE FOLLOWING WAY, WE CAN ADD VALIDATORS IN THE MODELS AS WELL
    url_5678 = forms.CharField(label='Field #2', validators=[validate_url, validate_url_ending_with_dot_come])

    # Validating on the form [EVENTUALLY IT CALLS FIELD SPECIFIC clean method]
    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        # url = cleaned_data['url_1234']
        # print('clean::', url)

    # Validating on the field of the form (clean_<fieldName>)
    def clean_url_1234(self):
        url = self.cleaned_data['url_1234']
        print('clean_url::', url)
        url_validator = URLValidator()
        try:
            url_validator(url)
        except:
            raise forms.ValidationError("Invalid URL for this field")
        return url
