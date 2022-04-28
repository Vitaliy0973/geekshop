from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from adminapp.forms import CategoryAdminCreateForm, CategoryAdminUpdateForm, ProductAdminCreateForm, UserAdminProfileForm, UserAdminRegisterForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin

from mainapp.models import Product, ProductCategories

# Пагинация
from django.core.paginator import Paginator

# Модули для CBV
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy

# Create your views here.


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):

#     context = {
#         'title': 'Админка',
#     }

#     return render(request, 'adminapp/admin.html', context)


class IndexTemplateView(TemplateView):

    template_name = 'adminapp/admin.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(IndexTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка'
        return context


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):

#     context = {
#         'title': 'Админка | Пользователи',
#         'users': User.objects.all(),
#     }

#     return render(request, 'adminapp/admin-users-read.html', context)


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):

    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка | Пользователи'
    context_object_name = 'users'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):

#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()

#     context = {
#         'title': 'Админка | Регистрация',
#         'form': form,
#     }

#     return render(request, 'adminapp/admin-users-create.html', context)


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):

    model = User
    template_name = 'adminapp/admin-users-create.html'
    title = 'Админка | Регистрация'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request, id):

#     user_select = User.objects.get(id=id)

#     if request.method == 'POST':
#         form = UserAdminProfileForm(
#             data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)

#     context = {
#         'title': 'Админка | Обновление пользователя',
#         "form": form,
#         'user_select': user_select,
#     }

#     return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):

    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title = 'Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request, id):

#     # Удаление пользователя
#     # user = User.objects.get(id=id).delete()

#     # Делаем пользователя неактивным вместо удаления учётной записи.
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))


class UserDeleteView(DeleteView, CustomDispatchMixin):

    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False if self.object.is_active else True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def admin_categories(request):

#     context = {
#         'title': 'Админка | Категории',
#         'categories': ProductCategories.objects.all(),
#     }

#     return render(request, 'adminapp/admin-categories-read.html', context)


class CategoriesListView(ListView, CustomDispatchMixin, BaseClassContextMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-read.html'
    title = 'Админка | Категории'
    context_object_name = 'categories'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_create(request):

#     if request.method == 'POST':
#         form = CategoryAdminCreateForm(data=request.POST)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_categories'))
#         else:
#             print(form.errors)
#     else:
#         form = CategoryAdminCreateForm()

#     context = {
#         'title': 'Админка | Новая категория',
#         'form': form,
#     }

#     return render(request, 'adminapp/admin-categories-create.html', context)


class CategoryCreateView(CreateView, CustomDispatchMixin, BaseClassContextMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-create.html'
    title = 'Админка | Новая категория'
    form_class = CategoryAdminCreateForm
    success_url = reverse_lazy('adminapp:admin_categories')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_update(request, id):

#     category_select = ProductCategories.objects.get(id=id)

#     if request.method == 'POST':
#         form = CategoryAdminUpdateForm(
#             data=request.POST, instance=category_select)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_categories'))
#         else:
#             print(form.errors)
#     else:
#         form = CategoryAdminUpdateForm(instance=category_select)

#     context = {
#         'title': 'Админка | Обновление категории',
#         'form': form,
#         'category_select': category_select,
#     }

#     return render(request, 'adminapp/admin-categories-update-delete.html', context)


class CategoryUpdateView(UpdateView, CustomDispatchMixin, BaseClassContextMixin):

    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    title = 'Админка | Обновление категории'
    form_class = CategoryAdminUpdateForm
    success_url = reverse_lazy('adminapp:admin_categories')
    context_object_name = 'category_select'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_delete(request, id):
#     category = ProductCategories.objects.get(id=id).delete()
#     return HttpResponseRedirect(reverse('adminapp:admin_categories'))


class CategoryDeleteView(DeleteView, CustomDispatchMixin):

    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_categories')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):

#     product_select = Product.objects.all()

#     context = {
#         'title': 'Админка | Продукты',
#         'product_select': product_select
#     }

#     return render(request, 'adminapp/admin-products-read.html', context)


class ProductListView(ListView, CustomDispatchMixin, BaseClassContextMixin):

    model = Product
    template_name = 'adminapp/admin-products-read.html'
    title = 'Админка | Продукты'
    context_object_name = 'product_select'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_create(request):

#     if request.method == 'POST':
#         form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminCreateForm()

#     context = {
#         'title': 'Админка | Новый продукт',
#         'form': form,
#     }

#     return render(request, 'adminapp/admin-products-create.html', context)


class ProductCreateView(CreateView, CustomDispatchMixin, BaseClassContextMixin):

    model = Product
    template_name = 'adminapp/admin-products-create.html'
    title = 'Админка | Новый продукт'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('adminapp:admin_products')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_update(request, id):

#     product_select = Product.objects.get(id=id)

#     if request.method == 'POST':
#         form = ProductAdminCreateForm(
#             data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminCreateForm(instance=product_select)

#     context = {
#         'title': 'Админка | Обновление продукта',
#         'form': form,
#         'product_select': product_select,
#     }

#     return render(request, 'adminapp/admin-products-update-delete.html', context)


class ProductUpdateView(UpdateView, CustomDispatchMixin, BaseClassContextMixin):

    model = Product
    form_class = ProductAdminCreateForm
    template_name = 'adminapp/admin-products-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_products')
    context_object_name = 'product_select'


# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_delete(request, id):
#     product_select = Product.objects.get(id=id).delete()
#     return HttpResponseRedirect(reverse('adminapp:admin_products'))


class ProductDeleteView(DeleteView, BaseClassContextMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    success_url = reverse_lazy('adminapp:admin_products')
