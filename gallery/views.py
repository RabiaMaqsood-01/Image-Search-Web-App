
import requests
from django.shortcuts import redirect, render
from .api import fetch_pexels_photos
from .models import Favorite
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

def search_images(request):
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', '1'))
    request.session['last_query'] = query
    favorite_urls = list(Favorite.objects.values_list('image_url', flat=True))
    
    images = fetch_pexels_photos(query=query or None, page=page)

    return render(request, 'gallery/home.html', {
        'images': images,
        'favorite_urls': favorite_urls,
        'page': page,
        'query': query,
    })



@login_required
def save_favorite(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        alt_text = request.POST.get('alt_text')
        search_query = request.POST.get('search_query')
        image_index = request.POST.get('image_index')  # Get image index from form
        page = request.POST.get('page', '1')  # Default to 1 if not found

        Favorite.objects.create(image_url=image_url, alt_text=alt_text)

        if search_query and image_index:
            return redirect(f"/home/?q={search_query}&page={page}#img{image_index}")
        elif search_query:
            return redirect(f"/home/?q={search_query}&page={page}")
        else:
            return redirect('/home/')
    return redirect('/home/')   


def view_favorites(request):
    favorites = Favorite.objects.all()
    last_query = request.session.get('last_query', '')
    return render(request, 'gallery/favorites.html', {'favorites': favorites, 'last_query': last_query})

def delete_favorite(request, pk):
    fav = get_object_or_404(Favorite, pk=pk)
    fav.delete()
    return redirect('view_favorites')



def delete_by_url(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        search_query = request.POST.get('search_query')
        image_index = request.POST.get('image_index')
        page = request.POST.get('page', '1')

        Favorite.objects.filter(image_url=image_url).delete()

        if search_query and image_index:
            return redirect(f"/home/?q={search_query}&page={page}#img{image_index}")
        elif search_query:
            return redirect(f"/home/?q={search_query}&page={page}")
        else:
            return redirect('/home/')
        
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after register
            return redirect('/home/')
    else:
        form = UserCreationForm()
    return render(request, 'gallery/register.html', {'form': form})

def index_page(request):
    return render(request, 'gallery/index.html')