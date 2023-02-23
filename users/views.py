from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.urls import reverse_lazy, reverse
from products.models import Basket
from users.models import User, EmailConfirmation


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('index')


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    success_message = 'You have successfully registered!'


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        context['total_quantity'] = sum(basket.quantity for basket in context['baskets'])
        context['total_sum'] = sum(basket.sum() for basket in context['baskets'])
        return context


class LogoutUserView(LogoutView):

    def get_default_redirect_url(self):
        return reverse_lazy('login')


class EmailConfirmationView(TemplateView):
    template_name = 'users/email_confirmation.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_confirmation = EmailConfirmation.objects.filter(user=user, code=code)
        if email_confirmation.exists() and not email_confirmation.first().is_expired():
            user.is_the_email_confirmed = True
            user.save()
            return super(EmailConfirmationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
