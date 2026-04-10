import os

# PDF folder path
PDF_FOLDER = "data/input/equipa_tecnica"

# Define expected table columns
COLUMNS = [
    "PROJETO ORDENADOR E DE ESPECIALIDADE",
    "NOME DO AUTOR DO PROJETO", 
    "Nº INSCRIÇÃO NA ORDEM PROFISSIONAL"
]

ESPECIALIDADES = [
    "Autor do Projeto Arquitetura, incluindo Plano de Acessibilidades",
    "Autor do Projeto de Escavação e Contenção Periférica (ECV)",
    "Autor do Projeto de Fundações e Estruturas e de Demolições, incluindo plano de sondagens e de prospeção geotécnica, plano de análise estrutural e Relatório de Avaliação da Vulnerabilidade Sísmica (EST)",
    "Autor do Projeto de Instalações, Equipamentos e Sistemas de Águas, incluindo Rede de Incêndio (AGU)",
    "Autor do Projeto de Instalações, Equipamentos e Sistemas de Águas e Esgotos – doméstica e pluvial (ESG)",
    "Autor do Projeto de Instalações, Equipamentos e Sistemas de Aquecimento, Ventilação, Ar Condicionado e Refrigeração (MEC)",
    "Autor do Projeto de segurança contra incêndios em edifícios – e respetiva submissão à apreciação da Autoridade Nacional de Emergência e Proteção Civil – ANEPC (SCI);",
    "Autor do Estudo de Comportamento Térmico, incluindo Certificado Energético do edificado existente e o Pré-Certificado Energético da proposta (ECT);",
    "Autor do Projeto de Arquitetura Paisagista para o logradouro privativo, incluindo plano de acessibilidades (PAI)"
]

# Map filenames to identifiers
FILE_MAPPING = {
    "11651.pdf": "11651",    
    "12098.pdf": "12098", 
    "12102.pdf": "12102", 
    "12220.pdf": "12220", 
    "12224.pdf": "12224", 
    "12228.pdf": "12228", 
    "12263.pdf": "12263", 
    "12291.pdf": "12291", 
    "12308.pdf": "12308", 
    "12316.pdf": "12316", 
    "12321.pdf": "12321", 
    "12327.pdf": "12327", 
    "12334.pdf": "12334", 
    "12347.pdf": "12347", 
    "12351.pdf": "12351",
    "12402.pdf": "12402",
    "12406.pdf": "12406",
}