from json import load

desafioConf = load(open('config\\desafio.json'))

debug = desafioConf.get('debug')

if debug == 1:
	desafioConf['debug'] = True
elif debug == 0:
	desafioConf['debug'] = False
else:
	print("\n\nDebug em desafio.json deve ser 0 ou 1\n\n")
	quit()

def get_desafio_conf():
	return desafioConf