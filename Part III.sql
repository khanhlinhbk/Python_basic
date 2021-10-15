-- Các hàm tổng hợp cơ bản
SELECT 
    MIN(quantity_in_stock) AS lowest,
    MAX(quantity_in_stock) AS highest,
    AVG(unit_price) AS average_price,
    SUM(quantity_in_stock * unit_price) AS total
    COUNT(*) AS total_products
FROM products;

-- Tính tổng bill cho đơn hàng có order = 2
SELECT 
    order_id, 
    SUM(quantity * unit_price) AS total_bill
FROM sql_store.order_items
WHERE order_id = 2;


-- GROUP BY

-- Tính tổng số lượng đã bán theo product trong bảng order_items
-- Sắp xếp theo sản phẩm bán chạy nhất
SELECT 
    name, SUM(quantity) AS sold 
FROM order_items
JOIN products
    USING(product_id)
GROUP BY product_id
ORDER BY sold DESC;

-- Tính tổng số đơn đã ship theo shipper
SELECT name, COUNT(order_id)
FROM shippers
LEFT JOIN orders
USING(shipper_id)
GROUP BY name;

-- HAVING

-- Tính tổng bill cho các đơn hàng
-- Chỉ lấy ra các đơn có bill > 50
SELECT 
    order_id, SUM(quantity * unit_price) AS total_bill
FROM order_items
GROUP BY order_id 
HAVING total_bill > 50;

-- Tính tổng tương theo office_id
-- Chỉ lấy ra các office có tổng lương phải trả cao hơn 300000
SELECT 
    office_id, 
    SUM(salary)
FROM employees
GROUP BY office_id
HAVING SUM(salary) > 300000;