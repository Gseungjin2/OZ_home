SELECT * FROM classicmodels.products;

-- 1) customers 테이블에 새 고객을 추가하세요.
INSERT INTO `classicmodels`.`customers` (`customerNumber`, `customerName`, `contactLastName`, `contactFirstName`, `phone`, `addressLine1`, `city`, `country`) VALUES ('123', 'seungjin_shop', 'seungjin2', 'Sue', '+02 2 1234567', 'seoul', 'seoul', 'seoul');
-- '123', 'seungjin_shop', 'seungjin2', 'Sue', '+02 2 1234567', 'seoul', NULL, 'seoul', NULL, NULL, 'seoul', NULL, NULL

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
