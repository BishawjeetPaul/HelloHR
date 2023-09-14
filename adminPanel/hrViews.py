from django.shortcuts import render #Used to render the .html pages.




# Function to HR panel.
def dashboard(request):
    return render(request, 'hr-panel/dashboard.html')