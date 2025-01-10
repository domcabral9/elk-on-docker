import requests
from datetime import datetime, timezone
import secrets
import string
import hashlib

def test_advanced_authentication(api_key_id, api_key):
    # Gerar valores necessários
    nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
    timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
    auth_key = "%s%s%s" % (api_key, nonce, timestamp)
    auth_key = auth_key.encode("utf-8")
    api_key_hash = hashlib.sha256(auth_key).hexdigest()

    # Configurar headers
    headers = {
        "x-xdr-timestamp": str(timestamp),
        "x-xdr-nonce": nonce,
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key_hash
    }

    # Parâmetros da requisição
    parameters = {
        "request_data": {
            "filters": [],
            "sort": {"field": "creation_time", "keyword": "desc"},
            "pagination": {"limit": 100}
        }
    }

    # Fazer a requisição
    res = requests.post(
        url="https://api-<YOU-ORGANIZATION>.xdr.us.paloaltonetworks.com/public_api/v1/alerts/get_alerts",
        headers=headers,
        json=parameters
    )
    return res.text

# Substituir pelos seus valores
api_key_id = "4"  # Exemplo
api_key = "INPUT YOUR KEY HERE"
print(test_advanced_authentication(api_key_id, api_key))
