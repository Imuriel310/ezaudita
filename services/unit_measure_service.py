import dao.unit_measure_dao as dao
from models.unit_measure_model import UnitMeasureModel
from chalice import NotFoundError


# Get a unit of measure by ID or all units of measure
def get_unit_measure(params:object) ->list or object :
    unit_measure_id = params.get('unit_measure_id') if params else None
    if unit_measure_id is not None:
        # Retrieve specific row by ID
        return get_unit_measure_by_id(unit_measure_id=int(unit_measure_id)), 200
    else:
        # Retrieve all unit measures
        return get_unit_measure_all(), 200


# Create a new unit of measure
def create_unit_measure(body:dict) -> dict:
    return dao.save_unit_measure(body.get('name')), 201


# Update a unit of measure's name
def update_unit_measure_name(body:dict, unit_measure_id:int) -> dict:
    return dao.update_unit_measure(body.get('name'), int(unit_measure_id)), 200


# Delete a unit of measure by ID
def delete_unit_measure(unit_measure_id:int) -> dict:
    dao.delete_unit_measure(unit_measure_id)
    return {'message':'unit measure deleted'}, 200


# Get a unit of measure by ID
def get_unit_measure_by_id(unit_measure_id:int) -> object:
    unit_measure_data = dao.get_unit_measure_specific(unit_measure_id=unit_measure_id)
    # Convert dict data into UnitMeasureModel
    if unit_measure_data is None:
        raise NotFoundError("unit measure not found")
    return UnitMeasureModel(
        unit_measure_id=unit_measure_data.unit_measure_id,
        name=unit_measure_data.name
    ).__dict__


# Get all unit of measures
def get_unit_measure_all() -> list:
    result_list = []
    unit_measure_data = dao.get_unit_measure_all()
    for unit_measure in unit_measure_data:
        result_list.append(
            UnitMeasureModel(
                unit_measure_id=unit_measure.unit_measure_id,
                name=unit_measure.name
            ).__dict__
        )
    return result_list