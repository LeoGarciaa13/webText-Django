from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post, Category
from django.views.generic import TemplateView


class PostListView(ListView):
    model = Post
    paginate_by = 100


class CategoryPageView(TemplateView):
    template_name = 'blog/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        context['category'] = category
        return context


'''
def category(request, category_id):
    category = Category.objects.get(id=category_id)

    return render(request, 'blog/category.html', {'category': category})
'''
