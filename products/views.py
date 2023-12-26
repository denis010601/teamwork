from django.views.generic import DetailView, TemplateView, ListView, CreateView
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
    review = Review.objects.all()
    print(product)
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
    return render(request, 'products/products_detail.html', {'product':product,  'formr':form})

class RatingCreateView(CreateView):
    model = Rating
    form_class = RatingForm
    template_name = 'products/products_detail.html'
    success_url = '/'