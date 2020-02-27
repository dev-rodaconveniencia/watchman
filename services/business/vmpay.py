from pprint import pprint as print
import requests

class AbstractApi:
  '''
  AbstractApi() -> None

  Conecta a VMPay e retorna via o endpoint e id (não obrigatório) informações cadastradas na api
  deles. Para acessar qualquer indexador da documentação é preciso passar a chave de acesso e o
  parâmetro de busca (https://vmpay-api.readthedocs.io/en/latest/intro.html). Para facilitar a
  integração, preferi criar classes de acesso com algumas funções automatizadas.
  '''

  _WISE_HEADERS = { 'content-type': 'application/json; charset=utf-8' }
  _WISE_PAYLOAD = { "access_token": "X6WktVwPeKagMHZh2iBBoEdK2cZK3h3TWQN5ZDDT" }
  _BASEURL = 'http://vmpay.vertitecnologia.com.br/api/v1/%s'

  @classmethod
  def _connect(cls, endpoint, id=None):
    '''
    Retorna um json com o resultado da busca por id ou não.
    '''
    uri = cls._BASEURL % endpoint
    if id != None:
      uri += '/%d' % id
    response = requests.get(uri, params=cls._WISE_PAYLOAD, headers=cls._WISE_HEADERS)
    return response.json()


class AbstractService:
  @classmethod
  def all(self):
    items = self._connect(endpoint=self.endpoint)
    return items

  @classmethod
  def filter(self, **kwargs):
    items = self.all()
    raise NotImplementedError

  @classmethod
  def get(self):
    raise NotImplementedError

  @classmethod
  def save(self):
    raise NotImplementedError    

  @classmethod
  def watchman(self):
    raise NotImplementedError


class Product(AbstractApi, AbstractService):
  endpoint = 'products'

Product.all()
