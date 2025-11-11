from django import forms

class LandingForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    workspaceToggle = forms.BooleanField(label='Enable workspace selection', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'workspaceToggle'}))
    workspace = forms.ChoiceField(label='Workspace Name', choices=[], required=False, widget=forms.Select(attrs={'class': 'form-control', 'id': 'workspaceSelect'}))

    def __init__(self, *args, **kwargs):
        workspace_choices = kwargs.pop('workspace_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['workspace'].choices = workspace_choices