from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Post
from .form import PostForm
from .forms import ContactForm
import os

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	if "post_edit" in request.POST:
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_test(request):
	form_class = ContactForm

	return render(request, 'blog/contact.html', {'form': form_class,})

def post_write(request):
	if 'contact' in request.POST:
		form = ContactForm(request.POST)

		if form.is_valid():
			code = form.cleaned_data['content']
			code = str(code)
			f = open('test.py','w')
			f.write(code)
			f.close()
			return render(request, 'blog/result.html', {'form': form})
	return render(request, '',)

def post_result(request):
	form = ContactForm
	content = get_object_or_404(form)
	return render(request, 'blog/result.html',{'form': content})