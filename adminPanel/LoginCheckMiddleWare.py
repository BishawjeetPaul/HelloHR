from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin




class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user

        if user.is_authenticated:

            if user.user_type == "1":
                if modulename == "adminPanel.adminViews":
                    pass
                elif modulename == "adminPanel.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse('admin-dashboard'))
            elif user.user_type == "2":
                if modulename == "adminPanel.hrViews":
                    pass
                elif modulename == "adminPanel.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse('hr-dashboard'))
            elif user.user_type == "3":
                if modulename == "adminPanel.staffViews":
                    pass
                elif modulename == "adminPanel.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse('staff-dashboard'))
            elif user.user_type == "4":
                if modulename == "adminPanel.freelancerViews":
                    pass
                elif modulename == "adminPanel.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse('freelancer-dashboard'))
            else:
                return HttpResponseRedirect(reverse('login'))
            
        # else:
            
        #     if request.path == reverse('login') or request.path == reverse('user-login'):
        #         pass
        #     else:
        #         return HttpResponseRedirect(reverse('login'))