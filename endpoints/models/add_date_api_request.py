from run import api, fields

add_date_api_request = api.model('add_date_api_request', {
    'name': fields.String(description='The name', required=True)
})