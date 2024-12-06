-- 유저 10명 추가
INSERT INTO USERS (first_name, last_name, email, password, address, contact, gender)
VALUES ('First1', 'Last1', 'email1@test.com', 'password1', 'address1', 'contact1', 'MALE'),
	   ('First2', 'Last2', 'email2@test.com', 'password2', 'address2', 'contact2', 'FEMALE'),
	   ('First3', 'Last3', 'email3@test.com', 'password3', 'address3', 'contact3', 'MALE'),
       ('First4', 'Last4', 'email4@test.com', 'password4', 'Address4', 'contact4', 'MALE'),
       ('First5', 'Last5', 'email5@test.com', 'password5', 'Address5', 'contact5', 'FEMALE'),
       ('First6', 'Last6', 'email6@test.com', 'password6', 'Address6', 'contact6', 'FEMALE'),
       ('First7', 'Last7', 'email7@test.com', 'password7', 'Address7', 'contact7', 'MALE'),
       ('First8', 'Last8', 'email8@test.com', 'password8', 'Address8', 'contact8', 'FEMALE'),
       ('First9', 'Last9', 'email9@test.com', 'password9', 'Address9', 'contact9', 'MALE'),
       ('First10', 'Last10', 'email10@test.com', 'password10', 'Address10', 'contact10','FEMALE');
       
-- 재고 10개 변동
INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id)
VALUES (1, 2, 3, 'IN', 1),
       (2, 3, 4, 'IN', 1),
       (3, 4, 5, 'IN', 1),
       (4, 5, 6, 'IN', 1),
       (5, 6, 7, 'IN', 1),
	   (6, 7, 8, 'IN', 1),
       (7, 8, 9, 'IN', 1),
       (8, 9, 10, 'IN', 1),
       (9, 10, 11, 'IN', 1),
       (10, 11, 12, 'IN', 1);
       
-- sales_items 테이블에 데이터 추가
INSERT INTO sales_items (sales_record_id, product_id, quantity)
VALUES (1, 2, 3),
       (2, 4, 6),
       (3, 5, 7),
       (4, 6, 8),
       (5, 7, 9),
       (6, 8, 10),
       (7, 9, 11),
       (8, 10, 12),
       (9, 11, 13),
       (10, 12, 14);

-- products 테이블에 시그니처 메뉴 추가
INSERT INTO products (name, description, price)
VALUES ('signature','the best of all kind. do not miss it', 12.77);

-- user1과 user2를 매장 id에 소속된 직원과 매니저로 변경
INSERT INTO employees (code, type, user_id, store_id, is_active)
VALUES(12331, 'STAFF', 1, 5, TRUE);

INSERT INTO employees (code, type, user_id, store_id, is_active)
VALUES(12332, 'MANAGER', 2, 7,TRUE);