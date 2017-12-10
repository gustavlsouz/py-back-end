from json import load

dbConf = load(open('config\\db.config.json'))

def get_DBConf():
	return dbConf