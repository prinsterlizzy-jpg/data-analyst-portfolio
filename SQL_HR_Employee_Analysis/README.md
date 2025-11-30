SQL Project: HR Employee Analysis

🧑‍💼 HR Employee Data Analysis Using SQL

Overview

Analyzed workforce structure, salary distribution, and department staffing.

⸻

🔧 Tools Used
	•	SQL
	•	HR Dataset

⸻

📁 Project Files
	•	hr_employee_analysis.sql
	•	Employee dataset
	•	Query results

⸻

🗂️ Dataset Columns
	•	employee_id
	•	name
	•	gender
	•	age
	•	department
	•	salary
	•	hire_date

⸻

🛠 Key SQL Queries

1️⃣ Average Salary by Department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

2️⃣ Number of Employees per Department
SELECT department, COUNT(*) AS staff_count
FROM employees
GROUP BY department;

3️⃣ Longest Serving Employees
SELECT name, hire_date
FROM employees
ORDER BY hire_date ASC
LIMIT 10;

📈 Insights
	•	IT department had the highest salary average.
	•	32% of employees earned above company average.
	•	Gender split was nearly balanced: 48% female, 52% male.

⸻

✅ Conclusion

SQL analysis helps HR understand workforce distribution and compensation structure.


