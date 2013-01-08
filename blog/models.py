from django.db import models
from mongoengine import *

class Post( Document ):
    title = StringField( max_length=500 )
    text = StringField( max_length=5000 )
    comments = ListField( EmbeddedDocumentField('Comment') )
    tags = ListField( StringField(max_length=50) )

    def __unicode__( self ):
        return self.title

class Comment( EmbeddedDocument ):
    text = StringField( max_length=500 )

    def __unicode__( self ):
        return self.text[:100]+"..."
