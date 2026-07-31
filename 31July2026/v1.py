# What is XML File / XML Format

"""
<book>
    <title>Learning XML</title>
    <author>John Smith</author>
    <price>29.99</price>
</book>
"""

xml_info = {
    "student": {
        "id": 101,
        "name": {
            "firstName": "Ali",
            "lastName": "Khan"
        },
        "age": 20,
        "gender": "Male",
        "email": "ali.khan@example.com",
        "phone": "+92-300-1234567",
        "address": {
            "street": "12 Main Road",
            "city": "Lahore",
            "province": "Punjab",
            "country": "Pakistan",
            "postalCode": "54000"
        },
        "course": {
            "courseId": "CS101",
            "courseName": "Introduction to Programming",
            "semester": "Fall 2026",
            "credits": 3
        },
        "marks": {
            "assignment": 85,
            "midterm": 78,
            "finalExam": 90,
            "total": 253,
            "grade": "A"
        },
        "skills": [
            "Python",
            "Java",
            "SQL"
        ],
        "isScholarshipStudent": True
    }
}

"""
<?xml version="1.0" encoding="UTF-8"?>
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
