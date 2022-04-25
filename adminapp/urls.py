from django.urls import path
from adminapp.views import CategoriesListView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView, IndexTemplateView, ProductCreateView, ProductDeleteView, ProductListView, ProductUpdateView, UserDeleteView, UserListView, UserCreateView, UserUpdateView


app_name = 'adminapp'

urlpatterns = [
    #     path('', index, name='index'),
    path('', IndexTemplateView.as_view(), name='index'),

    #     path('users/', admin_users, name='admin_users'),
    path('users/', UserListView.as_view(), name='admin_users'),

    #     path('user-create/', admin_user_create, name='admin_user_create'),
    path('user-create/', UserCreateView.as_view(), name='admin_user_create'),

    #     path('user-update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('user-update/<int:pk>/', UserUpdateView.as_view(),
         name='admin_user_update'),

    #     path('user-delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
    path('user-delete/<int:pk>/', UserDeleteView.as_view(),
         name='admin_user_delete'),

    #     path('categories/', admin_categories, name='admin_categories'),
    path('categories/', CategoriesListView.as_view(), name='admin_categories'),

    #     path('category-create/', admin_category_create, name='admin_category_create'),
    path('category-create/', CategoryCreateView.as_view(),
         name='admin_category_create'),

    #     path('category-update/<int:id>/', admin_category_update, name='admin_category_update'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(),
         name='admin_category_update'),

    #     path('category-delete/<int:id>/', admin_category_delete,name='admin_category_delete'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(),
         name='admin_category_delete'),

    #     path('products/', admin_products, name='admin_products'),
    path('products/', ProductListView.as_view(), name='admin_products'),

    #     path('product-create/', admin_product_create, name='admin_product_create'),
    path('product-create/', ProductCreateView.as_view(),
         name='admin_product_create'),

    #     path('product-update/<int:id>/', admin_product_update,name='admin_product_update'),
    path('product-update/<int:pk>/', ProductUpdateView.as_view(),
         name='admin_product_update'),

    #     path('product-delete/<int:id>/', admin_product_delete,name='admin_product_delete'),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view(),
         name='admin_product_delete'),

]
