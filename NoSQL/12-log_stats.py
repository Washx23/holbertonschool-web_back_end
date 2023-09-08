#!/usr/bin/env python3
"""   Documents  """


from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client['logs']
collection = db['nginx']

total_logs = collection.count_documents({})

http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents
                 ({"method": method}) for method in http_methods}

status_endpoint_count =
collection.count_documents({"method": "GET", "path": "/status"})

print(f"Total logs: {total_logs} logs")
print("Methods:")
for method in http_methods:
    print(f"\t{method}: {method_counts[method]} logs")
print(f"GET method with path=/status: {status_endpoint_count} logs")

client.close()
