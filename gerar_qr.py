#!/usr/bin/env python3
"""
Gera o QR code do pôster em formato vetorial (SVG e PDF) e em PNG de alta resolução.

Uso:
    pip install segno
    python gerar_qr.py https://tiagochavo87.github.io/poster/

Saídas (na pasta atual):
    qr_poster.svg  -> use este no Illustrator/Inkscape/PowerPoint do pôster
    qr_poster.pdf  -> alternativa vetorial para LaTeX/InDesign
    qr_poster.png  -> 1200 px, só se a diagramação não aceitar vetor

Regras de impressão já aplicadas:
    - correção de erro nível M (equilíbrio entre robustez e densidade)
    - quiet zone de 4 módulos (borda branca obrigatória; sem ela o leitor falha)
    - preto puro sobre branco puro (não use cores do laboratório no QR)
"""

import sys
import segno

URL_PADRAO = "https://tiagochavo87.github.io/poster/"


def main() -> int:
    url = sys.argv[1] if len(sys.argv) > 1 else URL_PADRAO

    if not url.startswith(("http://", "https://")):
        print(f"URL inválida: {url!r} — precisa começar com https://")
        return 1

    qr = segno.make(url, error="m")

    qr.save("qr_poster.svg", scale=10, border=4, dark="#000000", light="#FFFFFF")
    qr.save("qr_poster.pdf", scale=10, border=4, dark="#000000", light="#FFFFFF")
    qr.save("qr_poster.png", scale=40, border=4, dark="#000000", light="#FFFFFF")

    print(f"URL codificada : {url}")
    print(f"Versão do QR   : {qr.version} ({qr.symbol_size(scale=1, border=0)[0]} módulos)")
    print("Arquivos       : qr_poster.svg, qr_poster.pdf, qr_poster.png")
    print()
    print("Tamanho no pôster: mínimo 5 cm de lado; 6–7 cm é o confortável para")
    print("leitura a ~1 m de distância. Não reduza abaixo disso nem recorte a borda branca.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
