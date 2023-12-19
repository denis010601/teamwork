from django.views.generic import DetailView, TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Products, Review, Rating
from .forms import ReviewForm, RatingForm

class ProductListView(ListView):
    model = Products
    # template_name = 'products/products_list.html'

class ProductDetailView(DetailView):
    model = Products

def products_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    reviews = product.reviews.all()
    ratings = product.ratings.all()
    average_rating = ratings.aggregate(models.Avg('value'))['value__avg']
    if average_rating:
        average_rating = round(average_rating, 1)
    review_form = ReviewForm()
    rating_form = RatingForm()
    return render(request, 'products_detail.html', {
        'product': product,
        'reviews': reviews,
        'ratings': ratings,
        'average_rating': average_rating,
        'review_form': review_form,
        'rating_form': rating_form,
    })

@login_required
def add_review(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('products_detail.html', pk=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

@login_required
def add_rating(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.product = product
            rating.user = request.user
            rating.save()
            return redirect('products_detail', pk=product.pk)
    else:
        form = RatingForm()
    return render(request, 'add_rating.html', {'form': form})