from django.shortcuts import render #Used to render the .html pages.




# Function to staff panel.
def dashboard(request):
    return render(request, 'staff-panel/dashboard.html')