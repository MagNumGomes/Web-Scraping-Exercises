import sys
import requests
from bs4 import BeautifulSoup

# Garante suporte a UTF-8 na saída do console no Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def obter_conteudo():
    urls = [
        "http://127.0.0.1:8000/exercicio_2/index.html",
        "http://127.0.0.1:8000/index.html",
        "http://127.0.0.1:8000/"
    ]
    for url in urls:
        try:
            resposta = requests.get(url, timeout=3)
            if resposta.status_code == 200:
                resposta.encoding = "utf-8"
                if "produto" in resposta.text.lower():
                    return resposta.text, url
        except requests.exceptions.RequestException:
            continue
    return None, None

def main():
    print("=" * 60)
    print("Exercício 2 — Loja de informática (Raspagem com BeautifulSoup)")
    print("=" * 60)

    html, url_usada = obter_conteudo()
    if not html:
        print("[ERRO] Não foi possível conectar ao servidor local na porta 8000.")
        print("Certifique-se de iniciar o servidor HTTP local com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        return

    print(f"[OK] Página obtida com sucesso a partir de: {url_usada}\n")

    soup = BeautifulSoup(html, "html.parser")
    elementos_produtos = soup.find_all("div", class_="produto")

    todos_produtos = []

    for elemento in elementos_produtos:
        nome = elemento.find("h2", class_="produto-nome").get_text(strip=True)
        fabricante = elemento.find("span", class_="fabricante").get_text(strip=True)
        categoria = elemento.find("span", class_="categoria").get_text(strip=True)
        preco = elemento.find("p", class_="produto-preco").get_text(strip=True)
        situacao = elemento.find("span", class_="situacao-estoque").get_text(strip=True)

        todos_produtos.append({
            "nome": nome,
            "fabricante": fabricante,
            "categoria": categoria,
            "preco": preco,
            "situacao": situacao
        })

    # 1. Apresentando todos os produtos de forma organizada
    print("--- TODOS OS PRODUTOS CADASTRADOS ---")
    for i, prod in enumerate(todos_produtos, start=1):
        print(f"[{i}] {prod['nome']}")
        print(f"    Fabricante: {prod['fabricante']}")
        print(f"    Categoria:  {prod['categoria']}")
        print(f"    Preço:      {prod['preco']}")
        print(f"    Estoque:    {prod['situacao']}")
        print("-" * 40)

    # 2. Exibindo separadamente apenas os produtos com situação 'Disponível'
    print("\n--- PRODUTOS DISPONÍVEIS EM ESTOQUE ---")
    produtos_disponiveis = [p for p in todos_produtos if p['situacao'].lower() == "disponível"]

    for prod in produtos_disponiveis:
        print(f"  [DISPONÍVEL] {prod['nome']} - {prod['preco']} (Fabricante: {prod['fabricante']})")

    print(f"\nTotal disponível: {len(produtos_disponiveis)} de {len(todos_produtos)} produtos.")

if __name__ == "__main__":
    main()

