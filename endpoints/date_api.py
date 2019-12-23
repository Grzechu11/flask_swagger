
from run import app, api, Resource, datetime, request, fields, Namespace

ns = api.namespace('date', 
                   description='Date endpoints')

from endpoints.models.date_api_response import date_api_response
from endpoints.models.add_date_api_request import add_date_api_request

@ns.route('/<name>')
@ns.doc(params={'name': 'The name'})
class DateApi_Gets(Resource):
    @ns.marshal_with(date_api_response, mask=False, code=200)
    def get(self, name):       
        now = datetime.now()
        formatted_now = now.strftime("%A, %d %B, %Y at %X")  
        return {'date': formatted_now, 'name': name }

@ns.route('')
class DateApi_Posts(Resource):
    @ns.expect(add_date_api_request)
    @ns.marshal_with(date_api_response, mask=False, code=200)
    def post(self):       
        now = datetime.now()
        formatted_now = now.strftime("%A, %d %B, %Y at %X")        
        r = request.json      
        return {'date': formatted_now, 'name': r.get('name') }