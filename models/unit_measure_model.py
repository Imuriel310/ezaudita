from datetime import date

class UnitMeasureModel:

    def __init__(self,
                unit_measure_id = None,
                name = None):
        """Constructor"""
        self.unit_measure_id = unit_measure_id
        self.name = name

    unit_measure_id: int
    name: str