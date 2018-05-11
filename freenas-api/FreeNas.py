import requests
from requests.auth import HTTPBasicAuth

class FreeNas:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password


    def enable_cifs(self):
        return self.enable_service('cifs')


    def enable_service(self, service):
        resource = '{}/services/services/{}/'.format(host, service)
        body = {
            'srv_enable': True
        }
        r = requests.put(resource, json=body, auth=HTTPBasicAuth(self.user, self.password))
        return r


if __name__ == '__main__':
    nas = FreeNas('192.168.128.100', 'root', '0')
    r = nas.enable_cifs()
    print(r.content)