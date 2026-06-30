# 🤝 Guia de Contribuição (Contributing Guide)

Primeiramente, muito obrigado por demonstrar interesse em contribuir para o **Path Traversal Scanner**! ✨

Este é um projeto de código aberto voltado para segurança ofensiva ética e automação de testes. Toda contribuição desde a correção de um erro ortográfico na documentação até a reestruturação do código para Programação Orientada a Objetos é extremamente valiosa.

Este guia serve para orientar o processo de contribuição de forma clara e organizada, garantindo a qualidade do código e a consistência do projeto.

---

## 🚀 Como Posso Contribuir?

Você pode apoiar o desenvolvimento do projeto de várias maneiras:

1. **Relatando Bugs (Bug Reports):** Se você encontrar uma falha, comportamento inesperado ou travamento (crash) no script, abra uma *Issue* descrevendo o problema, o ambiente onde ocorreu e os passos para reproduzi-lo.
2. **Sugerindo Melhorias (Feature Requests):** Tem uma ideia para uma nova funcionalidade? (Ex: suporte a múltiplos alvos, exportação de relatórios em JSON/CSV, paralelismo com Threads, suporte a proxies). Abra uma *Issue* para debatermos.
3. **Melhorando a Documentação:** Correções no `README.md`, tradução da documentação para inglês, ou comentários explicativos no código.
4. **Escrevendo Código:** Implementando correções de bugs ou novas funcionalidades diretamente.

---

## 🛠️ Passo a Passo para Contribuir (Fluxo de Trabalho Git)

Seguimos o fluxo padrão de Bifurcação (*Fork & Pull Request*) no GitHub:

### 1. Faça um Fork do Repositório
Clique no botão **Fork** no canto superior direito da página do repositório para criar uma cópia do projeto na sua conta pessoal do GitHub.

### 2. Clone o seu Fork localmente
Abra o terminal na sua máquina e clone o repositório que agora está na sua conta:
```bash
git clone https://github.com/SEU-USUARIO/path-traversal-scanner.git
cd path-traversal-scanner
```

### 3. Crie uma Branch para suas alterações
Nunca faça alterações diretamente na branch `main`. Crie uma branch específica e descritiva para o que você vai desenvolver:
```bash
# Para novas funcionalidades
git checkout -b feature/nome-da-melhoria

# Para correção de bugs
git checkout -b fix/nome-do-bug
```

### 4. Configure o Ambiente de Testes
Recomenda-se o uso de um ambiente virtual para garantir que as dependências não interfiram no seu sistema global:
```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# ou
.\venv\Scripts\activate  # No Windows

pip install -r requirements.txt
```

### 5. Desenvolva e Teste suas alterações
* Escreva seu código mantendo o padrão visual e de identação já existente.
* Faça testes manuais executando o script para garantir que a funcionalidade adicionada funciona e não quebrou as regras anteriores.

### 6. Faça o Commit das suas alterações
Utilize mensagens de commit claras e preferencialmente baseadas no padrão de **Conventional Commits**:
```bash
git commit -m "feat: adiciona tratamento de timeout nas requisições HTTP"
git commit -m "fix: corrige loop infinito quando a URL não possui barra final"
```

### 7. Envie as alterações para o seu GitHub (Push)
```bash
git push origin feature/nome-da-melhoria
```

### 8. Abra um Pull Request (PR)
Vá até a página original do repositório no GitHub. Uma barra amarela indicará que você fez push em uma nova branch. Clique em **Compare & pull request**.
* Adicione um título claro que resuma a alteração.
* Na descrição, explique detalhadamente o que foi feito e o porquê.
* Aguarde a revisão do código!

---

## 📋 Boas Práticas e Padrões de Código

Para manter o projeto limpo e legível para a comunidade, buscamos seguir as seguintes diretrizes:

* **Estilo de Código:** Siga as recomendações da **PEP 8** para nomenclatura de variáveis e funções em Python (ex: `camel_case` para variáveis e funções, `PascalCase` para classes se houver).
* **Tratamento de Exceções:** Sempre preveja falhas de rede (como quedas de conexão ou timeouts) utilizando blocos `try/except`. O programa nunca deve quebrar abruptamente (crash) de forma descontrolada.
* **Segurança:** Nunca inclua dados sensíveis, chaves de API reais ou URLs privadas de alvos nos commits ou testes de código.
* **Mensagens no Terminal:** Mantenha os prints informativos, limpos e organizados de forma visual para o usuário final.

---

## ⚖️ Código de Conduta

Como um projeto educacional e focado em cibersegurança, estabelecemos um ambiente seguro e inclusivo:
* **Respeito Mútuo:** Seja cordial e paciente nas discussões de Issues e Pull Requests.
* **Uso Ético:** Este projeto promove exclusivamente o aprendizado de segurança cibernética e testes de intrusão autorizados. Não toleramos discussões ou contribuições focadas em atividades cibernéticas maliciosas ou ilegais.

---
