import random
import pprint
import json
import csv

nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Lucas", "Mariana", "Nicolas", "Olivia", "Paulo", "Renata", "Samuel", "Tatiane", "Vinicius", "Yasmin"
]

sobrenomes = [
    "Silva", "Souza", "Oliveira", "Santos", "Pereira", "Costa", "Rodrigues", "Almeida", "Nascimento", "Lima"
]

turnos = ["Manhã", "Tarde", "Noite"]
periodos = [1, 2, 3, 4, 5]

alunos = {}

# 🔹 Gerando os dados
for i in range(1, 2001):
    alunos[f"aluno_{i}"] = {
        "nome": f"{random.choice(nomes)} {random.choice(sobrenomes)}",
        "turno": random.choice(turnos),
        "periodo": random.choice(periodos),
        "notas": [round(random.uniform(0, 10), 1) for _ in range(3)]
    }

# 🔹 1. Salvar como arquivo Python (BONITO)
with open("alunos.py", "w", encoding="utf-8") as f:
    f.write("alunos = ")
    f.write(pprint.pformat(alunos, indent=4, width=120))

# 🔹 2. Salvar como JSON
with open("alunos.json", "w", encoding="utf-8") as f:
    json.dump(alunos, f, indent=4, ensure_ascii=False)

# 🔹 3. Salvar como CSV (formato tabular)
with open("alunos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nome", "turno", "periodo", "nota1", "nota2", "nota3"])
    
    for aluno_id, dados in alunos.items():
        writer.writerow([
            aluno_id,
            dados["nome"],
            dados["turno"],
            dados["periodo"],
            dados["notas"][0],
            dados["notas"][1],
            dados["notas"][2]
        ])

print("Arquivos gerados: alunos.py, alunos.json, alunos.csv")