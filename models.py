
'''
@author: pwilliams
'''

from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class MovieQuote(EndpointsModel):
    """ A movie quote and the movie title   """
    _message_fields_schema = ("entityKey", "quote", "movie", "last_updated")
    quote = ndb.StringProperty()
    movie = ndb.StringProperty()
    last_updated = ndb.DateTimeProperty(auto_now=True)



