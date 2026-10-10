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
        "http://127.0.0.1:8000/exercicio_4/index.html",
        "http://127.0.0.1:8000/index.html",
        "http://127.0.0.1:8000/"
    ]
    for url in urls:
        try:
            resposta = requests.get(url, timeout=3)
            if resposta.status_code == 200:
                resposta.encoding = "utf-8"
                if "livro" in resposta.text.lower() or "biblioteca" in resposta.text.lower():
                    return resposta.text, url
        except requests.exceptions.RequestException:
            continue
    return None, None

def main():
    print("=" * 60)
    print("Exercício 4 — Biblioteca (Raspagem com BeautifulSoup)")
    print("=" * 60)

    html, url_usada = obter_conteudo()
    if not html:
        print("[ERRO] Não foi possível conectar ao servidor local na porta 8000.")
        print("Certifique-se de iniciar o servidor HTTP local com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        return

    print(f"[OK] Página obtida com sucesso a partir de: {url_usada}\n")

    soup = BeautifulSoup(html, "html.parser")
    elementos_livros = soup.find_all("article", class_="livro")

    livros = []

    print("--- ACERVO COMPLETO DE LIVROS ---\n")
    for idx, elemento in enumerate(elementos_livros, start=1):
        titulo = elemento.find("h2", class_="livro-titulo").get_text(strip=True)
        autor = elemento.find("span", class_="livro-autor").get_text(strip=True)
        ano = elemento.find("span", class_="livro-ano").get_text(strip=True)
        genero = elemento.find("span", class_="livro-genero").get_text(strip=True)
        status = elemento.find("span", class_="livro-status").get_text(strip=True)

        # Percorrendo a lista de palavras-chave
        lista_kw = elemento.find("ul", class_="palavras-chave")
        palavras_chave = [li.get_text(strip=True) for li in lista_kw.find_all("li")] if lista_kw else []

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "genero": genero,
            "status": status,
            "palavras_chave": palavras_chave
        }
        livros.append(livro)

        print(f"[{idx}] {titulo}")
        print(f"    Autor:          {autor}")
        print(f"    Ano:            {ano}")
        print(f"    Gênero:         {genero}")
        print(f"    Situação:       {status}")
        print(f"    Palavras-chave: {', '.join(palavras_chave)}")
        print("-" * 50)

    # Apresentando separadamente apenas os livros que estejam disponíveis
    print("\n--- LIVROS DISPONÍVEIS PARA EMPRÉSTIMO ---")
    livros_disponiveis = [livro for livro in livros if livro["status"].lower() == "disponível"]

    for l in livros_disponiveis:
        print(f"\n[DISPONÍVEL] Título: {l['titulo']}")
        print(f"             Autor:  {l['autor']} ({l['ano']})")
        print(f"             Gênero: {l['genero']}")
        print(f"             Tags:   {', '.join(l['palavras_chave'])}")

    print(f"\nTotal disponível: {len(livros_disponiveis)} de {len(livros)} livros no catálogo.")

if __name__ == "__main__":
    main()

