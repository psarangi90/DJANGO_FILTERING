from rest_framework.filters import BaseFilterBackend
class WFMTFilterClass(BaseFilterBackend):
    def filter_queryset(self, request ,queryset,view):
        trs=request.query_params.get("trs")
        if trs is not None:
            queryset=queryset.filter(trs__istartswith=trs)
        return queryset
            