from django import forms
# from .models import Watcher

class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=300)
    repo_url = forms.CharField(required=False)
    package_name = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super(SubscribeForm, self).clean()  
        repo = cleaned_data.get("repo_url")
        package = cleaned_data.get("package_name"),
        
        if not repo and package == (u'',):  # wtf?
            raise forms.ValidationError('Please fill in at least one option[repo/package].')

        return cleaned_data
