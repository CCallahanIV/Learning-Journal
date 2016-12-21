"""Views for the Pyramid Learning Journal app."""

from pyramid.view import view_config
import io
import os

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Entry 1", "id": 1, "creation_data": "Dec 20, 2016", "body": "I learned some stuff about some stuff."},
    {"title": "Entry 1", "id": 2, "creation_data": "Dec 20, 2016", "body": "I learned some stuff about some stuff."},
    {"title": "Entry 1", "id": 3, "creation_data": "Dec 20, 2016", "body": "I learned some stuff about some stuff."}
]


@view_config(route_name="home", renderer="templates/list.jinja2")
def home_page(request):
    """View for the home page."""
    all_my_stuff = ["pens", "book", "laptop", "other stuff", "bubbgle gum"]
    return {"bag_list": all_my_stuff}


@view_config(route_name="detail", renderer="string")
def detail_view(request):
    """Handle the detail view for a specific journal entry."""
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry": entry}


@view_config(route_name="create", renderer="string")
def create_view(request):
    """Handle the view for creating a new entry."""
    file_path = os.path.join(HERE, "templates", "create_entry.html")
    file_data = io.open(file_path).read()
    return file_data


@view_config(route_name="update", renderer="update")
def update_view(request):
    """Handle the view for updating a new entry."""
    file_path = os.path.join(HERE, "templates", "edit_entry.html")
    file_data = io.open(file_path).read()
    return file_data
