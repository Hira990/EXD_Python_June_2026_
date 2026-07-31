import json

import xmltodict

student_xml_str = """
<student>
    <id>101</id>
    <name>
        <firstName>Ali</firstName>
        <lastName>Khan</lastName>
    </name>
    <age>20</age>
    <gender>Male</gender>
    <email>ali.khan@example.com</email>
    <phone>+92-300-1234567</phone>

    <address>
        <street>12 Main Road</street>
        <city>Lahore</city>
        <province>Punjab</province>
        <country>Pakistan</country>
        <postalCode>54000</postalCode>
    </address>

    <course>
        <courseId>CS101</courseId>
        <courseName>Introduction to Programming</courseName>
        <semester>Fall 2026</semester>
        <credits>3</credits>
    </course>

    <marks>
        <assignment>85</assignment>
        <midterm>78</midterm>
        <finalExam>90</finalExam>
        <total>253</total>
        <grade>A</grade>
    </marks>

    <skills>
        <skill>Python</skill>
        <skill>Java</skill>
        <skill>SQL</skill>
    </skills>

    <isScholarshipStudent>true</isScholarshipStudent>

</student>
"""

data = xmltodict.parse(student_xml_str)

print(data)
print(type(data))

json_data = json.dumps(data, indent=4)
print(json_data)