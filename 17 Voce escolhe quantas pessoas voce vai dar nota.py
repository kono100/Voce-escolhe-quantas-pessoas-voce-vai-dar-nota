# Voce escolhe quantas pessoas voce vai dar nota 

alunos=int(input("Quantos alunos na turma? "))

count=1; soma = 0.0
while count <= alunos:
    
    print(f"Nota do aluno{count} ")
    nota = float( input() )
    
    soma += nota
    count += 1

print(f"Media da turma: {(soma/alunos)} ")
