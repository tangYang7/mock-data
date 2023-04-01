import json
from random import choice, shuffle
import IDcard

# 生成的資料數
N = 8

# 將 Python 資料轉為 JSON 格式，儲存至 json 檔案
for i in range(0, N) :
    nationality = choice(['Taiwan', 'Taiwan', 'Taiwan', 'Taiwan', 'Taiwan', 'Taiwan', 'Hong Kong', 'Japan', 'Canada', 'China'])

    numbers = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    name_zh = [ '宣', '光', '貫', '冠', '宇', '亦', '雨', '菲', '祐', '嘉', 
                '豪', '曉', '筱', '罐', '新', '鑫', '興', '杏', '美', '梅',
                '名', '桀', '杰', '昱', '域', '琝', '柚', '雯', '文', '玫',  
                '電', '強', '廣', '鴻', '宏', '華', '樺', '民', '冥', '銘',
                '仰', '澹', '歎', '鵬', '毞', '豊', '亥', '青', '磊', '嬅',
                '奈', '亞', '雅', '客', '氙', '咚', '寅', '博', '柏', '伯',
                '猛', '瑟', '法', '麝', '濡', '茹', '賈', '思', '司', '帛',
    ]
    name_else = [ 'John', 'Joan', 'William', 'Neal', 'Gordon', 'Howard', 'Mary',
                  'Richard', 'Mary', 'Jane', 'Adrian']
    
    a = [choice(numbers) for _ in range(8)]
    b = [choice(letters) for _ in range(2)]
    c = [choice(numbers) for _ in range(5)]
    
    password_list = a + b
    shuffle(password_list)
    password = "".join(password_list)

    email_list = a + b
    shuffle(email_list)
    email = "".join(email_list)
    
    phone_list = a
    phone = "".join(phone_list)

    idcard_list = b[0:1]+a
    idCard = "".join(idcard_list)

    postalCode_list = c
    postalCode = "".join(postalCode_list)

    firstname_zh = choice(name_zh)+choice(name_zh)
    lastname_zh = choice(['陳', '吳', '謝', '劉'])
    firstname_else = choice(name_else)
    lastname_else = choice(['Chen', 'Kim', 'Walker', 'Wilson', 'Brown', 'Smith'])

    city = choice(["雲林縣", "台北市", "台南市", "新北市", "宜蘭縣"])
    load = choice(["仲山路", "仁心路", "清信路", "忠港路", "幸益路", "汀周路", "司大路", "滑興路", "民竹路", "和貧路"])
    nnnn = choice(["一段5號", "168號", "52號", "45號", "二段10號", "32號"])
    address_list = city + load + nnnn
    address = "".join(address_list)

    date1 = [ "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    date2 = [ "13", "14", "15", "16", "28", "18", "19", "20", "25", "22", "23", "24"]
    
    y = choice(["2000", "2001", "2002", "2003", "1999"])
    m = choice(date1)
    d = choice(date1 + date2)
    birthday_list = y + "-" + m + "-" + d
    birthday = "".join(birthday_list)
    if nationality == 'Taiwan':
        new_member_data = {
            str(i):{
                "email": email+"@gmail.com",
                "phone": "+886-9"+phone,
                "password": password,
                "firstName": firstname_zh, 
                "middleName": "",
                "lastName": lastname_zh,
                "gender": choice(["Male","Female"]), 
                "birthday": birthday, 
                "applyInfo": {
                    "idCard": IDcard.createIDcard(), 
                    "bornAddress": {
                        "country": "Taiwan",
                        "postalCode": postalCode,
                        "city": city, 
                        "address": address
                    }
                },
                "role": choice(["Admin" , "PM" , "Reviewer" , "Applicant"]), 
                "nationality": "Taiwan"
            }
        }
    else :
        new_member_data = {
            str(i):{
                "email": email+"@gmail.com",
                "phone": "+886-9"+ phone,
                "password": password,
                "firstName": firstname_else, 
                "middleName": "",
                "lastName": lastname_else,
                "gender": choice(["Male","Female"]), 
                "birthday": birthday, 
                "applyInfo": {
                    "idCard": idCard, 
                    "bornAddress": {
                        "country": nationality,
                        "postalCode": postalCode,
                        "city": city, 
                        "address": address
                    }
                },
                "role": choice(["Admin" , "PM" , "Reviewer" , "Applicant"]), 
                "nationality": nationality
            }
        }
# output
    try:
        with open("data.json", "r", encoding="utf-8") as password_file:
            password_data = json.load(password_file)
    except:
        with open("data.json", "w", encoding="utf-8") as password_file:
            json.dump(new_member_data, password_file, indent=4, ensure_ascii=False)
    else:
        password_data.update(new_member_data)
        with open("data.json", "w", encoding="utf-8") as password_file:
            json.dump(password_data, password_file, indent=4, ensure_ascii=False)
