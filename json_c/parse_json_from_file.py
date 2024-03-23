import json
from jsonpath import jsonpath


class JsonUtil:


    @staticmethod
    def jsonPathStr(json_str, json_path):
        jsonObj = jsonpath(json.loads(json_str), json_path)
        return json.dumps(jsonObj, indent=4, ensure_ascii=False)

    


