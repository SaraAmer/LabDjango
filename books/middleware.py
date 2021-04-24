from django.http import HttpResponseForbidden
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required ,permission_required
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
  
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.username:
            if request.user.is_staff:
              return self.get_response(request)
            else:
              return HttpResponseForbidden("Please  Check your Email to active your account")

 
        return self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

       