from bottle import run

from routes import customerAccountRoute
from utils.desafioConf import get_desafio_conf

def main():
	confObj = get_desafio_conf()
	run(host='localhost', port=8080, debug=confObj.get('debug'))
	pass

if __name__ == '__main__':
	main()
