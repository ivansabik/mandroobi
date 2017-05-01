from __future__ import absolute_import

from flask_restful import abort, reqparse, Resource
from sqlalchemy_mixins import ModelNotFoundError

from .dimensions import Account, AccountingPeriod, BusinessUnit, Currency, Driver, Scenario


RESOURCES_CLASSES_MAPPING = {
    'AccountResource': Account,
    'AccountingPeriodResource': AccountingPeriod,
    'BusinessUnitResource': BusinessUnit,
    'CurrencyResource': Currency,
    'DriverResource': Driver,
    'ScenarioResource': Scenario,
}


class ApiResource(Resource):
    def __init__(self):
        self.resource_model = RESOURCES_CLASSES_MAPPING[self.__class__.__name__]
        self.parser = reqparse.RequestParser()

    def _validate_put_patch_params(self, put=True):
        '''
        Example:
            self.parser.add_argument('user', type=str, required=True)
            return self.parser.parse_args()

        return: dict with parsed args, coming from self.parser.parse_args()
        '''
        raise NotImplementedError('Needs to be implemented by inheriting class')

    def get(self, id):
        '''
        Gets an existing API resource
        '''
        try:
            resource = self.resource_model.find_or_fail(id)
        except ModelNotFoundError:
            abort(404, message='{} does not exist'.format(id))
        else:
            return resource

    def delete(self, id):
        '''
        Deletes an existing API resource
        '''
        try:
            resource = self.resource_model.find_or_fail(id)
        except ModelNotFoundError:
            abort(404, message='{} does not exist'.format(id))
        else:
            resource.delete()
            return {'success': True, 'message': '{} id deleted'.format(id)}, 204

    def put(self):
        '''
        Creates a new API resource
        '''
        args = self._validate_put_patch_params(put=True)
        resource = self.resource_model().create(**args)
        return resource, 201

    def patch(self, id):
        '''
        Updates an existing API resource, will only updated passed args
        '''
        try:
            resource = self.resource_model.find_or_fail(id)
        except ModelNotFoundError:
            abort(404, message='{} does not exist'.format(id))
        else:
            args = self._validate_put_patch_params(put=False)
            return resource.update(**args), 200


class AccountResource(ApiResource):
    def _validate_put_patch_params(self, put=True):
        if put:
            required = True
            self.parser.add_argument('id', required=required)
        else:
            required = False
        self.parser.add_argument('description', required=required)
        self.parser.add_argument('parent_id', required=required)
        self.parser.add_argument('type', required=required)
        return self.parser.parse_args()


class AccountingPeriodResource(ApiResource):
    def _validate_put_patch_params(self, put=True):
        if put:
            required = True
            self.parser.add_argument('id', required=required)
        else:
            required = False
        self.parser.add_argument('description', required=required)
        self.parser.add_argument('parent_id', required=required)
        self.parser.add_argument('date', required=False)
        self.parser.add_argument('day', type=int, required=False)
        self.parser.add_argument('month', type=int, required=required)
        # Quarter is set before inserting AccountingPeriod to db
        self.parser.add_argument('year', type=int, required=required)
        return self.parser.parse_args()


class BusinessUnitResource(ApiResource):
    def _validate_put_patch_params(self, put=True):
        if put:
            required = True
            self.parser.add_argument('id', required=required)
        else:
            required = False
        self.parser.add_argument('description', required=required)
        self.parser.add_argument('parent_id', required=required)
        self.parser.add_argument('local_currency', required=required)
        return self.parser.parse_args()


class CurrencyResource(ApiResource):
    def _validate_put_patch_params(self, put=True):
        if put:
            required = True
            self.parser.add_argument('id', required=required)
        else:
            required = False
        self.parser.add_argument('description', required=required)
        self.parser.add_argument('parent_id', required=required)
        return self.parser.parse_args()


class DriverResource(ApiResource):
    def _validate_put_patch_params(self, put=True):
        if put:
            required = True
            self.parser.add_argument('id', required=required)
        else:
            required = False
        self.parser.add_argument('description', required=required)
        self.parser.add_argument('parent_id', required=required)
        return self.parser.parse_args()


class ScenarioResource(ApiResource):
    def _validate_put_patch_params(self, put=True):
        if put:
            required = True
            self.parser.add_argument('id', required=required)
        else:
            required = False
        self.parser.add_argument('description', required=required)
        self.parser.add_argument('parent_id', required=required)
        return self.parser.parse_args()
