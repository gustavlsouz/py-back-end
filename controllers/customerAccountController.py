from bottle import response
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy import desc
from sqlalchemy.exc import *

from models import tb_customer_account as tbCust
from utils.desafioConf import get_desafio_conf

def get_desafio():
	Session = sessionmaker(bind=tbCust.get_engine())
	session = Session()
	
	dConf = get_desafio_conf()

	tb = tbCust.TbCustomerAccount

	valores = session.query(tb.vl_total, tb.nm_customer).filter(
			text('id_customer between %d and %d' % (dConf.get("idMin") , dConf.get("idMax") ) ) ).filter(
			text('vl_total %s' % dConf.get("val") )).order_by(desc(tb.vl_total))
	
	numeroDeRegistros = valores.count()

	print("\n\nRegistros encontrados %d, tipo %s\n\n" % (numeroDeRegistros, type(numeroDeRegistros)))

	if numeroDeRegistros > 0:
		nomes = []
		valorTotal = 0

		for el in valores:
			nomes.append(el.nm_customer)
			valorTotal+=el.vl_total

		media = valorTotal / numeroDeRegistros

		obj = {
			"media" : media,
			"nomes" : nomes
		}

		for nome in nomes:
			print(nome)
		print(media)
	else:
		obj = {"msg": "numero de registros é 0"}

	return obj


def post(json):

	def errorResponse(err):
		response.status = 500
		print("\n\n{}\n".format(err))
		session.rollback()
		return { "error": err }

	Session = sessionmaker(bind=tbCust.get_engine())
	session = Session()


	id_customer = json.get('id_customer')
	cpf_cnpj = json.get('cpf_cnpj')
	nm_customer = json.get('nm_customer')
	is_active = json.get('is_active')
	vl_total = json.get('vl_total')
	
	customer = tbCust.TbCustomerAccount(
		id_customer=id_customer
		,cpf_cnpj=cpf_cnpj
		,nm_customer=nm_customer
		,is_active=is_active
		,vl_total=vl_total
	)

	try:
		session.add(customer)
		print('Registro adicionado')
		session.commit()
		print('Commit.')
		response.status = 204
		pass
	except AmbiguousForeignKeysError:
		return errorResponse("AmbiguousForeignKeysError")
	except ArgumentError:
		return errorResponse("ArgumentError")
	except CircularDependencyError:
		return errorResponse("CircularDependencyError")
	except CompileError:
		return errorResponse("CompileError")
	except DBAPIError:
		return errorResponse("DBAPIError")
	except DataError:
		return errorResponse("DataError")
	except DatabaseError:
		return errorResponse("DatabaseError")
	except DisconnectionError:
		return errorResponse("DisconnectionError")
	except DontWrapMixin:
		return errorResponse("DontWrapMixin")
	except IdentifierError:
		return errorResponse("IdentifierError")
	except IntegrityError:
		return errorResponse("IntegrityError")
	except InterfaceError:
		return errorResponse("InterfaceError")
	except InternalError:
		return errorResponse("InternalError")
	except InvalidRequestError:
		return errorResponse("InvalidRequestError")
	except InvalidatePoolError:
		return errorResponse("InvalidatePoolError")
	except NoForeignKeysError:
		return errorResponse("NoForeignKeysError")
	except NoInspectionAvailable:
		return errorResponse("NoInspectionAvailable")
	except NoReferenceError:
		return errorResponse("NoReferenceError")
	except NoReferencedColumnError:
		return errorResponse("NoReferencedColumnError")
	except NoReferencedTableError:
		return errorResponse("NoReferencedTableError")
	except NoSuchColumnError:
		return errorResponse("NoSuchColumnError")
	except NoSuchModuleError:
		return errorResponse("NoSuchModuleError")
	except NoSuchTableError:
		return errorResponse("NoSuchTableError")
	except NotSupportedError:
		return errorResponse("NotSupportedError")
	except ObjectNotExecutableError:
		return errorResponse("ObjectNotExecutableError")
	except OperationalError:
		return errorResponse("OperationalError")
	except ProgrammingError:
		return errorResponse("ProgrammingError")
	except ResourceClosedError:
		return errorResponse("ResourceClosedError")
	except SADeprecationWarning:
		return errorResponse("SADeprecationWarning")
	except SAPendingDeprecationWarning:
		return errorResponse("SAPendingDeprecationWarning")
	except SAWarning:
		return errorResponse("SAWarning")
	except SQLAlchemyError:
		return errorResponse("SQLAlchemyError")
	except StatementError:
		return errorResponse("StatementError")
	except TimeoutError:
		return errorResponse("TimeoutError")
	except UnboundExecutionError:
		return errorResponse("UnboundExecutionError")
	except UnreflectableTableError:
		return errorResponse("UnreflectableTableError")
	except UnsupportedCompilationError:
		return errorResponse("UnsupportedCompilationError")
	except:
		return errorResponse("ErroDesconhecido")

	return