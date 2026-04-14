# #_____________________1_________________________1
import requests
def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url)# Gửi yêu cầu GET tới API

        # Kiểm tra nếu yêu cầu thành công (status code 200 là good chạy ngon)
        if response.status_code == 200:
            # Chuyển đổi dữ liệu nhận được sang định dạng JSON
            data = response.json()


            # in ra nội dung câu joke
            print(data['value'])
        else:
            print("error: cannot connect to API.")

    except Exception as e:
        print(f"error: {e}")


# Chạy chương trình
if __name__ == "__main__":
    get_chuck_norris_joke()
#_____________________2________________________2______
import requests

city_name = input("Nhập tên thành phố: ")
api_key = "c7226dbdd14114bb6cd21ba7b7728cae"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=vi"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Thời tiết: {data['weather'][0]['description']}")
    print(f"Nhiệt độ: {data['main']['temp']}°C")
else:
    print("Lỗi rồi! Có thể Key chưa kích hoạt hoặc sai tên thành phố.")
# #-------------------------3----------------
from flask import Flask, json
app = Flask(__name__)
@app.route('/prime_number/<int:number>')
def is_prime_endpoint(number):
    result = {
        "Number": number,
        "isPrime": check_prime(number)
    }

    return json.dumps(result)

def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
# #-----------------------4-----------------------4
from flask import Flask, json

app = Flask(__name__)
@app.route('/airport/<string:icao>')
def get_airport(icao):
    result = find_airport_in_file(icao)

    if result == "FILE_ERROR":
        return json.dumps({"message": "Server file error"})

    if result:
        return json.dumps(result), 200
    else:
        return json.dumps({"message": "Airport not found"})

def find_airport_in_file(icao_to_find):
    try:
        with open('airports.txt', 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')

                if len(parts) == 4 and parts[0].upper() == icao_to_find.upper():
                    return {
                        "icao": parts[0],
                        "name": parts[1],
                        "city": parts[2],
                        "country": parts[3]
                    }
        return None
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file airports.txt")
        return "FILE_ERROR"
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)