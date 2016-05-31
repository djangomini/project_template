"""Auto-detect all urls, based on "controllers" directory."""
from djangomini.urls import auto_discover


urlpatterns = auto_discover()
