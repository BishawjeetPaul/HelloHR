from django.shortcuts import render #Used to render the .html pages.





# Function to HR panel.
def dashboard(request):
    return render(request, 'hr-panel/dashboard.html')


def candidate_detail(request):
    return render(request, "hr-panel/candidate-detail.html")

def candidate_manage(request):
    return render(request, "hr-panel/candidate-manage.html")