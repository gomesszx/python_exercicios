alunos = {}

for _ in range(5):
    notasra = [] 
    ra = input("Aluno:")
    nota1, nota2, nota3 = input('Notas: ').split()
    
    nota1 = int(nota1)
    nota2 = int(nota2)
    nota3 = int(nota3)

    notasra.append(nota1)
    notasra.append(nota2)
    notasra.append(nota3)

    alunos[ra] = notasra

for aluno in alunos:
    somaNotas = alunos[aluno]
    media = sum(somaNotas) / 3
    print(f"Aluno: {aluno} teve a media de {media:.2f}")




    
