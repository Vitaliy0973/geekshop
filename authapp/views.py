from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, FormView
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from adminapp.mixin import BaseClassContextMixin, UserDispatchMixin
from authapp.forms import UserLoginForm, UserProfileEditForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from basket.models import Basket

# Create your views here.


# def login(request):

#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = auth.authenticate(username=username, password=password)
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 print('Юзер не активный')
#         else:
#             print(form.errors)
#     else:
#         form = UserLoginForm()

#     context = {
#         'title': 'Geekshop | Авторизация',
#         'form': form
#     }
#     return render(request, 'authapp/login.html', context)


class LoginGBView(LoginView, BaseClassContextMixin):

    title = 'Geekshop | Авторизация'
    form_class = UserLoginForm
    template_name = 'authapp/login.html'


# def register(request):

#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегестрировались')
#             return HttpResponseRedirect(reverse('authapp:login'))
#         else:
#             print(form.errors)
#     else:
#         form = UserRegisterForm()

#     context = {
#         'title': 'Geekshop | Регистрация',
#         'form': form
#     }
#     return render(request, 'authapp/register.html', context)


class RegisterView(FormView, BaseClassContextMixin):

    model = User
    title = 'Geekshop | Регистрация'
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегестрировались')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        context = {'form': form}
        return render(request, self.template_name, context)

    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[
                              user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылке'
        message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activate_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activate_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(
                    self, user, backend='django.contrib.auth.backend.ModelBackend')
            return render(self, 'authapp/verification.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('index'))


# @login_required
# def profile(request):

#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user,
#                                data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#         else:
#             print(form.errors)

#     user_select = request.user

#     context = {
#         'title': 'Geekshop | Профиль',
#         'form': UserProfileForm(instance=user_select),
#         'baskets': Basket.objects.filter(user=user_select),
#     }
#     return render(request, 'authapp/profile.html', context)


class ProfileFormView(UpdateView, BaseClassContextMixin, UserDispatchMixin):

    # model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    title = 'Geekshop | Профиль'

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(
            data=request.POST, files=request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(
            data=request.POST, files=request.FILES, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data()
        context['profile'] = UserProfileEditForm(
            instance=self.request.user.userprofile)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileFormView, self).get_context_data()
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context

    def from_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, 'Вы успешно сохранили профиль')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.pk)


# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')


class Logout(LogoutView):
    template_name = 'mainapp/index.html'
