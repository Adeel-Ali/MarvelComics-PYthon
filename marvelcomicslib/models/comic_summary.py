# -*- coding: utf-8 -*-

"""
    marvelcomicslib.models.comic_summary
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 09/23/2016
"""
from .base_model import BaseModel

class ComicSummary(BaseModel):

    """Implementation of the 'ComicSummary' model.

    TODO: type model description here.

    Attributes:
        name (string): The canonical name of the comic.
        resource_uri (string): The path to the individual comic resource.

    """

    def __init__(self, 
                 name = None,
                 resource_uri = None):
        """Constructor for the ComicSummary class"""
        
        # Initialize members of the class
        self.name = name
        self.resource_uri = resource_uri

        # Create a mapping from Model property names to API property names
        self.names = {
            "name" : "name",
            "resource_uri" : "resourceURI",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            name = dictionary.get("name")
            resource_uri = dictionary.get("resourceURI")
            # Return an object of this model
            return cls(name,
                       resource_uri)
