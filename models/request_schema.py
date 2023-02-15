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

create_sales_model = {
    "type": "object",
    "properties": {
        "date": {
            "type": "string"
        },
        "quantity": {
            "type": "number"
        },
        "product_id": {
            "type": "integer"
        }
    },
    "required": [
        "date",
        "quantity",
        "product_id"
    ],
    "additionalProperties": False,
    "minProperties": 1
    
}
