from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.views.generic import CreateView, FormView
from .forms import LoginForm, RegisterForm

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'
    login_url = "/"

    # If form is valid (no validation errors)
    def form_valid(self, form):
        request = self.request

        # Get the Redirection Path After Logging in
        next_get = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_get or next_post or None

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        # If the User did not check "Remember Me", then it will not remember session.
        if form.cleaned_data.get('remember_me') is None:
            request.session.set_expiry(0)
        
        # authenticate user
        user = authenticate(request, username=email, password=password)

        # if user exists
        if user is not None:

            # Login user into the redirect path
            login(request, user)

            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
                
        return super().form_invalid(form)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = '/account/login/'

def logout_view(request):
    logout(request)
    return redirect('/')