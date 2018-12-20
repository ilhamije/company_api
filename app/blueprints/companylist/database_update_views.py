""" this module contains the REST endpoint"""
# from models import Company_List, db
from app import db

import os
import json
import time

# import logging
# import logging.config
# import datetime
# from flask import jsonify

from app import Session
from models import Company_List


APP_ROOT = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
DATA_DIR = os.path.join(APP_ROOT, 'static/data')

json_file = DATA_DIR + '/company_index.json'
f = open(json_file, 'r')
company_data = json.load(f)


def return_existing_kode(kode):
    session = Session()
    check_if_present = session.query(Company_List).\
        filter(Company_List.company_code==kode).\
        scalar()
    session.close()
    return check_if_present


def data_processing(data, i):
    session = Session()
    existing_kode = return_existing_kode(kode=data[i]["company_code"])
    val = {
        "npwp": data[i].get('npwp', ''),
        "company_name": data[i].get('company_name', ''),
        "company_code": data[i].get('company_code', ''),
        "email": data[i].get('email', '').lower(),
        "phone": data[i].get('phone', ''),
        "fax": data[i].get('fax', ''),
        "address": data[i].get('address', ''),
        "website": data[i].get('website', ''),
        "business": data[i].get('business', ''),
        "sector": data[i].get('sector', ''),
        "url": data[i].get('url', ''),
        "crawled_on": data[i].get('crawled_on', ''),
    }

    kode = data[i]["company_code"]
    if existing_kode:
        existing_company = Company_List.query.filter_by(company_code=kode)
        existing_company.update(val)
        try:
            session.commit()
            res = ("data UPDATED : " + str(kode))
            print (res)
            print (val)
            # return/yield counter

        except Exception as e:
            print("data updating FAILED" + str(kode))

    else:
        new_company = Company_List(**val)
        session.add(new_company)
        try:
            session.commit()
            print ("data ADDED : " + str(kode))
            print (val)
            # return/yield counter
        except Exception as e:
            print("data adding FAILED" + str(kode))
            print (e.message)


def main_update():
    """Main loop of the script, to interate data data_processing for each company."""
    session = Session()
    timer_count = 0
    for i in range(len(company_data)):
        timer_count += 1
        print (timer_count)
        # count all yield
        data_processing(company_data, i)
        time.sleep(2)

    session.close()
    # return all statistik
    return ("DONE")
    # logger.info("---END---")
