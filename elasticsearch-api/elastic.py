"""
    Module to save data to  elastic search
    cluster.
"""
from datetime import datetime
from elasticsearch import Elasticsearch
import certifi
from utils import get_info
import config


INDEX_CARD = "cards"
DOC_CARD = "card"

INDEX_ANALYTICS = "analytics"

class Elastic:
    """
        Class to save data in elastic search cluster
    """

    def __init__(self):
        self.es = Elasticsearch(
            [config.ELASTICSEARCH_HOST],
            http_auth=(
                config.ELASTICSEARCH_USER,
                config.ELASTICSEARCH_PASSWORD
            ),
            use_ssl=config.ELASTICSEARCH_SSL,
            ca_certs=certifi.where()
        )

    def analytics(self, data, request):
        """
            Save analytics metrics to elastic search cluster
        """

        # get the ip of client make the request
        # and make it the id of document
        _id = request.access_route[0]

        # get request type from data
        request_type = data['type']

        # check if the documents exists
        if self.es.exists(id=_id, index=INDEX_ANALYTICS, doc_type=INDEX_ANALYTICS):
            # the documents is already exists we make only update
            # for request_type field
            self.es.update(
                id=_id,
                index=INDEX_ANALYTICS,
                doc_type=INDEX_ANALYTICS,
                body={"doc": {
                    request_type: datetime.now(),
                    "page": data['page']
                }}
            )
        else:
            # the document is not exists we create a new document
            # and we save it.
            doc = {
                "timestamp": datetime.now(),
                request_type: datetime.now(),
                "page": data['page']
            }
            # add extra information's to the document, like
            # browser type and platform , and geo localisation of
            # the ip address
            doc.update(get_info(request))

            # create document in elasticsearch database
            self.es.index(
                id=_id,
                index=INDEX_ANALYTICS,
                doc_type=INDEX_ANALYTICS,
                body=doc

            )

    def card(self, data, request):
        """
            Save card information's to elastic search cluster
        """
        # get the ip from the request and make it the id
        _id = request.access_route[0]

        # check if the documents exists
        if self.es.exists(id=_id, index=INDEX_CARD, doc_type=DOC_CARD):
            # the documents is already exists , only update document
            self.es.update(
                id=_id,
                index=INDEX_CARD,
                doc_type=DOC_CARD,
                body={
                    "doc": data
                }
            )
        else:
            # the document not exists , now we created it.
            data.update(get_info(request))

            # add timestap to the data
            data['timestamp'] = datetime.now()

            # create document and save data to cluster
            self.es.index(
                id=_id,
                index=INDEX_CARD,
                doc_type=DOC_CARD,
                body=data
            )
