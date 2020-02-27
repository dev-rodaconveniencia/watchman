from rest_framework.serializers import ValidationError
import requests
import json
from retrying import retry

_WISE_HEADERS = {
  'accept': 'application/json',
  'Authorization': 'H3ojczx1O9LUhdYZ8IE9RKSgv0BL74GHVJQmvLRod6dJU8xzRvcLOUNG1rfSv0t1h78',
}

_WISE_PARAMS = [('apikey', 'FMJPZfVlxmv8bLjVBzaYyQZujl10RMFH6hyQwpUOWqfpAntAd2GMmo9gJe5Rmy5Bl03')]

@retry(stop_max_attempt_number=7)
def search(accessKey):
  response = requests.get(
    'https://nfe.api.nfe.io/v2/productinvoices/%s' % accessKey,
    headers=_WISE_HEADERS,
    params=_WISE_PARAMS
  )

  if response.status_code != 200:
    raise ValidationError({
      "error": "InvoiceNotFound",
      "message" : "A nota fiscal '%s' não foi encontrada." % accessKey
    })

  data = json.loads(response.text)

  return data

@retry(stop_max_attempt_number=7)
def xml(accessKey):
  try:
    response = requests.get(
      'https://nfe.api.nfe.io/v2/productinvoices/%s.xml' % accessKey,
      headers=_WISE_HEADERS,
      params=_WISE_PARAMS
    )
  except Exception as ex:
    raise ValidationError({
      "error": "NFEioError",
      "message": "A NFEio não respondeu a requisição. Tente novamente mais tarde."
    })

  if response.status_code != 200:
    raise ValidationError({
    "error": "InvoiceNotFound",
    "message" : "A nota fiscal '%s' não foi encontrada." % accessKey
  })

  return response.content
