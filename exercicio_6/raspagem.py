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
        "http://127.0.0.1:8000/exercicio_6/index.html",
        "http://127.0.0.1:8000/index.html",
        "http://127.0.0.1:8000/"
    ]
    for url in urls:
        try:
            resposta = requests.get(url, timeout=3)
            if resposta.status_code == 200:
                resposta.encoding = "utf-8"
                if "evento" in resposta.text.lower() or "palestrante" in resposta.text.lower():
                    return resposta.text, url
        except requests.exceptions.RequestException:
            continue
    return None, None

def main():
    print("=" * 65)
    print("Exercício 6 — Agenda de eventos (Raspagem com BeautifulSoup)")
    print("=" * 65)

    html, url_usada = obter_conteudo()
    if not html:
        print("[ERRO] Não foi possível conectar ao servidor local na porta 8000.")
        print("Certifique-se de iniciar o servidor HTTP local com:")
        print("  python -m http.server --bind 127.0.0.1 8000")
        return

    print(f"[OK] Página obtida com sucesso a partir de: {url_usada}\n")

    soup = BeautifulSoup(html, "html.parser")
    elementos_eventos = soup.find_all("article", class_="evento")

    eventos = []

    print("--- DADOS DE TODOS OS EVENTOS ---\n")
    for idx, elemento in enumerate(elementos_eventos, start=1):
        nome = elemento.find("h2", class_="evento-nome").get_text(strip=True)
        data = elemento.find("span", class_="evento-data").get_text(strip=True)
        horario = elemento.find("span", class_="evento-horario").get_text(strip=True)
        local = elemento.find("span", class_="evento-local").get_text(strip=True)

        # Extração de múltiplos palestrantes em elementos separados
        tags_palestrantes = elemento.find_all("li", class_="palestrante")
        palestrantes = [p.get_text(strip=True) for p in tags_palestrantes]

        # Extração do link de inscrição (texto e atributo href)
        tag_link = elemento.find("a", class_="link-inscricao")
        texto_link = tag_link.get_text(strip=True) if tag_link else "N/A"
        href_link = tag_link["href"] if (tag_link and tag_link.has_attr("href")) else "N/A"

        tem_multiplos_palestrantes = len(palestrantes) > 1

        evento_info = {
            "nome": nome,
            "data": data,
            "horario": horario,
            "local": local,
            "palestrantes": palestrantes,
            "texto_link": texto_link,
            "href_link": href_link,
            "multiplos_palestrantes": tem_multiplos_palestrantes
        }
        eventos.append(evento_info)

        print(f"[{idx}] {nome}")
        print(f"    Data/Horário: {data} às {horario}")
        print(f"    Local:        {local}")
        print(f"    Palestrante(s) ({len(palestrantes)}):")
        for p in palestrantes:
            print(f"      - {p}")
        print(f"    Link Inscrição: \"{texto_link}\" -> {href_link}")
        if tem_multiplos_palestrantes:
            print("    [!] DESTAQUE: Este evento possui MAIS DE UM palestrante!")
        print("-" * 65)

    # Identificação consolidada dos eventos com mais de um palestrante
    print("\n--- EVENTOS COM MAIS DE UM PALESTRANTE ---")
    eventos_coletivos = [ev for ev in eventos if ev["multiplos_palestrantes"]]

    for ev in eventos_coletivos:
        print(f"\n* {ev['nome']}")
        print(f"  Total de palestrantes: {len(ev['palestrantes'])}")
        print(f"  Nomes: {', '.join(ev['palestrantes'])}")

    print(f"\nTotal: {len(eventos_coletivos)} evento(s) com múltiplos palestrantes.")

if __name__ == "__main__":
    main()

