from django.urls import path

from . import SARIMA
from . import WGAUSS
from . import views
from .analysis import seasonality

urlpatterns = [
    path('SARIMA', SARIMA.AD_SARIMA.as_view(), name='SARIMA'),
    path('ADWindowedStats', WGAUSS.ADWindowedStats.as_view(), name='ADWindowedStats'),
    path('read-data', views.ReadUploadedData.as_view(), name='read-data'),
    path('import-data', views.ImportData.as_view(), name='import-data'),
    path('analysis/CheckSeasonality', seasonality.CheckSeasonality.as_view(), name='CheckSeasonality')
]