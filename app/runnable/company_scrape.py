import os
import requests
import json
from datetime import datetime


def main():
    URL = 'https://www.idx.co.id/umbraco/Surface/ListedCompany/GetCompanyProfiles?length=1000'
    # https://www.idx.co.id/en-us/listed-companies/company-profiles/company-profile-detail/?kodeEmiten=AALI
    APP_ROOT = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
    DATA_DIR = os.path.join(APP_ROOT, 'static/data')

    response = requests.get(URL)
    resp_json = response.json()
    data_json = resp_json["data"]

    data_list = []
    key_list = ["NPWP", "NamaEmiten", "KodeEmiten", "Sektor", "Email", "Telepon", "Fax", "Alamat", "Website", "KegiatanUsahaUtama"]
    key_list_new = ["npwp", "company_name", "company_code", "sector", "email", "phone", "fax", "address", "website", "business"]

    for i in data_json:
        data_dict = {}
        for key, value in i.items():
            if key in key_list:
                data_dict[key_list_new[key_list.index(key)]] = value
        data_dict["url"] = "https://www.idx.co.id/en-us/listed-companies/company-profiles/company-profile-detail/?kodeEmiten=" + i["KodeEmiten"]
        data_dict["crawled_on"] = '{:%Y-%m-%d}'.format(datetime.now())

        data_list.append(data_dict)

    result = json.dumps(data_list)
    json_file = DATA_DIR + '/company_index.json'
    f = open(json_file, 'w')
    f.write(result)
    # if f.write(result):
    #     print "data extracted to: " + json_file
    # else:
    #     print "data extracting is failed"


if __name__ == "__main__":
    main()
