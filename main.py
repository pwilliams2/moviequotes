#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import os
from google.appengine.ext import ndb

import jinja2
import webapp2
from models import MovieQuote


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                               autoescape=True)

# Generic key to serve as parent
PARENT_KEY = ndb.Key("Entity", "moviequoute_root")

class MovieQuotesPage(webapp2.RequestHandler):
    def get(self):
        moviequotes_query = MovieQuote.query(ancestor=PARENT_KEY).order(-MovieQuote.last_updated)

        template = jinja_env.get_template("templates/index.html")
        self.response.write(template.render({"moviequotes_query": moviequotes_query}))

class AddQuoteAction(webapp2.RequestHandler):
    def post(self):
        entity_key = self.request.get('entity_key')
        # logging.info("key: " + entity_key)
        # logging.info("quote: " + self.request.get("quote"))

        if entity_key:
            logging.info("URL safe = " + entity_key)
            moviequote_key = ndb.Key(urlsafe=self.request.get("entity_key"))
            moviequote = moviequote_key.get()
            moviequote.quote = self.request.get("quote")
            moviequote.movie = self.request.get("movie")
            moviequote.put()
        else:
            new_movieQuote = MovieQuote(parent=PARENT_KEY,
                                quote=self.request.get("quote"),
                                movie=self.request.get("movie"))
            new_movieQuote.put()

        self.redirect(self.request.referer)

app = webapp2.WSGIApplication([
    ('/', MovieQuotesPage),
    ('/updatequote', AddQuoteAction)
], debug=True)
