import random
import string

class Dummy : 
    # --------------------------------- 회원정보
    def first_name():
        name = input("이름을 입력해주세요 : ")
        # name = ""
        # for _ in range(5):
        #     name += random.choice(string.ascii_lowercase)
        return name
    def last_name():
        name = input("성을 입력해주세요 : ")
        # name = ""
        # for _ in range(5):
        #     name += random.choice(string.ascii_lowercase)
        return name
    def email():
        email = input("메일을 입력해주세요 : ")
        # email = ""
        # for _ in range(7):
        #     email += random.choice(string.ascii_lowercase)
        return email
    def password():
        password = input("비밀번호룰 입력해주세요 : ")
        # password = ""
        # for _ in range(8):
        #     password += random.choice(string.ascii_lowercase)
        return password
    def choice() :
        while True:
            gender = input("성별을 입력해주세요 남 : MALE, 여자 : FEMALE ")
            if gender == "Male" :
                break

            if gender == "FEMALE" : 
                break
            print("입력을 잘못하셨습니다. MALE, FEMALE 로 대문자만 입력해주세요")
        return gender
    
    #--------------------------------------- 재고
    def raw_materials_id():
        name = int(input("원재료 아이디를 입력해주세요 : "))
        return name
    
    def pre_quantity():
        name = int(input("이전 재고 수량을 입력해주세요 : "))
        return name
    
    def quantity():
        quantity = int(input("변동 재고수량을 입력해주세요 : "))
        return quantity
    
    def change_type():
        while True:
            type = input("분류를 입력해주세요 입고 : IN 출고 : OUT 반품 : RETURNED 폐기 : DISCARDED ")
            if type == "IN" :
                break
            if type == "OUT" :
                break
            if type == "RETURNED" :
                break
            if type == "DISCARDED" :
                break
            print("입력을 잘못하셨습니다. 입고 : IN 출고 : OUT 반품 : RETURNED 폐기 : DISCARDED 로 대문자만 입력해주세요")
        return type

    def store_id() :
        store = int(input("매장 번호를 입력해주세요 : "))
        return store
    #-----------------------------------------    세일즈 아이템 추가  
    def sales_record_id():
        sales_record_id = int(input("판매 번호를 입력해주세요 : "))
        return sales_record_id
    def product_id():
        product_id = int(input("제품 번호를 입력해주세요 : "))
        return product_id       
    def sales_quantity():
        sales_quantity = int(input("판매 수량을 입력해주세요 : "))
        return sales_quantity
    
    #-----------------------------------------    시그니처 메뉴 추가

    def product_name():
        product_name = input("제품명을 입력해주세요 : ")
        return product_name

    def description():
        description = input("상품 설명을 상세하게 입력해주세요 : ")
        return description

    def product_price():
        product_price = float(input("가격을 $로 입력해주세요: "))
        return round(product_price,2)
