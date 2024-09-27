from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CustomUserCreationForm, VideoForm, CommentForm
from .models import Video, Comment

def signup(request):
    try:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('login')  # Redirect to the login page after signup
        else:
            form = CustomUserCreationForm()  # Use your custom form here
        return render(request, 'signup.html', {'form': form})
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'signup.html', {'form': form, 'error': str(e)})

@login_required
def home_view(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})

@login_required
def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    comments = video.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.video = video
            comment.user = request.user
            comment.save()
            return redirect('video_detail', video_id=video.id)
    else:
        comment_form = CommentForm()

    return render(request, 'video_detail.html', {'video': video, 'comments': comments,'comment_form': comment_form})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video =form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, 'Video added successfully!')
            return redirect('home')
    else:
        form = VideoForm()

    return render(request, 'add_video.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    messages.success(request, 'Video deleted successfully!')
    return redirect('home')

@user_passes_test(lambda u: u.is_superuser)
@login_required
def edit_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video edited successfully!')
            return redirect('video_detail', video_id=video.id)
    else:
        form = VideoForm(instance=video)

    return render(request, 'edit_video.html', {'form': form, 'video': video})

def login_view(request):
    return render(request, 'login.html')
