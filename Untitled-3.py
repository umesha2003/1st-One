
result = "import requests

url = "https://raw.githubusercontent.com/umesha2003/1st-One/refs/heads/main/Untitled-1.py"

try:
    
    response = requests.get(url)

    
    if response.status_code == 200:
        
        with open("downloaded_hello.py", "w") as file:
            file.write(response.text)
        print("Script downloaded successfully! Check 'downloaded_hello.py'.")
    else:
        print(f"Failed to fetch the file. HTTP Status Code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")"


with open("output.txt", "w") as file:
    file.write(result)
