import xmltodict
import json

with open("echo_study.xml", "r") as file:
    xml_content = file.read()

# print(xml_content)

try:
    study_data = xmltodict.parse(xml_content)
    print(json.dumps(study_data, indent=4))

    try:
        study_type = study_data['MeasurementExport']['Patient']['Studyq']['StudyDescription']

        if "ECHO" in study_type:
            print("yes")
        else:
            print("no")
    except Exception as e:
        print("xml not contain keys we wanted")
except Exception as e:
    print("xml not valid")

