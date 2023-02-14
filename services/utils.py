from jsonschema import validate
from jsonschema import ValidationError
from models.custom_exception import CustomException
from chalice import BadRequestError

def validate_request(request_json, model_json):
    try:
        validate(instance=request_json, schema=model_json)
    except ValidationError as e:
        message = return_param_error(e)
        raise BadRequestError(
            message
        )

def return_param_error(e: ValidationError):
        mensaje = ""
        param = ""
        if e.validator == 'type':
            for p in  e.absolute_path:
                if type(p) == str:
                    param += f'{p}.'
            mensaje = f'request error {param} must be type {e.validator_value}'
        if e.validator == 'required':
            param = e.message
            mensaje = f'Request error {param}'
        return mensaje