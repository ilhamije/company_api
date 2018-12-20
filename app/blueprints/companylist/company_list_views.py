""" this module contains the REST endpoint"""
# import logging
from flask import jsonify, request
from app import Session
from models import Company_List


def index():
    return jsonify({'Message': "This is not the droid you are looking for."})


def get_companies():
    # logger = logging.getLogger(__name__)
    results = []
    total = 0
    if request.args:
        if "company_name" in request.args:
            # getting specific company by name
            companyname = request.args.get("company_name", "")
            session = Session()
            selected_company = session.query(Company_List).\
                filter(Company_List.company_name.ilike('%'+companyname+'%')).\
                all()
            session.close()
            if len(selected_company) == 0:
                statuscode = 404
                message = "Data not found"
            else:
                for i in selected_company:
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
                statuscode = 200
                message = "Successful"
                total = len(results)

            return jsonify({"status_code": statuscode,
                            "message": message,
                            "data": results,
                            "total": total})

        elif "industry" in request.args:
            # getting company with specific industry/sector
            industry = request.args.get("industry", "")
            session = Session()
            selected_company = session.query(Company_List).\
                filter(Company_List.sector.ilike('%'+industry+'%')).\
                all()
            session.close()
            if len(selected_company) == 0:
                statuscode = 404
                message = "Data not found"
            else:
                for i in selected_company:
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
                statuscode = 200
                message = "Successful"
                total = len(results)
            return jsonify({"status_code": statuscode,
                            "message": message,
                            "data": results,
                            "total": total})

        else:
            return jsonify({"status_code": 404,
                            "message": "Data not found"})

    else:
        # getting all companies
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
