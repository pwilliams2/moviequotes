__author__ = 'pwilliams'

import endpoints
import protorpc

from models import MovieQuote
import main

@endpoints.api(name="moviequotes", version="v1", description="Movie Quotes API")
class MovieQuotesApi(protorpc.remote.Service):
    """ API for the CRUD methods """
    pass

    @MovieQuote.method(name="moviequote.insert", path="movieqoute/insert", http_method="POST")
    def moviequote_insert(self, request):
        """ insert or update """
        if request.from_datastore:
            mq = request
        else:
            mq = MovieQuote(parent=main.PARENT_KEY, quote=request.quote, movie=request.movie)

        mq.put()
        return mq

    @MovieQuote.method(request_fields=("entityKey",),name="moviequote.delete", path="movieqoute/delete/{entityKey}", http_method="DELETE")
    def moviequote_delete(self, request):
        """ Delete quote, if exists """
        if not request.from_datastore:
            raise endpoints.NotFoundException("Movie quote to be deleted was not found")

        request.key.delete()
        return MovieQuote(quote="delete")

    @MovieQuote.query_method (query_fields=("limit", "order","pageToken"), name="moviequote.list", path="movieqoute/list", http_method="GET")
    def moviequote_list(self, query):
         """ get all the quotes """
         return query


app = endpoints.api_server([MovieQuotesApi], restricted=False)



