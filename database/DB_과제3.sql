use classicmodels

-- 1) customers 테이블에 새 고객을 추가하세요.
INSERT INTO `classicmodels`.`customers` (`customerNumber`, `customerName`, `contactLastName`, `contactFirstName`, `phone`, `addressLine1`, `city`, `country`) VALUES ('123', 'seungjin_shop', 'seungjin2', 'Sue', '+02 2 1234567', 'seoul', 'seoul', 'seoul');

-- (2) **`products`** 테이블에 새 제품을 추가하세요.
INSERT INTO `classicmodels`.`products` (`productCode`, `productName`, `productLine`, `productScale`, `productVendor`, `productDescription`, `quantityInStock`, `buyPrice`, `MSRP`) VALUES ('S78_3211', 'seungjin', 'Ships', '1:74', 'Unimax Art Galleries', 'easures 39 inches Long x 34 3/4 inches High. Includes a stand.', '612', '38.33', '55.70');

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
INSERT INTO `classicmodels`.`employees` (`employeeNumber`, `lastName`, `firstName`, `extension`, `email`, `officeCode`, `reportsTo`, `jobTitle`) VALUES ('1709', 'Gerarr', 'Martins', 'x2313', 'kgerard@classicmodelcars.com', '4', '1102', 'Sales Rep');

-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
INSERT INTO `classicmodels`.`offices` (`officeCode`, `city`, `phone`, `addressLine1`, `addressLine2`, `country`, `postalCode`, `territory`) VALUES ('8', 'Londons', '+44 20 7877 2042', '27 Old Broad Street', 'Level 8', 'KR', 'EC2N 1HNS', 'EMEAS');

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
INSERT INTO `classicmodels`.`orders` (`orderNumber`, `orderDate`, `requiredDate`, `shippedDate`, `status`, `customerNumber`) VALUES ('10426', '2005-06-01', '2005-06-06', '2005-06-03', 'In Process', 201);

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요. 
INSERT INTO `classicmodels`.`orderdetails` (`orderNumber`, `productCode`, `quantityOrdered`, `priceEach`, `orderLineNumber`) VALUES ('10424', 'S10_2016', '70', '50.02', '9');

-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
INSERT INTO `classicmodels`.`payments` (`customerNumber`, `checkNumber`, `paymentDate`) VALUES ('496', 'MN89922', '2005-01-20');

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요. 
INSERT INTO `classicmodels`.`productlines` (`productLine`) VALUES ('Kang');

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO `classicmodels`.`customers` (`customerNumber`, `customerName`, `contactLastName`, `contactFirstName`, `phone`, `addressLine1`, `city`, `country`, `salesRepEmployeeNumber`, `creditLimit`) VALUES ('113', 'seungjin', 'seungjink', 'seoul', '+82 9 5000000', '6252 Ingle Ln.', 'Aucklans', '', '1002', '72600.02');

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO `classicmodels`.`products` (`productCode`, `productName`, `productLine`, `productScale`, `productVendor`, `productDescription`, `quantityInStock`, `buyPrice`) VALUES ('S88_3211', 'seungjin2', 'Ships', '1:78', 'Unimax Art Galleries', 'easures 39 inches Long x 34 3/4 inches High. Includes a stand.2', '623', '38.34');

-- 일기

-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
select * from `customers`;

-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
select * from `products`;

-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
select `firstName`, `lastName`, `jobTitle` from `employees`;

-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
select `addressLine1`, `addressLine2` from `offices`;

-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
select * from `orders` ORDER BY `orderDate` DESC LIMIT 10;

-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from `orderdetails` where `orderNumber` = 10100;

-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from `payments` where `customerNumber` = 114;

-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
 select `roductLine`, `textDescription` from `productlines`;

-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
select `city`, `country` from `customers`;

-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT * FROM `products` WHERE `buyPrice` BETWEEN 20 AND 50;

-- 갱신 
-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
update `classicmodels`,`customers` set `addressLine1` = '456 Updated St' where (`customerNumber` = '113');
-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
update `classicmodels`.`products` set `buyPrice` = '104.46' where (`productCode` = 'S10_4962');

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
update `classicmodels`.`employees` set `jobTitle` = 'VP Marketing' where (`employeeNumber` = '1165');

-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
update `classicmodels`.`offices` set `phone` = '+1 650 219 9547' where (`officeCode` = '1');

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
update `classicmodels`.`orders` set `status` = 'Shipped' where (`orderNumber` = '10420');

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
update `classicmodels`.`orderdetails` set `priceEach` = '37.74' where (`orderNumber` = '10205') and (`productCode` = 'S24_2022');

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
update `classicmodels`.`payments` set `amount` = '52266.98' where (`customerNumber` = '496') and (`checkNumber` = 'MN89922');

-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
update `classicmodels`.`productlines` set `productLine` = 'Kang2.ver', `textDescription` = 'aaassssccccc' where (`productLine` = 'Kang');

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.customers
update `classicmodels`.`customers` set`addressLine1` = 'Erling Skakkes gate 80' where (`customerNumber` = '123');
update `classicmodels`.`customers` set `addressLine1` = '466Updated St', `addressLine2` = 'Level 3' where (`customerNumber` = '113');

-- 삭제

-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
delete from `classicmodels`.`customers` where (`customerNumber` = '123');
delete from `classicmodels`.`customers` where (`customerNumber` = '113');
-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
delete from  `classicmodels`.`products` WHERE `productName` = 'seungjin2' and `productCode` = 'S88_3211';

-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.

-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.

-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.

-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.

-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.

-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.

-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.

