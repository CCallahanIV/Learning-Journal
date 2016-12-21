import pytest
from pyramid import testing


@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


@pytest.fixture
def test_app():
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_home_page_renders_has_right_variable():
    """Test that the home page renders file data."""
    from .views import home_page
    response = home_page(req)
    assert "bag_list" in response


def test_home_page_has_iterable():
    """Test that the home page view responds with iterable named bag_list."""
    from .views import home_page
    response = home_page(req)
    assert hasattr(response["bag_list"], "__iter__")

def test_home_page_has_list(test_app):
    """Functional test that home page has a list."""
    response = test_app.get("/", status=200) # status code is option - can test other responses?  e.g. 404
    inner_html = response.html
