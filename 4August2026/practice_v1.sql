CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender ENUM('Male', 'Female'),
    age INT,
    department VARCHAR(50),
    designation VARCHAR(50),
    salary DECIMAL(10,2),
    city VARCHAR(50),
    hire_date DATE
);


INSERT INTO employees
(first_name, last_name, gender, age, department, designation, salary, city, hire_date)
VALUES
('Ali', 'Khan', 'Male', 28, 'IT', 'Software Engineer', 85000, 'Lahore', '2022-01-15'),
('Sara', 'Ahmed', 'Female', 25, 'HR', 'HR Officer', 55000, 'Karachi', '2023-02-10'),
('Usman', 'Malik', 'Male', 32, 'Finance', 'Accountant', 70000, 'Islamabad', '2021-07-20'),
('Ayesha', 'Iqbal', 'Female', 29, 'IT', 'Web Developer', 78000, 'Lahore', '2020-11-05'),
('Hamza', 'Raza', 'Male', 35, 'Sales', 'Sales Manager', 92000, 'Faisalabad', '2019-04-18'),
('Fatima', 'Noor', 'Female', 27, 'Marketing', 'Marketing Executive', 62000, 'Multan', '2023-01-08'),
('Bilal', 'Hussain', 'Male', 31, 'IT', 'Database Administrator', 95000, 'Karachi', '2018-09-12'),
('Zainab', 'Saeed', 'Female', 26, 'Finance', 'Financial Analyst', 68000, 'Islamabad', '2022-06-25'),
('Ahmed', 'Shah', 'Male', 30, 'Sales', 'Sales Executive', 60000, 'Peshawar', '2021-03-17'),
('Hira', 'Aslam', 'Female', 24, 'IT', 'Frontend Developer', 72000, 'Lahore', '2024-02-01'),
('Omer', 'Farooq', 'Male', 33, 'Marketing', 'SEO Specialist', 65000, 'Karachi', '2020-08-14'),
('Maham', 'Khalid', 'Female', 28, 'HR', 'Recruiter', 58000, 'Rawalpindi', '2023-05-19'),
('Danish', 'Ali', 'Male', 36, 'Finance', 'Finance Manager', 105000, 'Lahore', '2017-12-11'),
('Sana', 'Yousaf', 'Female', 31, 'IT', 'Backend Developer', 89000, 'Islamabad', '2019-10-09'),
('Imran', 'Butt', 'Male', 40, 'Management', 'Project Manager', 120000, 'Karachi', '2016-06-01');