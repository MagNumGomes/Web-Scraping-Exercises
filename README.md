# Lista de Exercícios — HTML, DOM e Beautiful Soup

Este repositório contém a resolução completa dos 6 exercícios propostos na lista.

Cada exercício foi organizado em sua respectiva pasta, contendo:
- `index.html`: A página desenvolvida com estrutura HTML semântica e estilização limpa.
- `raspagem.py`: Script Python com requisição HTTP via `requests` e extração dos dados usando `BeautifulSoup`.

---

## Como Executar

### 1. Iniciar o servidor HTTP local
Abra o terminal na pasta raiz do projeto (`Nova pasta`) e execute o comando indicado nas orientações da lista:

```bash
python -m http.server --bind 127.0.0.1 8000
```

### 2. Executar os scripts de raspagem
Em outro terminal (na mesma pasta raiz), execute o script de qualquer um dos exercícios:

```bash
python exercicio_1/raspagem.py
python exercicio_2/raspagem.py
python exercicio_3/raspagem.py
python exercicio_4/raspagem.py
python exercicio_5/raspagem.py
python exercicio_6/raspagem.py
```

*(Obs: Os scripts também funcionam se você entrar na pasta do exercício e executá-los diretamente).*

---

## Estrutura dos Exercícios

### [Exercício 1 — Catálogo de cursos](./exercicio_1/)
- **HTML (`index.html`)**: Escola fictícia com 4 cursos, contendo nome, área, carga horária e lista `<ul>` com 3 assuntos estudados.
- **Script (`raspagem.py`)**: Localiza os cursos, extrai metadados e itera sobre a lista de assuntos exibindo-os organizadamente.

### [Exercício 2 — Loja de informática](./exercicio_2/)
- **HTML (`index.html`)**: Catálogo com 5 produtos contendo nome, fabricante, categoria, preço e situação de estoque (`Disponível`, `Estoque baixo`, `Indisponível`).
- **Script (`raspagem.py`)**: Extrai todos os produtos e ao final filtra e exibe separadamente apenas os produtos com situação `Disponível`.

### [Exercício 3 — Portal de notícias](./exercicio_3/)
- **HTML (`index.html`)**: Portal com 4 notícias utilizando tags semânticas (`<article>`, `<h2>`, `<time>`, `<p>`) com categoria, título, data, autor e resumo.
- **Script (`raspagem.py`)**: Apresenta as notícias em blocos formatados e lista os títulos pertencentes à categoria filtrada (`Tecnologia`).

### [Exercício 4 — Biblioteca](./exercicio_4/)
- **HTML (`index.html`)**: Acervo com 4 livros contendo título, autor, ano, gênero, situação de empréstimo (`Disponível` / `Emprestado`) e lista de palavras-chave.
- **Script (`raspagem.py`)**: Extrai os campos e a lista de tags/palavras-chave de cada livro, exibindo separadamente os livros disponíveis para empréstimo.

### [Exercício 5 — Cardápio por categorias](./exercicio_5/)
- **HTML (`index.html`)**: Cardápio de restaurante dividido em 3 seções (`Pratos`, `Bebidas` e `Sobremesas`), cada qual com nome, descrição e preço de cada item.
- **Script (`raspagem.py`)**: Localiza primeiro as seções e depois percorre os itens de cada uma, preservando a hierarquia de categorias na saída.

### [Exercício 6 — Agenda de eventos](./exercicio_6/)
- **HTML (`index.html`)**: Agenda com 5 eventos com nome, data, horário, local, palestrantes e link de inscrição. Eventos possuem um ou mais palestrantes em elementos separados.
- **Script (`raspagem.py`)**: Extrai texto e `href` dos links de inscrição e identifica quais eventos possuem mais de um palestrante.

