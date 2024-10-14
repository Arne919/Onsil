-- Active: 1728635811571@@127.0.0.1@3306
INSERT INTO employees (name, age, salary, departmentId) 
VALUES ('이규보', 77,  1700, 1);      
INSERT INTO employees (name, age, salary, departmentId) 
VALUES ('김구', 21,  126000, 2);
INSERT INTO employees (name, age, salary, departmentId) 
VALUES ('안중근', 37,  23000, 3);
INSERT INTO employees (name, age, salary, departmentId) 
VALUES ('유관순', 41,  82000, 4);  

SELECT departments.name AS department,
        employees.name AS oldest_employee,
        MAX(employees.age) AS max_age,
        AVG(employees.age) AS avg_age
FROM employees
JOIN departments ON employees.departmentId = departments.id
GROUP BY departments.name;

SELECT departments.name AS department,
       employees.name AS highest_paid_employee,
       employees.salary AS max_salary
FROM employees
JOIN departments ON employees.departmentId = departments.id
WHERE (employees.salary, employees.departmentId) IN (
    SELECT MAX(salary), departmentId
    FROM employees
    GROUP BY departmentId
);

SELECT departments.name AS department,
       CASE
           WHEN age < 30 THEN 'Under 30'
           WHEN age BETWEEN 30 AND 40 THEN 'BETWEEN 30-40'
           ELSE 'Over 40'
       END AS age_group,
       COUNT(*) AS num_employees
FROM employees
JOIN departments ON employees.departmentId = departments.id
GROUP BY department, age_group
ORDER BY department, age_group;


SELECT departments.name AS department,
       AVG(employees.salary) AS avg_salary_excluding_highest
FROM employees
JOIN departments ON employees.departmentId = departments.id
WHERE (employees.salary, employees.departmentId) NOT IN (
    SELECT MAX(salary), departmentId
    FROM employees
    GROUP BY departmentId
)
GROUP BY departments.name;
