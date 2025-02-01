from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from django.db.models import Q
from goods1.models import products


def q_search(query_set):
    if query_set.isdigit() and len(query_set) <= 5:
        return products.objects.filter(id=int(query_set))

    vector = SearchVector("name", "description")
    query_set = SearchQuery(query_set)

    result =(
        products.objects.annotate(rank=SearchRank(vector, query_set))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query_set,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query_set,
            start_sel='<span style="background-color: green;">',
            stop_sel="</span>",
        )
    )
    
    return result
    # return products.objects.annotate(search=SearchVector("name", "description")).filter(search=query_set)
    # keywords = [word for word in query_set.split() if len(word) > 2 ]

    # q_objects =Q()

    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
