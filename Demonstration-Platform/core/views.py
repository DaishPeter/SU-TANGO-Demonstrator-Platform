
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LandingForm
# Create your views here.
def home_view(request):
    return render(request, "core/home.html")



AUTH_URL = "https://auth.tango.u-hopper.com"
WORKSPACES = [("tango_demo", "Tango_Demo")]
EXPERIENCES_BASE_ROUTE = "/exp"





INTERACTIVE_EXPERIENCES = [
    {
        "title": "Sliders",
        "description": "Navigate the latent space of AI models through a set of sliders.",
        "url": f"{EXPERIENCES_BASE_ROUTE}/sliders",
        "icon": "bi-sliders",
        "partners": [
            {"name": "Swansea AI Lab", "icon": "bi-building"},
            {"name": "TANGO Consortium", "icon": "bi-people"}
        ]
    },
    {
        "title": "Bongard",
        "description": "Solve visual reasoning problems that challenge AI models.",
        "url": f"{EXPERIENCES_BASE_ROUTE}/bongard",
        "icon": "bi-eye",
        "partners": [
            {"name": "Visual Reasoning Group", "icon": "bi-camera-video"}
        ]
    },
    {
        "title": "NeuroSymbolic",
        "description": "TBC",
        "url": f"{EXPERIENCES_BASE_ROUTE}/neurosymbolic",
        "icon": "bi bi-flower2",
        "partners": [
            {"name": "NeuroNet", "icon": "bi-cpu"},
            {"name": "Symbolic Systems", "icon": "bi-diagram-3"}
        ]
    }
]






def landing_page(request):
    workspace_options = WORKSPACES
    form = LandingForm(workspace_choices=workspace_options)

    if request.method == 'POST':
        form = LandingForm(request.POST, workspace_choices=workspace_options)
        
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            workspace_toggle = form.cleaned_data.get('workspaceToggle', False)
            workspace = form.cleaned_data['workspace'] if workspace_toggle else ""

            payload = {
                "email": username,
                "password": password,
            }
            if workspace_toggle:
                payload["workspace"] = workspace


            url = f"{AUTH_URL}/api/auth/token/obtain"

            try:
                response = requests.post(url, json=payload)
                data = response.json()
                print("Status:", response.status_code)
                print("Body:", response.text)

                if 'access' in data and 'refresh' in data:
                    request.session['access_token'] = data['access']
                    request.session['refresh_token'] = data['refresh']
                    request.session['username'] = username
                    request.session['workspace'] = workspace or 'N/A'
                    request.session['workspace_enabled'] = workspace_toggle
                    messages.success(request, "Login successful!")
                    return redirect('dashboard')
                else:
                    detail = data.get('detail', 'Unknown error')
                    messages.error(request, f"Login failed! {detail}")
            except requests.RequestException as e:
                messages.error(request, f"Network error: {str(e)}")
    
    return render(request, 'core/landing_page.html', {'form': form})


def dashboard_view(request):
    access_token = request.session.get('access_token')
    if not access_token:
        messages.warning(request, "You must log in first.")
        return redirect('landing_page')


    return render(request, 'core/dashboard.html', {
        'username': request.session.get('username', 'User'),
        'sessions': INTERACTIVE_EXPERIENCES,
    })



def sliders_view(request):

    return render(request, 'core/exp/sliders.html')