-- ============================================
-- Employee Analysis SQL Script
-- File: employee_analysis.sql
-- ============================================

-- Task 1: Basic Querying
-- 1. Select all employees in Marketing department
SELECT *
FROM employees
WHERE department = 'Marketing';

-- 2. Display name, department, and salary for employees earning > $90,000
SELECT name, department, salary
FROM employees
WHERE salary > 90000;

-- 3. Find employees in Sales OR Finance departments
SELECT *
FROM employees
WHERE department IN ('Sales', 'Finance');

-- ============================================
-- Task 2: Sorting and Limiting
-- ============================================

-- 1. Top 5 highest-paid employees
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;

-- 2. 3 most recently hired employees in Engineering
SELECT *
FROM employees
WHERE department = 'Engineering'
ORDER BY hire_date DESC
LIMIT 3;

-- 3. Oldest employee earning > $70,000 and not in HR
SELECT *
FROM employees
WHERE salary > 70000
  AND department != 'HR'
ORDER BY hire_date ASC
LIMIT 1;

-- ============================================
-- Task 3: Calculated Fields and Aliases
-- ============================================

-- 1. Monthly salary report for employees earning > $60,000
SELECT name,
       salary,
       (salary/12) AS monthly_pay
FROM employees
WHERE salary > 60000;

-- 2. Finance department salary report
SELECT name AS employee_name,
       salary AS annual_salary,
       (salary/12) AS monthly_salary
FROM employees
WHERE department = 'Finance'
ORDER BY salary DESC;
