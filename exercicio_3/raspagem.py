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
        "http://127.0.0.1:8000/exercicio_3/index.html",
        "http://127.0.0.1:8000/index.html",
        "http://127.0.0.1:8000/"
    ]
    for url in urls:
        try:
            resposta = requests.get(url, timeout=3)
            if resposta.status_code == 200:
                resposta.encoding = "utf-8"
                if "noticia" in resposta.text.lower() or "infonews" in resposta.text.lower():
                    return resposta.text, url
        except requests.exceptions.RequestException:
            continue
    return None, None

def main():
    print("=" * 60)
    print("Exercício 3 — Portal de notícias (Raspagem com BeautifulSoup)")
    print("=" * 60)

    html, url_usada = obter_conteudo()
    if not html:
        print("[ERRO] Não foi possível conectar ao servidor local na porta 8000.")
        print("Certifique-se de iniciar o servidor HTTP local com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        return

    print(f"[OK] Página obtida com sucesso a partir de: {url_usada}\n")

    soup = BeautifulSoup(html, "html.parser")
    artigos = soup.find_all("article", class_="noticia")

    noticias = []

    print("--- TODAS AS NOTÍCIAS PUBLICADAS ---\n")
    for i, artigo in enumerate(artigos, start=1):
        categoria = artigo.find("span", class_="noticia-categoria").get_text(strip=True)
        titulo = artigo.find("h2", class_="noticia-titulo").get_text(strip=True)
        data = artigo.find("time", class_="noticia-data").get_text(strip=True)
        autor = artigo.find("span", class_="noticia-autor").get_text(strip=True)
        resumo = artigo.find("p", class_="noticia-resumo").get_text(strip=True)

        noticia = {
            "categoria": categoria,
            "titulo": titulo,
            "data": data,
            "autor": autor,
            "resumo": resumo
        }
        noticias.append(noticia)

        # Apresenta cada notícia em um bloco de saída organizado
        print(f"+-- [Notícia {i}] ------------------------------------------")
        print(f"| Categoria: {categoria}")
        print(f"| Título:    {titulo}")
        print(f"| Data:      {data} | Autor: {autor}")
        print(f"| Resumo:    {resumo}")
        print("+---------------------------------------------------------\n")

    # Filtro por categoria escolhida (exemplo: 'Tecnologia')
    categoria_alvo = "Tecnologia"
    print(f"--- NOTÍCIAS DA CATEGORIA '{categoria_alvo.upper()}' ---")
    titulos_categoria = [n["titulo"] for n in noticias if n["categoria"].lower() == categoria_alvo.lower()]

    for idx, titulo in enumerate(titulos_categoria, start=1):
        print(f"  {idx}. {titulo}")

    if not titulos_categoria:
        print(f"Nenhuma notícia encontrada para a categoria '{categoria_alvo}'.")

if __name__ == "__main__":
    main()

