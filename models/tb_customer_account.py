from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, Sequence, String, Boolean, Float

from utils.DBconf import get_DBConf
from utils.desafioConf import get_desafio_conf

Base = declarative_base()

dbConf = get_DBConf()

# tb_customer_account
class TbCustomerAccount(Base):
	__tablename__ = 'tb_customer_account'

	id_customer = Column(Integer, primary_key=True)
	cpf_cnpj = Column(String(18), nullable=False)
	nm_customer = Column(String(70), nullable=False)
	is_active = Column(Boolean, nullable=False)
	vl_total = Column(Float, nullable=False)

	def __repr__(self):
		return "<TbCustomerAccount(id_customer=%r, cpf_cnpj=%r, nm_customer=%r, is_active=%r, vl_total=%r)>" % (self.id_customer, self.cpf_cnpj, self.nm_customer, self.is_active, self.vl_total)

	pass

confObj = get_desafio_conf()
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format( dbConf.get("user"), 
	dbConf.get("pwd"), dbConf.get("host"), 
	dbConf.get("dbname") ), 
	echo=confObj.get('debug') )
Base.metadata.create_all(engine)

def get_engine():
	return engine
