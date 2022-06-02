import json
import jsonschema
from jsonschema import validate

class JsonValidator:
    def __init__(self, json_file, schema_file):
        self.json_file = json_file
        self.schema_file = schema_file
        
    def validate_schema(self):
        try:
            validate(self.json_file, self.schema_file)
        except jsonschema.exceptions.ValidationError as err: 
            return False 
        return True

    """
    Validates json data according to the schema given.
    """