from django.shortcuts import render #Used to render the .html pages.




# Function to Freelancer panel.
def dashboard(request):
    return render(request, 'freelancer-panel/dashboard.html')

def candidate_submission(request):
    return render(request, "freelancer-panel/candidate-submission.html")