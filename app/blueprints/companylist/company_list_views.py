""" this module contains the REST endpoint"""
# import logging
# import datetime
# import json
from flask import jsonify, request
# from app import Session
from models import Company_List


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
        companylist = Company_List.query.all()
        results = []
        for i in companylist:
            obj = {
                'id': i.id_company_list,
                'company_url': i.url,
                'company_name': i.company_name,
                'company_email': i.email,
                'company_description': i.business,
                'company_phone_number': i.phone,
                'industry': i.sector,
            }
            results.append(obj)
        total = len(results)
        return jsonify({
            "status_code": 200,
            "message": "Successful",
            "data": results,
            "total": total})
