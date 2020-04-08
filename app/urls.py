from django.urls import path
from .views import google_sheet_views,github_report_views

urlpatterns = [

    path('v1/world/report/',github_report_views.ReportView.as_view()),
    path('v1/nation/<str:country>/',github_report_views.CountrysTotalReportView.as_view()),
    path('v1/total/report/',github_report_views.WorldReport.as_view()),
    path('v2/world/report/', google_sheet_views.NationsReport.as_view()),
    path('v2/nation/<str:country>/', google_sheet_views.CountrysTotalReport.as_view()),
    path('v2/total/report/', google_sheet_views.TodaysReport.as_view()),
    path('v2/daily/<str:country>/',google_sheet_views.CountrysDailyReport.as_view())

]