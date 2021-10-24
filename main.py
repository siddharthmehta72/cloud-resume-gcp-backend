from google.cloud import firestore
from flask import Flask, jsonify
import json
db = firestore.Client()

def getset_counter(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)
    request_json = request.get_json()
    #db_ref = db.collection(u'visitcount')
    counter_ref = db.collection(u'visitcount').document(u'oBJ7ounXMtpahGzfeXOe')
    #docs = db_ref.stream()
    #visitcounters = []
    #for doc in docs:
    #    visitcounter = doc.to_dict()
    #    visitcounters.append(visitcounter)
        # render the template
    #return scientist
    #json_object = json.dumps(visitcounters, indent = 2) 
    #return json_object
    counter_ref.update({u'count': firestore.Increment(1)})
    doc = counter_ref.get()
    response = jsonify(doc.to_dict())
    headers = {
        'Access-Control-Allow-Origin': 'https://siddharthmehta.in'
    }
    return (response, 200, headers)
