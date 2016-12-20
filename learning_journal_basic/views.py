"""Views for the Pyramid Learning Journal app."""

from pyramid.response import Response
import io
import os

HERE = os.path.dirname(__file__)


def home_page(request):
    """View for the home page."""
    file_path = os.path.join(HERE, "templates", "index.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def detail_view(request):
    """Handle the detail view for a specific journal entry."""
    file_path = os.path.join(HERE, "templates", "entry.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def create_view(request):
    """Handle the view for creating a new entry."""
    file_path = os.path.join(HERE, "templates", "create_entry.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def update_view(request):
    """Handle the view for updating a new entry."""
    file_path = os.path.join(HERE, "templates", "edit_entry.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    """Set up views with routes."""
    config.add_view(home_page, route_name="home")
    config.add_view(detail_view, route_name="detail")
    config.add_view(create_view, route_name="create")
    config.add_view(update_view, route_name="update")
