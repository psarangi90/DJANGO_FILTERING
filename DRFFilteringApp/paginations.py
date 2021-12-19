from rest_framework.pagination import PageNumberPagination
class WFMTPaginate(PageNumberPagination):
    page_size=10
    page_query_param="wfmtpage"
    page_size_query_param="wfmt_size"
    max_page_size=15
    last_page_strings=("last",)
    