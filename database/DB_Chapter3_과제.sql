USE testdatabase;

CREATE TABLE Employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2),
    unique_id INT UNIQUE
);

CREATE INDEX idx_unique_id ON Employees (unique_id);

SHOW INDEX FROM Employees;

START TRANSACTION;

INSERT INTO Employees (name, position, salary, unique_id)
VALUES 
    ('해린', 'PM', 90000.00, 1),
    ('은우', 'Frontend', 80000.00, 2),
    ('가을', 'Backend', 92000.00, 3),
    ('지수', 'Frontend', 78000.00, 4),
    ('민혁', 'Frontend', 96000.00, 5),
    ('하온', 'Backend', 130000.00, 6);

-- 1. 모든 직원의 이름과 연봉 정보만을 조회하는 쿼리를 작성해주세요
SELECT name, salary FROM Employees;

-- 2. Frontend 직책을 가진 직원 중에서 연봉이 90000 이하인 직원의 이름과 연봉을 조회하세요.
SELECT name, salary FROM Employees WHERE position = 'Frontend' AND salary <= 90000;

-- 3. PM 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.
UPDATE Employees SET salary = salary * 1.10 WHERE position = 'PM' AND unique_id = 1;
SELECT name, salary FROM Employees WHERE position = 'PM';

-- 4. 모든 Backend' 직책을 가진 직원의 연봉을 5% 인상하세요.
UPDATE Employees SET salary = salary * 1.05 WHERE position = 'Backend' AND (unique_id = 3 OR unique_id = 6);
SELECT name, salary FROM Employees WHERE position = 'Backend';

-- 5. 민혁 사원의 데이터를 삭제하세요
DELETE FROM Employees WHERE unique_id = 5;

COMMIT;

-- 데이터 삭제 확인
SELECT * FROM Employees;

-- 6. 모든 직원을 position 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요
SELECT position, AVG(salary) AS AverageSalary FROM Employees GROUP BY position;

-- 7. employees 테이블을 삭제하세요.
DROP TABLE Employees;
