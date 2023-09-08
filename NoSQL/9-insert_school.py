#!/usr/bin/env python3
"""documents"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ documents insert_school """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
