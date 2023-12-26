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
    product = get_object_or_404(Products, id=pk)
    review = Review.objects.filter(product=pk)
    if request.method == 'POST':
        formr = ReviewForm(request.POST)
        if formr.is_valid():
            form = formr.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect(products_detail, pk)
    else:
        form = ReviewForm()
    return render(request, 'products/products_detail.html', {'product':product, 'reviews':review, 'form':form})


# @login_required
# def add_rating(request, pk):
#     product = get_object_or_404(Products, pk=pk)
#     if request.method == 'POST':
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             rating = form.save(commit=False)
#             rating.product = product
#             rating.user = request.user
#             rating.save()
#             return redirect('products_detail', pk=product.pk)
#     else:
#         form = RatingForm()
#     return render(request, 'add_rating.html', {'form': form})