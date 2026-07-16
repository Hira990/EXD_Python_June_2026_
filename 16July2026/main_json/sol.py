from patient_summary_constants import patient_summary_json
from heart_summary_constants import heart_summary_json

def cleerly_main_json():
    return {"booking_id": None, **patient_summary_json(), **heart_summary_json()}

import json
print(cleerly_main_json())

print(json.dumps(cleerly_main_json(), indent=4))
