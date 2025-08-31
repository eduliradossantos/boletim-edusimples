# Boletim EduSimples

Este projeto faz parte do **Desafio 1 - Fundamentos do Python** do programa **COMPET Médio SophIA**, realizado entre **25 de agosto de 2025 e 25 de setembro de 2025** na **Escola Técnica Estadual Porto Digital**, sob orientação do professor **André Ribeiro**.

## Objetivo

O sistema **Boletim EduSimples** permite cadastrar, listar, alterar e excluir alunos, exibindo suas notas, média e situação (aprovado, recuperação ou reprovado).

## Funcionalidades

- Cadastrar aluno (matrícula, nome, notas)
- Listar alunos com média e situação
- Alterar dados de um aluno (nome ou notas)
- Excluir aluno
- Tratamento de erros (validação de notas e entradas inválidas)

## Estrutura do Código

- Uso de funções (`cadastrar`, `listar`, `alterar`, `excluir`, `media`, `situacao`, `menu`)
- Lista de dicionários para armazenar alunos
- Loop de menu interativo até a escolha da opção de saída

## Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/boletim-edusimples.git
3. Acesse a pasta do projeto:
   ```bash
   cd boletim-edusimples
4. Execute o programa:
   ```bash
   python boletim.py

## Estrutura de dados esperado na lista "Alunos"

Cada aluno é armazenado como um dicionário com os seguintes campos:
```python
{
  "matricula": "0001",
  "nome": "Ana Souza",
  "n1": 8.5,
  "n2": 7.0
}
```

A média e a situação são calculadas dinamicamente pelas funções media() e situacao().

## Autoria

Projeto desenvolvido por Eduardo Lira, estudante participante do COMPET Médio SophIA.
