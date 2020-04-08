from bs4 import BeautifulSoup
import requests
from datetime import datetime,timedelta
from rest_framework import views
from rest_framework.response import Response
from ..serializers import ReportSerializer
from ..utils import helper



class CountrysDailyReport(views.APIView):

    def get(self,requests,country):
        nation = country.upper()

        result = helper.getDailyReportForCountry(nation)

        final_res = ReportSerializer(result,many=True).data

        return Response(final_res)




class CountrysTotalReport(views.APIView):
    
    def get(self,requests,country):
        
        report = helper.getReport(country.upper())

        results = ReportSerializer(report,many=True).data

        return Response(results)


class NationsReport(views.APIView):
    
    def get(self,requests):
        
        all_reports = helper.getReport("")

        results = ReportSerializer(all_reports,many=True).data

        return Response(results)


class TodaysReport(views.APIView):

    def get(self,requests):
        
        report = helper.getTodaysReport()

        results = ReportSerializer(report,many=True).data

        return Response(results)




