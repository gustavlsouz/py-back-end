from bottle import route, request 

from controllers import customerAccountController

@route('/desafio', method='GET')
def desafio():
	return customerAccountController.get_desafio()

@route('/desafio/post', method='POST')
def post_registros():
	return customerAccountController.post(request.json)
