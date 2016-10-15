import urllib.request
import json

class BaseClient:
    BASE_URL = None # URL VK API

    method = None # Метод VK API
    http_method = None

    def get_params(self):  # Получение GET параметров запроса
        pass

    def get_json(self):    # Получение данных POST запроса
        pass

    def get_headers(self):  # Получение HTTP заголовков
        pass

    def generate_url(self, method):
        return '{0}{1}'.format(self.BASE_URL, method)

    def _get_data(self, method, http_method):   # Отправка запроса к VK API
        response = None

        # todo выполнить запрос

        return self.response_handler(response)

    def response_handler(self, response):  # Обработка ответа от VK API
        return response

    def execute(self):  # Запуск клиента
        return self._get_data(
            self.method,
            self.http_method
        )


class VkApi(BaseClient):
    PARAMETERS = {}
    response = ""

    def __init__(self):
        self.http_method = "GET"
        self.BASE_URL = "https://api.vk.com/method/"

    def set_parameters(self, par):
        self.PARAMETERS = par

    def get_json(self):
        return json.loads(self.response)

    def _get_data(self, method, http_method):
        if http_method != "GET":
            return 'unsupported'
        params = self.generate_url(method)
        params += "?"
        params += "".join(['%s=%s&' % (key, value) for (key, value) in self.PARAMETERS.items()])
        params += 'v=5.56'

        response = urllib.request.urlopen(params)

        if response is not None:
            self.response = response.read().decode("utf-8")
            return self.get_json()
        else:
            return False
