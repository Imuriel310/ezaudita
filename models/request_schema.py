unit_measure_model = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        }
    },
    "required": [
        "name",
    ],
    "additionalProperties": False
}

create_product_model = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "price": {
            "type": "number"
        },
        "unit_measure_id": {
            "type": "integer"
        }
    },
    "required": [
        "name",
        "price",
        "unit_measure_id"
    ],
    "additionalProperties": False
}

update_product_model = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "price": {
            "type": "number"
        },
        "unit_measure_id": {
            "type": "integer"
        }
    },
    "required": [
    ],
    "additionalProperties": False,
    "minProperties": 1
    
}
