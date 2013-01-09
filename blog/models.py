from django.db import models
from mongoengine import *
# The above import gives us all of these Field types, as well as Document and EmbeddedDocument.

class Post( Document ):
    title = StringField( max_length=500 )
    text = StringField( max_length=5000 )

    # Comments are EMBEDDED within Posts. No second query needed.
    comments = ListField( EmbeddedDocumentField('Comment') )
    tags = ListField( StringField(max_length=50) )

    def __unicode__( self ):
        return self.title

class Comment( EmbeddedDocument ):
    '''
    Note that Comments are not actually stored in the database by themselves. They are
    embedded within Posts.
    '''
    text = StringField( max_length=500 )

    def __unicode__( self ):
        return self.text[:100]+"..."
