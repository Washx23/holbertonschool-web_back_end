#!/usr/bin/env python3
"""   Documents  """


def schools_by_topic(mongo_collection, topic):
    """ documents schools_by_topic"""
    list = []
    for idx in mongo_collection.find({"topics": topic}):
        list.append(idx)
    return list
