from pyramid.response import Response
import io
import os

HERE = os.path.dirname(__file__)


def home_page(request):
    """View for the home page."""
    file_path = os.path.join(HERE, "data", "sample.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    config.add_view(home_page, route_name="home")