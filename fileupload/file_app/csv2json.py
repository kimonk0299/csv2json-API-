import csv 
import json
from django.http import HttpResponse
from django.http import JsonResponse

def convert2json(location):
    data = [] 

    with open(location) as f:
        reader = csv.DictReader(f,delimiter=',')
        for row in reader:
            if not row["response"]:
                continue

            chips = row["chips"].split('|')
            row["chips"] = []
            for chip in chips:
                row["chips"].append({"icon": "", "title": chip})          

            data.append(row)
    
    jsonobject = json.dumps(data, indent= 4)
    return (jsonobject)