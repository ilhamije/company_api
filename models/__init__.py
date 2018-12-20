from flask_sqlalchemy import SQLAlchemy

import arrow
utc = arrow.utcnow()
local_sg = utc.to('Asia/Singapore').format('DD MMM YYYY hh:mm')

db = SQLAlchemy()


class Company_List(db.Model):
    __tablename__ = 'company_list'
    id_company_list = db.Column(db.Integer, primary_key=True)
    npwp = db.Column(db.String(30))
    company_name = db.Column(db.String(255))
    company_code = db.Column(db.String(10))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    fax = db.Column(db.String(255))
    address = db.Column(db.String(255))
    website = db.Column(db.String(255))
    business = db.Column(db.Text())
    sector = db.Column(db.String(255))
    url = db.Column(db.String(150))
    crawled_on = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=local_sg)

    def __init__(self, npwp, company_name, company_code, email, phone, fax, address, website, business, sector, url, crawled_on):
        self.npwp = npwp
        self.company_name = company_name
        self.company_code = company_code
        self.email = email
        self.phone = phone
        self.fax = fax
        self.address = address
        self.website = website
        self.business = business
        self.sector = sector
        self.url = url
        self.crawled_on = crawled_on
