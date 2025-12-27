def limpar_resposta(texto: str) -> str:
    lixo = [
        "como um modelo de linguagem",
        "não tenho sentimentos",
        "sou uma ia",
        "não posso"
    ]

    for l in lixo:
        texto = texto.replace(l, "")

    return texto.strip()
