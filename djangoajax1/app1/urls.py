from django.urls import path


urlpatterns = [
    path('', show_time, name='show_time'),
    path('time/', get_current_time, name='get_current_time'),
    # Other URL patterns
]