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
        "http://127.0.0.1:8000/exercicio_5/index.html",
        "http://127.0.0.1:8000/index.html",
        "http://127.0.0.1:8000/"
    ]
    for url in urls:
        try:
            resposta = requests.get(url, timeout=3)
            if resposta.status_code == 200:
                resposta.encoding = "utf-8"
                if "cardapio" in resposta.text.lower() or "cardápio" in resposta.text.lower():
                    return resposta.text, url
        except requests.exceptions.RequestException:
            continue
    return None, None

def main():
    print("=" * 60)
    print("Exercício 5 — Cardápio por categorias (Raspagem com BeautifulSoup)")
    print("=" * 60)

    html, url_usada = obter_conteudo()
    if not html:
        print("[ERRO] Não foi possível conectar ao servidor local na porta 8000.")
        print("Certifique-se de iniciar o servidor HTTP local com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        return

    print(f"[OK] Página obtida com sucesso a partir de: {url_usada}\n")

    soup = BeautifulSoup(html, "html.parser")

    # 1. Primeiro localiza cada seção do cardápio
    secoes = soup.find_all("section", class_="secao-cardapio")

    print(f"Total de seções encontradas: {len(secoes)}\n")

    # 2. Percorre cada seção preservando a organização por categoria
    for secao in secoes:
        categoria_nome = secao.find("h2", class_="categoria-titulo").get_text(strip=True)
        print("=" * 50)
        print(f"CATEGORIA: {categoria_nome.upper()}")
        print("=" * 50)

        # 3. Percorre apenas os itens pertencentes àquela seção
        itens = secao.find_all("div", class_="item-prato")
        for i, item in enumerate(itens, start=1):
            nome = item.find("span", class_="item-nome").get_text(strip=True)
            descricao = item.find("p", class_="item-descricao").get_text(strip=True)
            preco = item.find("span", class_="item-preco").get_text(strip=True)

            print(f"  {i}. {nome} - {preco}")
            print(f"     Descrição: {descricao}")
        print()

if __name__ == "__main__":
    main()

