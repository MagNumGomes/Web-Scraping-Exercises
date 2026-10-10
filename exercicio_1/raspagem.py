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
        "http://127.0.0.1:8000/exercicio_1/index.html",
        "http://127.0.0.1:8000/index.html",
        "http://127.0.0.1:8000/"
    ]
    for url in urls:
        try:
            resposta = requests.get(url, timeout=3)
            if resposta.status_code == 200:
                resposta.encoding = "utf-8"
                if "curso" in resposta.text.lower():
                    return resposta.text, url
        except requests.exceptions.RequestException:
            continue
    return None, None

def main():
    print("=" * 60)
    print("Exercício 1 — Catálogo de cursos (Raspagem com BeautifulSoup)")
    print("=" * 60)

    html, url_usada = obter_conteudo()
    if not html:
        print("[ERRO] Não foi possível conectar ao servidor local na porta 8000.")
        print("Certifique-se de iniciar o servidor HTTP local com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        return

    print(f"[OK] Página obtida com sucesso a partir de: {url_usada}\n")

    soup = BeautifulSoup(html, "html.parser")
    cursos = soup.find_all("div", class_="curso")

    print(f"Total de cursos encontrados: {len(cursos)}\n")

    for indice, curso in enumerate(cursos, start=1):
        # Extração de nome, área e carga horária
        nome = curso.find("h2", class_="curso-nome").get_text(strip=True)
        area = curso.find("p", class_="curso-area").get_text(strip=True)
        carga = curso.find("p", class_="curso-carga").get_text(strip=True)

        print(f"--- Curso {indice}: {nome} ---")
        print(f"  {area}")
        print(f"  {carga}")
        print("  Assuntos estudados:")

        # Percorrendo a lista de assuntos
        lista_assuntos = curso.find("ul", class_="curso-assuntos")
        itens = lista_assuntos.find_all("li")
        for item in itens:
            print(f"    - {item.get_text(strip=True)}")
        print()

if __name__ == "__main__":
    main()

