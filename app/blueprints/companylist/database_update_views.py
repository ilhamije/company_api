""" this module contains the REST endpoint"""
from models import Company_List, db

import os
import json
import time

import logging
import logging.config
# import datetime
from flask import jsonify

# from models import db, Company_List


APP_ROOT = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
DATA_DIR = os.path.join(APP_ROOT, 'static/data')

json_file = DATA_DIR + '/company_index.json'
f = open(json_file, 'r')
company_data = json.load(f)


def return_existing_kode(kode):
    db.session.commit()
    check_if_present = db.session.query(Company_List).filter_by(company_code=kode).first()
    db.session.close()
    return check_if_present


def data_processing(data, i):
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

    if existing_kode:
        existing_company = Company_List.query.filter_by(company_code=data[i]["company_code"])
        existing_company.update(val)
        db.session.commit()
        print ("data updated")
        print (val)
    else:
        new_company = Company_List(**val)
        db.session.add(new_company)
        print ("data added")
        print (val)



def main_update():
    """Main loop of the script, to interate data data_processing for each company."""
    timer_count = 0
    for i in range(len(company_data)):
        data_processing(company_data, i)
        time.sleep(2)
        timer_count += 1
        print (timer_count)
    db.session.close()
    # logger.info("---END---")
