import requests
import base64

class search:
  @classmethod
  def image(self, barcode):
    image64 = None
    uri = "http://cdn-cosmos.bluesoft.com.br/products/%s" % barcode
    if barcode:
      response = requests.get(uri)
      if response.status_code == 200:
        safe = b"data:image/jpeg;base64,"
        image64 = safe + base64.b64encode(response.content)
    return image64
