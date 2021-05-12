import logging
import os

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse

from backend.search_api.models import Youtube
from backend.search_api.serializers import YoutubeSerializer

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(module)s [%(levelname)s] %(message)s')


def index(request):
    """
     Demo API for testing
    :param request:
    :return:
    """

    json_payload = {"message": "hello world!"}

    return JsonResponse(json_payload)


def get_videos(request):
    """
    A GET API which returns the stored video data in a paginated response sorted in descending order of published
    datetime.
    getvideos/?q=messi&page=1

    :param request:
    :return:
    """

    query_title = request.GET.get('q')
    query_desc = request.GET.get('desc')
    page_number = int(request.GET.get('page'))

    try:
        # search_results = Youtube.objects.raw(final_query, [query_title_string, query_desc_string])
        """
        Search the stored videos using their title and description
        """
        search_results = Youtube.objects.filter(title__icontains=query_title if query_title is not None else '', description__contains=query_title if query_title is not None else '').order_by(
            '-published_at'
        )

        '''
        Pagination
        '''
        paginator = Paginator(search_results, 25)
        page_obj = paginator.get_page(page_number)

        '''
        Serializing results using Django Rest Framework
        '''
        serialized_results = YoutubeSerializer(page_obj.object_list, many=True)

        return JsonResponse({"result": serialized_results.data, "total_page": paginator.num_pages})
    except Exception as e:
        logging.error(e)
        return JsonResponse({"success": "failed", "result": e})
