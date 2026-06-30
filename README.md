# 🛡️ Path Traversal Scanner
---
Este é um script automatizado desenvolvido em Python para realizar testes de segurança de aplicações web, focando especificamente na detecção de vulnerabilidades de Path Traversal **(também conhecida como Directory Traversal)**.

---
### 🧑‍💻️ Sobre o Projeto

E meu primeiro script oficial. O script automatiza o envio de payloads variados para testar se uma aplicação expõe arquivos sensíveis do sistema (como /etc/passwd) através de manipulação de caminhos de diretório. É uma ferramenta de automação para auxiliar em auditorias de segurança e validação de vulnerabilidades.

---
## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

|Bibliotecas|Versão|
|-----------|------|
|Requests | 2.32.5 |

---
## 💻️ Como Utilizar

```

git clone https://github.com/seu-usuario/seu-repositorio.github

pip install requests

python3 scanner.py

```

**Entrada de Dados:**

- Insira a URL alvo.

- Defina o número de tentativas de payloads.

- Informe o código de status HTTP esperado para sucesso.

---

## 📊 Especificações Técnicas

| Recurso | Descrição |
|--|--|
| Objetivo | Detecção de Path Traversal |
| Payload Padrão | ../../etc/passwd |
| Customização | Profundidade dinâmica (1 a 30 níveis) |
| Headers | User-Agent configurado (Browser emulation) |

---

## 👾️ Euzinho

Acompanhe meu trabalho!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michael-reis-2a909541a/)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/michael-reissp)

