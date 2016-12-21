"""Views for the Pyramid Learning Journal app."""

from pyramid.view import view_config
import io
import os

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"id": 0, "title": "There's value in stepping back.", "creation_date": "December 14, 2016", "body": """Sometimes principles from our past help with our present. Before starting the double linked list today, I committed to two things:

Starting with the tests.
Designing before coding.
I actually wrote some tests first, just sort of stream of consciousness but things quickly got messy. After flailing for a bit, I stepped back and mapped out the function of each method and made a list of everything I would want test about it. From that, I was able to write a fairly comprehensive testing suite that should require little refactoring to really test all functions of the Double Linked List.

Joey and I had some frustrating issues to work out with the server assignment. For whatever reason, since yesterday, our message sending on both the client and server sides decided to start escaping all the \r and \n characters. It had us and the TA's stumped for... far too long. We ended up changing our search parameters in our receiving while loops so that things could work again. Now I'm worried that I'll wake up tomorrow and it won't work. Or it just won't work whomever grades our assignment.

SUCH IS LIFE."""},
    {"id": 1, "title": "Revenge is Best SERVERED Cold", "creation_date": "December 15, 2016", "body": """The second you feel like youre starting to climb youre way out of the avalanche of work and information theres always some weird and random server error to pull you right back in.  Im struggling a lot to find ways to refactor and clean up the server code. I feel like were working with a patchwork of try/except statements, teetering towers of if/else logic, and precarious while loops.
Id like to see an example of a server done RIGHT. But I want to earn that - I want to finish my own server the hard way.Hey, urllib2, sup?"""},
    {"id": 2, "title": "Whiteboarding", "creation_date": "December 16, 2016", "body": "Its fun, its hard, it makes your brain bend in ways you never thought possible. Really lucky I was partnered with Joey. He had the essential, Aha! moment that led to the solution. Glad I was able to contribute though. I worry that in the future as I prep for interviews, I'll won't be able to rely on flexible thinking to solve new problems. I'll likely have to plan ahead and try to expose myself to as many problem scenarios as possible in order to succeed. So it goes, more studying ahead.  The server assignment really started as a hacky mess. Lots of patchwork try/except blocks and grabbing specific errors in desperation. I think today we really nailed it down into something I can be somewhat proud of. Looking forward to the opportunity to go back in time and refactor things this weekend.  Also looking forward to beer."},
    {"id": 3, "title": "Recent Awesome Things We've Learned", "creation_date": "December 19th, 2016", "body": """<ul>
                        <li>Big(O) Notation</li>
                        <li>Linked-List based Data Structures</li>
                        <li>Web App Deployment Frameworks (Pyramid)</li>
                    </ul>
                    <p>It feels like we're moving beyond the introductory part of Python knowledge and are really starting to get into the meat n' potatoes of development and CS concepts. For the first time in a while, I'm starting to feel somewhat empowered as a dev-in-development.  Not to say I know everything there is, but I know enough to now to actually make something with it, and more importantly, I'm starting to have some idea of what I don't know.</p>

                    <p>Despite the time crunch and the fast pace, I've enjoyed the class to this point.  BUT, I am really excited for what is to come.</p>

                    <p>Of course, the second I begin to think this, the rug will be pulled out from underneath once again.</p>

                    <p>Looking forward to building stuff.</p>"""},
    {"id": 4, "title": "Tunnels, Lights, Progress, etc.", "creation_date": "December 20th, 2016", "body": """Two quick things, the binary heap was initially a pain in the ass.  However, I feel really proud of the implementation I have.  Hooray for max OR min.
    Finally, I'm really excited for the group project.  I feel a strong personal connection to the purpose of this app and I'm excited to put our newfound skills and knowledge to good use."""}
]


@view_config(route_name="home", renderer="templates/list.jinja2")
def home_page(request):
    """View for the home page."""
    return {"entries": ENTRIES}


@view_config(route_name="detail", renderer="templates/entry.jinja2")
def detail_view(request):
    """Handle the detail view for a specific journal entry."""
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry": entry}


@view_config(route_name="create", renderer="templates/create_entry.jinja2")
def create_view(request):
    """Handle the view for creating a new entry."""
    return {}


@view_config(route_name="update", renderer="templates/edit_entry.jinja2")
def update_view(request):
    """Handle the view for updating a new entry."""
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry": entry}
