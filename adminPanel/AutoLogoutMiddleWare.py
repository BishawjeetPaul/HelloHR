from django.contrib import auth
from django.contrib.sessions.models import Session
from django.utils import timezone




class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check if the user has a session
            session_key = request.session.session_key
            if session_key:
                # Get the session object
                session = Session.objects.get(session_key=session_key)
                last_activity = session.get_decoded().get('_auth_user_last_activity')
                if last_activity:
                    # Calculate the session timeout based on your SESSION_COOKIE_AGE setting
                    session_timeout = auth.SESSION_COOKIE_AGE
                    if (timezone.now() - last_activity).seconds >= session_timeout:
                        # Logout the user if they have exceeded the session timeout
                        auth.logout(request)
        response = self.get_response(request)
        return response