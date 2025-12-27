import json
import os

class Memory:
    def __init__(self, file="memory.json"):
        self.file = file

        if not os.path.exists(self.file):
            self.data = {
                "name": None,
                "facts": [],
                "emotions": {}
            }
            self.save()
        else:
            with open(self.file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                self.data = json.loads(content) if content else {
                    "name": None,
                    "facts": [],
                    "emotions": {}
                }

    def save(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def context(self):
        ctx = ""
        if self.data.get("name"):
            ctx += f"O nome do usuário é {self.data['name']}.\n"
        for fact in self.data.get("facts", []):
            ctx += f"- {fact}\n"
        return ctx
