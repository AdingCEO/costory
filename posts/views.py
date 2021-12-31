# from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator
from django.views import View
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm
# Create your views here.

# def post_list(request):
#     posts=Post.objects.all()
#     paginator=Paginator(posts,6)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'posts/post_list.html', {'page':page})

class PostListView(ListView):
    model = Post
    # template_name = 'posts/post_list.html'  #모델명_list 가 기본값
    # context_object_name = 'posts' #object_list 를 posts 로 써도 되게 해줌
    ordering = ['-dt_created'] #최신순 리스트 정렬
    paginate_by = 6
    # page_kwarg = 'page' #'page'가 기본값


# def post_detail(request,post_id):
#     post = get_object_or_404(Post, id=post_id)
#     context={'post':post}
#     return render(request, 'posts/post_detail.html',context=context)

class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post_detail.html' #모델명_detail이 기본값
    # pk_url_kwarg = 'post_id' #detail url에서 받아오는 key #'pk'가 기본값
    # context_object_name = 'post' #모델명 소문자로 적은것이 기본값


# 함수형 view
# def post_create(request):
#     if request.method =='POST':
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)           
#     else:
#         post_form = PostForm()
#     return render(request, 'posts/post_form.html', {'form':post_form})

# 클래스형 view
# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form':post_form})
    
#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)
#         return render(request, 'posts/post_form.html', {'form':post_form})

# 제네릭 view
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm #form이라는 키워드로 템플릿에 context 자동으로 전달됨
    # template_name = 'posts/post_form.html' #post_form.html이 기본값
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.id})

        
# def post_update(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method=='POST':
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)
#     else:
#         post_form=PostForm(instance=post)
#     return render(request, 'posts/post_form.html', {'form':post_form})

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm #form이라는 키워드로 템플릿에 context 자동으로 전달됨
    # template_name = 'posts/post_form.html' #모델명_form.html이 기본값
    # pk_url_kwarg = 'pk'
    
    def get_success_url(self):
        return reverse ('post-detail', kwargs={'pk':self.object.id}) #detail 페이지로 이동하기 위한 id


# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method=='POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', {'post':post})

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html' #모델명_confirm_delete.html이 기본값
    # pk_url_kwarg = 'pk'
    # context_object_name = 'post' #해당 id에 데이터 있으면 'post' context에 담아서 보내줌
    
    def get_success_url(self):
        return reverse('post-list')
    
    
# def index(request):
#     return redirect('post-list')

class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'

    