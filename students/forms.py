from xml.parsers.expat import model

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields = '__all__'


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Name must contain only letters and spaces.")
        return name
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def clean_university_id(self):
        university_id = self.cleaned_data['university_id']
        number = str(university_id)
        if len(number) != 9:
            raise forms.ValidationError("University ID must be exactly 9 digits.")

        if not number.startswith(("1", "2")):
            raise forms.ValidationError("University ID must start with 1 or 2.")
        
        return university_id
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def clean_national_id(self):
        national_id = self.cleaned_data['national_id']
        number = str(national_id)
        if len(number) != 9:
            raise forms.ValidationError("National ID must be exactly 9 digits.")
        
        if not number.startswith(("9", "8", "4")):
            raise forms.ValidationError("National ID must start with 9, 8, or 4.")

        return national_id
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number must contain digits only.")
        
        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        
        if not mobile.startswith(("059", "056")):
            raise forms.ValidationError("Mobile number must start with 059 or 056.")
        
        return mobile
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def clean_image(self):
        image = self.cleaned_data['image']
        if not image.name.lower().endswith(('.jpg', '.png')):
            raise forms.ValidationError("Image must be JPG or PNG only.")

        return image