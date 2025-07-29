from django.urls import path
from . import views

# recipe_list
urlpatterns = [
    path('', views.landing_home, name='home'),  # Landing page,
    path('recipehome/', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipesearch/', views.RecipeSearchView.as_view(), name="recipes-search"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about, name="recipes-about"),
    path('category/<str:category>/', views.RecipeCategoryView.as_view(), name='recipes-category'),
]

# path('', lambda request: __import__('recipes.views').views.recipe_list(request), name='recipes-home'