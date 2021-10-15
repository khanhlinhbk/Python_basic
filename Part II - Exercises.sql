-- 1.
-- Viết câu lệnh truy vấn lấy dữ liệu từ 2 bảng orders và shippers:
-- Kết quả bao gồm: order_id, shipped_date và shipper_name

-- 2.
-- Viết câu lệnh truy vấn lấy ra dữ liệu từ tất cả các bảng trong CSDL sql_invoicing:
-- Kết quả bao gồm: payment_id, client_name, client_address, invoice_number, payment_method và amount

-- 3.
-- Viết câu lệnh truy vấn lấy ra dữ liệu từ 4 bảng orders,order_item customers, order_statuses trong CSDL sql_store, và bảng products trong CSDL sql_inventory:
-- Kết quả bao gồm: order_id, full_name, status_name, và product_name
-- Sắp xếp tập kết quả theo order_id

-- 4.
-- Viết câu lệnh truy vấn lấy ra các records từ 2 bảng employees và offices:
-- Các cột bao gồm: Employee ID, Full Name, Report To, Office Address
-- Report To là full_name của employee tương ứng
-- Chỉ lấy ra các records với office_id là 1
-- Sắp xếp kết quả theo Employee ID

-- 5.
-- Viết câu lệnh truy vấn lấy ra các records từ 2 bảng products và order_items:
-- Chứa các cột Product ID, Product Name, Quantity (trong bảng order_items)
-- Tập kết quả phải bao gồm cả các products chưa có (không tồn tại) trong order_items

-- 6.
-- Viết câu lệnh truy vấn lấy ra các records từ bảng employees:
-- Chứa các cột Employee ID, Employee Name, và Report To (Employee Name)
-- Tập kết quả bao gồm cả các records mà Report To là NULL
-- Nếu Report To là NULL, hiển thị text thay thế là 'Big Boss'

-- 7 .
-- Viết câu lệnh truy vấn lấy ra các records từ 4 bảng orders, customers, order_statuses và shippers:
-- Chứa các cột Order ID, Customer Full Name, Ship Status và Shipper Name
-- Bao gồm tất cả records trong orders, bất kể có shiper_id hay không
-- Sắp xếp dữ liệu theo order_id