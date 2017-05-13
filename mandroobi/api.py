from __future__ import absolute_import

from flask import Flask
from flask_restful import Api


from mandroobi.models.resources import (AccountResource, AccountingPeriodResource, BusinessUnitResource,
                                        CurrencyResource, DriverResource, ScenarioResource)

app = Flask(__name__)
api = Api(app)

api.add_resource(AccountResource, '/account/<id>')
api.add_resource(AccountingPeriodResource, '/accounting_period/<id>')
api.add_resource(BusinessUnitResource, '/business_unit/<id>')
api.add_resource(CurrencyResource, '/currency/<id>')
api.add_resource(DriverResource, '/driver/<id>')
api.add_resource(ScenarioResource, '/scenario/<id>')


if __name__ == '__main__':
    app.run(debug=True)
