"""Routes for the Learning Journal app."""


def includeme(config):
    """All of the routes for the configuration to find."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route("home", "/")
    config.add_route("detail", "/journal/entry")
    config.add_route("create", "/journal/new-entry")
    config.add_route("update", "/journal/edit")
