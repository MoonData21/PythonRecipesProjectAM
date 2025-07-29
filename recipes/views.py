from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe

def landing_home(request):
    return render(request, 'recipes/landing_home.html')

# Recipe List View (displays all recipes)
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'  # Or a specific list template, e.g., 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 20  # Number of recipes per page

    def get_queryset(self):
        # Simply return all recipes
        return Recipe.objects.all()

# Recipe Search View (handles search functionality)
class RecipeSearchView(ListView):
    model = Recipe
    template_name = 'recipes/search_form.html'  # Use a different template for search results
    context_object_name = 'recipes'
    paginate_by = 20  # Consistent pagination with RecipeListView

    def get_queryset(self):
        # Handle search query
        query = self.request.GET.get("q")
        if query:
            return Recipe.objects.filter(title__icontains=query)
        return Recipe.objects.none()  # Return empty queryset if no query (or redirect to list view)

    def get_context_data(self, **kwargs):
        # Add the search query to the context for display in the template
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("q", "")
        return context

# About view (unchanged)
def about(request):
    return render(request, 'recipes/about.html', {'title': 'about page'})

# Recipe Detail View (unchanged)
class RecipeDetailView(DetailView):
    model = Recipe

# Recipe Delete View (unchanged)
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

# Recipe Create View (unchanged)
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Recipe Update View (unchanged)
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description', 'category']

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class RecipeCategoryView(ListView):
    model = Recipe
    template_name = 'recipes/category.html'
    context_object_name = 'recipes'
    paginate_by = 20

    def get_queryset(self):
        category = self.kwargs.get('category')
        return Recipe.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('category')
        return context


"""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#from .models import Recipe
from . import models
from .models import Recipe

class RecipeListView(ListView):
  model = models.Recipe
  template_name = 'recipes/home.html'
  context_object_name = 'recipes'

# Create your views here.
def home(request):
  recipes = models.Recipe.objects.all()
  context = {
    'recipes': recipes
  }
  return render(request, 'recipes/home.html', context)

def about(request):
  return render(request, 'recipes/about.html', {'title': 'about page'})


class RecipeDetailView(DetailView):
  model = models.Recipe

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  success_url = reverse_lazy('recipes-home')

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
  model = models.Recipe
  fields = ['title', 'description']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Recipe
  fields = ['title', 'description']

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
"""