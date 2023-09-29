from django.shortcuts import render #Used to render the .html pages.





# Function to HR panel.
def dashboard(request):
    return render(request, 'hr-panel/dashboard.html')


def candidate_detail(request):
    return render(request, "hr-panel/candidate-detail.html")

def candidate_manage(request):
    return render(request, "hr-panel/candidate-manage.html")

def candidate_selected(request):
    return render(request, "hr-panel/candidate-selected.html")

def candidate_rejected(request):
    return render(request, "hr-panel/candidate-rejected.html")