from django.contrib import admin
from django.urls import path, include
from shop import views
from django.contrib.auth.models import User # Superuser banane ke liye

# --- Temporary Admin Creator ---
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
except Exception:
    pass
# -------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    # Agar cart ya orders ki urls hain toh wo bhi yahan include honi chahiye
]
