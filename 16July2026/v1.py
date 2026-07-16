# report_data = {
#     "patient_name": "fcwe",
#     "mrn": None,
#     "cleerly_id": None,
#     "study_date": None,
#     "provider": "sdfghjkl",
#     "summary": {
#         "atherosclerosis": {
#             "value": 2,
#             "total_plaque": "t1"
#         },
#         "stenosis": {
#             "value": 4,
#             "total_plaque": "t2",
#             "readings": [1, 2, 3, 23, 12, 10]
#         }
#     },
# }
#
# print(report_data["patient_name"])
# print(report_data["summary"]["stenosis"]["total_plaque"])
# print(report_data["summary"]["stenosis"]["readings"])
#
# for reading in report_data["summary"]["stenosis"]["readings"]:
#     print(reading)
#
import datetime, re
name_dob_str = "CHAUDHRY IFTIKHAR HUSSAIN (2/10/1971),"
name_dob_str = "ALI (2/10/1971) dxfcgvhbjk"

match = re.search(r"\(([^()]*)\)", name_dob_str)
if match:
    date_of_birth = match.group(1)
    print(date_of_birth)  # 124124
    print(date_of_birth)
    dob_object = datetime.date.strptime(date_of_birth, "%d/%m/%Y")
    print(dob_object)
else:
    print("no dob found")