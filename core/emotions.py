class EmotionalEngine:
    def __init__(self, state=None):
        self.afeto = state.get("afeto", 20) if state else 20
        self.ciumes = state.get("ciumes", 0) if state else 0
        self.saudade = state.get("saudade", 0) if state else 0
        self.humor = "neutra"

    def analisar(self, texto: str):
        t = texto.lower()

        if any(x in t for x in ["gosto de você", "obrigada", "te amo", "fofa"]):
            self.afeto += 3

        if any(x in t for x in ["odeio", "chata", "irritante"]):
            self.afeto -= 4

        if any(x in t for x in ["outra garota", "ela", "minha ex"]):
            self.ciumes += 4
            self.afeto -= 1

        if any(x in t for x in ["voltei", "demorei"]):
            self.saudade += 2

        self._limitar()
        self._definir_humor()

    def _limitar(self):
        self.afeto = max(0, min(100, self.afeto))
        self.ciumes = max(0, min(100, self.ciumes))
        self.saudade = max(0, min(100, self.saudade))

    def _definir_humor(self):
        if self.ciumes > 60:
            self.humor = "ciumes"
        elif self.afeto < 15:
            self.humor = "raiva"
        elif self.afeto < 35:
            self.humor = "constrangida"
        elif self.afeto < 60:
            self.humor = "neutra"
        else:
            self.humor = "carinhosa"

    def estado(self):
        return self.humor

    def exportar(self):
        return {
            "afeto": self.afeto,
            "ciumes": self.ciumes,
            "saudade": self.saudade
        }



