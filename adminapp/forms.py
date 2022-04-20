from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from authapp.models import User
from mainapp.models import Product, ProductCategories


class UserAdminRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):

        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['age'].widget.attrs['placeholder'] = 'Возраст'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custop-file-input'


class UserAdminProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'last_name',
                  'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'from-control py-1'

        self.fields['image'].widget.attrs['class'] = 'custop-file-input'


class CategoryAdminCreateForm(forms.ModelForm):

    class Meta:
        model = ProductCategories
        fields = ('name', 'descriptions')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название категории'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Введите описание категории'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'from-control py-1'


class CategoryAdminUpdateForm(forms.ModelForm):

    class Meta:
        model = ProductCategories
        fields = ('name', 'descriptions')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminUpdateForm, self).__init__(*args, **kwargs)
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Введите описание категории'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'from-control py-1'


class ProductAdminCreateForm(forms.ModelForm):

    # Переопределение image не помогло решить проблему. Label накладывается на input и невозможно вызвать меню выбора файла.
    # image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Product
        fields = ('name', 'descriptions', 'price',
                  'quantity', 'category', 'image')

    def __init__(self, *args, **kwargs):
        super(ProductAdminCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название продукта'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Введите описание продукта'
        self.fields['price'].widget.attrs['placeholder'] = 'Введите цену продукта'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Введите количество продукта'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'from-control py-1'
        self.fields['image'].widget.attrs['class'] = 'custop-file-input'
