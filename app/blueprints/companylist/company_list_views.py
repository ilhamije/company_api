""" this module contains the REST endpoint"""
# import logging
# import datetime
import json
from flask import jsonify, request, make_response

from models import db, Company_List


def index():
    return jsonify({'Message': "This is not the droid you are looking for."})


def get_companies():
    if request.args:
        companyname = request.args.get('company_name')
        industry = request.args.get('industry')
        # print (industry)
        if companyname:
            return jsonify({
                "status_code": 200,
                "message": "Will returning Company data based on name"})
        elif industry:
            return jsonify({
                "status_code": 200,
                "message": "Will returning Company data based on industry"})
        else:
            return jsonify({
                "status_code": 404, "message": "Not found"})
    else:
        return jsonify({
                "status_code": 200,
                "message": "We're gonna give you all data here"})
