from run import api, fields

date_api_response = api.model('date_api_response', {
    'name': fields.String(description='The name', required=True)
})