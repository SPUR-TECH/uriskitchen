from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal, Dessert, Comment, DessertComment
from .forms import CommentForm, DessertCommentForm


def home_view(request):
    """Home page view function
    """
    return render(request, "thai/index.html")


class mealDetailView(DetailView):
    """Meal detail view shows comments and edit buttons
    """
    model = Meal
    context_object_name = 'meal'

    def get_context_data(self, **kwargs):
        """ receives and filters the comment data
        """
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(meal=self.object)
        return context


def meal_view(request):
    """Meal view shows Meal menu page
    """
    request.session.set_expiry(0)
    template = "thai/meal.html"
    meal_objects = Meal.objects.all()
    context = {
        'meal_objects': meal_objects, 'active_link': 'meal'}
    return render(request, template, context)


class dessertDetailView(DetailView):
    """dessert detail view displays the details and comments
        of the dessert selected
    """
    model = Dessert
    context_object_name = 'dessert'

    def get_context_data(self, **kwargs):
        """ receives and filters the comment data
        """
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['comments'] = DessertComment.objects.filter(
            dessert=self.object)
        return context


def dessert_view(request):
    """Dessert view shows Dessert menu page
    """
    request.session.set_expiry(0)
    template = "thai/dessert.html"
    dessert_objects = Dessert.objects.all()
    context = {
        'dessert_objects': dessert_objects, 'active_link': 'dessert'}
    return render(request, template, context)


class commentCreateView(LoginRequiredMixin, CreateView):
    """Meal comments form
    """
    model = Comment
    context_object_name = 'comment'
    form_class = CommentForm

    def form_valid(self, form):
        """Assign Primary Key if form is valid
        """
        form.instance.meal = Meal.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to Meal Detail page
        """
        pk = self.kwargs['pk']
        return reverse_lazy('meal_detail', kwargs={'pk': pk})


class commentUpdateView(LoginRequiredMixin, UpdateView):
    """Meal comments editing function
    """
    model = Comment
    context_object_name = 'comment'
    form_class = CommentForm

    def get_success_url(self):
        """Redirect to Meal Detail page
        """
        pk = self.kwargs['id']
        return reverse_lazy('meal_detail', kwargs={'pk': pk})


class commentDeleteView(LoginRequiredMixin, DeleteView):
    """Meal comments deleting function
    """
    model = Comment
    context_object_name = 'comment'

    def get_success_url(self):
        """Redirect to Meal Detail page
        """
        pk = self.kwargs['id']
        return reverse_lazy('meal_detail', kwargs={'pk': self.object.meal.pk})


class dessertCommentCreateView(LoginRequiredMixin, CreateView):
    """Dessert comments form
    """
    model = DessertComment
    context_object_name = 'comment'
    form_class = DessertCommentForm

    def form_valid(self, form):
        """Assign Primary Key if form is valid
        """
        form.instance.dessert = Dessert.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to Dessert Detail page
        """
        pk = self.kwargs['pk']
        return reverse_lazy('dessert_detail', kwargs={'pk': pk})


class dessertCommentUpdateView(LoginRequiredMixin, UpdateView):
    """Dessert comments editing function
    """
    template = "thai/dessertcomment_update.html"
    model = DessertComment
    context_object_name = 'comment'
    form_class = DessertCommentForm

    def get_success_url(self):
        """Redirect to Dessert Detail page
        """
        pk = self.kwargs['id']
        return reverse_lazy('dessert_detail', kwargs={
            'pk': self.object.dessert.pk})


class dessertCommentDeleteView(LoginRequiredMixin, DeleteView):
    """Dessert comments delete function
    """
    model = DessertComment
    context_object_name = 'comment'

    def get_success_url(self):
        """Redirect to Dessert Detail page
        """
        pk = self.kwargs['id']
        return reverse_lazy('dessert_detail', kwargs={
            'pk': self.object.dessert.pk})


@csrf_exempt
def cart_view(request):
    """Cart view displays the shopping cart page
    """
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['order'] = request.POST.get('orders')
    template = "thai/cart.html"
    context = {'active_link': 'cart'}
    return render(request, template, context)


def signup_view(request):
    """Sign up view function displays the sign up page
    """
    template = "account_signup.html"
    context = {'active_link': 'signup'}
    print('signup_view called')
    return render(request, template, context)


def login_view(request):
    """Login view function displays the Login page
    """
    template = "account_login.html"
    context = {'active_link': 'login'}
    print('login_view called')
    return render(request, template, context)


def success_view(request):
    """Success view function displays the Success page
    """
    order = request.session['order']
    template = "thai/success.html"
    total = request.session.get('total')
    context = {'order': order, 'total': total}
    return render(request, template, context)
