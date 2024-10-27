from django.urls import path
from Spotify_Wrapped import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),  # Signup form
    path('login/', views.login_view, name='login'),  # Login form
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard after login/signup
    path('link_account/', views.link_spotify, name='link_account'),
    # path('logout/', views.logout_view, name='logout'),  # Logout view
    path('spotify-auth/', views.spotify_auth, name='spotify_auth'), # Spotify OAuth
    path('callback/', views.spotify_callback, name='spotify_callback'),
    path('link_error/', views.error_page, name='error_page'),
    path('contact_dev/', views.contact_dev, name='contact_dev')
]