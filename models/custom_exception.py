from jsonschema.exceptions import ValidationError
from chalice import Response
class CustomException(Exception):
    def __init__(
                    self,
                    message,
                    status_code,
                ):
        Exception.__init__(self)
        return Response(
            status_code=status_code,
            body={
                "message": message,
                "error": self.errors_catalog(status_code)
            },
            headers={'Content-Type': 'application/json'}
        )
    
    def errors_catalog(self, error):
        error_dict = {
            400: 'Bad Request',
            404: 'Not Found',
            405: 'Method not allowed',
            500: 'Internal Server Error'
        }
        return error_dict.get(error)
    
   
