from django.urls import path
from .views import TemplateViews,post_detail, category
from django.conf.urls.static import static
from django.conf import settings


from . import views
urlpatterns = [
	path('', TemplateViews.as_view(), name='index'),	
	path('postdetail/<int:news_id>/',views.post_detail,name='post_detail'),
	path('category/<int:category_id>/',views.category,name="category"),
]
if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,
		document_root = settings.MEDIA_ROOT)

