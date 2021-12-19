from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import WFMTModel
from .serializers import WFMTModelSerializer
from .paginations import WFMTPaginate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .filters import WFMTFilterClass

# Create your views here.
class WFMTListView(ListAPIView):
    serializer_class=WFMTModelSerializer
    pagination_class=WFMTPaginate
    queryset = WFMTModel.objects.all()

    '''This is Similar to Seach Backend But the Only Differenrce is here is field wise we can search in the Browsable API'''
     
     #*****DJANGO FILTER BACKEND **********#
     
    # filter_backends=[DjangoFilterBackend,]
    # filterset_fields=['trs','id']
    
    '''Here we can't mention the fields on the browsable API But we can mention those fields inside seach_fields  list/tuple'''
    
    #*****SEARCH FILTER BACKEND **********#

    # filter_backends=[SearchFilter,]
    # search_fields=["=id","^trs"]
    
     #*****ORDERING FILTER BACKEND **********#
    
    filter_backends=[OrderingFilter,]
    ordering_fields=["cp_number",'sne_id',"scheme_number","trs"]
    ordering=['cp_number','-trs']
    
     #*****CUSTOM FILTER BACKEND **********#
    filter_backends=[WFMTFilterClass,]
    
    ##PlAIN VANILA WAY OF SEARCHING##
    
    # def get_queryset(self):
    #     # queryset = self.get_queryset
    #     queryset = WFMTModel.objects.all()
    #     # trs=self.request.GET.get('trs')#1st approach
    #     # trs=self.kwargs.get('trs')#2nd approch
    #     trs=self.request.query_params.get('trs')
    #     print(trs)
    #     if trs is not None:
    #         queryset = queryset.filter(trs__icontains=trs)
    #     return queryset


class EmpRetrieve(RetrieveAPIView):
    serializer_class=WFMTModelSerializer
    queryset = WFMTModel.objects.all()
    filter_backends=[DjangoFilterBackend,]
    filterset_fields=['trs','id']
    # filter_backends=[SearchFilter,]
    # search_fields=["id","cp_number",'sne_id',"scheme_number","trs"]
    