from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal, Dessert, Comment, DessertComment
from .forms import CommentForm, DessertCommentForm


# Home page view

def home_view(request):
    return render(request, "thai/index.html")


# Meal detail view shows comments and edit buttons

class mealDetailView(DetailView):
    model = Meal
    context_object_name = 'meal'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['comments'] = Comment.objects.filter(meal=self.object)
        return context


# Meal view shows Meal menu page

def meal_view(request):
    request.session.set_expiry(0)
    template = "thai/meal.html"
    meal_objects = Meal.objects.all()
    context = {
        'meal_objects': meal_objects, 'active_link': 'meal'}
    return render(request, template, context)


# Dessert detail view shows Dessert detail and comments and edit buttons

class dessertDetailView(DetailView):
    model = Dessert
    context_object_name = 'dessert'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['comments'] = DessertComment.objects.filter(dessert=self.object)
        return context


# Dessert view shows Dessert menu page

def dessert_view(request):
    request.session.set_expiry(0)
    template = "thai/dessert.html"
    dessert_objects = Dessert.objects.all()
    context = {
        'dessert_objects': dessert_objects, 'active_link': 'dessert'}
    return render(request, template, context)


# Meal comments form

class commentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    context_object_name = 'comment'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.meal = Meal.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('meal_detail', kwargs={'pk': pk})


# Meal comments edit button

class commentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    context_object_name = 'comment'
    form_class = CommentForm

    def get_success_url(self):
        pk = self.kwargs['id']
        return reverse_lazy('meal_detail', kwargs={'pk': pk})


# Meal comments delete button

class commentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        pk = self.kwargs['id']
        return reverse_lazy('meal_detail', kwargs={'pk': self.object.meal.pk})


# Dessert comments form

class dessertCommentCreateView(LoginRequiredMixin, CreateView):
    model = DessertComment
    context_object_name = 'comment'
    form_class = DessertCommentForm

    def form_valid(self, form):
        form.instance.dessert = Dessert.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('dessert_detail', kwargs={'pk': pk})


# Dessert comments edit button

class dessertCommentUpdateView(LoginRequiredMixin, UpdateView):
    template = "thai/dessertcomment_update.html"
    model = DessertComment
    context_object_name = 'comment'
    form_class = DessertCommentForm

    def get_success_url(self):
        pk = self.kwargs['id']
        return reverse_lazy('dessert_detail', kwargs={'pk': self.object.dessert.pk})


# Dessert comments delete button

class dessertCommentDeleteView(LoginRequiredMixin, DeleteView):
    model = DessertComment

    def get_success_url(self):
        pk = self.kwargs['id']
        return reverse_lazy('dessert_detail', kwargs={'pk': self.object.dessert.pk})


# Cart page

@csrf_exempt
def cart_view(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['order'] = request.POST.get('orders')
    template = "thai/cart.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)


# Sign up page

def signup_view(request):
    template = "account_signup.html"
    context = {'active_link': 'signup'}
    print('signup_view called')
    return render(request, template, context)


# Login page

def login_view(request):
    template = "account_login.html"
    context = {'active_link': 'login'}
    print('login_view called')
    return render(request, template, context)


# Success shown after order completion

def success_view(request):
    order = request.session['order']
    template = "thai/success.html"
    total = request.session.get('total')
    context = {'order': order, 'total': total}
    return render(request, template, context)
