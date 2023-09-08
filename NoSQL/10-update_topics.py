#!/usr/bin/env python3
"""documents  """


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """documents update_topics"""
    filter_query = {"name": name}
    update_operation = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(filter_query, update_operation)
    return result
