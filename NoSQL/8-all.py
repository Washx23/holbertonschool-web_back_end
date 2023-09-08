#!/usr/bin/env python3
""" documents"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """ document list all"""
    list = []
    result = mongo_collection.find()
    if mongo_collection.count_documents({}) < 1:
        return list
    else:
        return result