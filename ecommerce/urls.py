from django.contrib import admin
from django.urls import include, path
import electronics.urls
import fashion.urls
import groceries.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(electronics.urls)),
    path('electronics/',include(electronics.urls)),
    path('fashion/',include(fashion.urls)),
    path('groceries/',include(groceries.urls)),
    
]
