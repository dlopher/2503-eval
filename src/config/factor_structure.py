from typing import Dict, List


# Define factor structure
FACTOR_STRUCTURE = {
    "A1": {
        "name": "Obras de edifícios de Ut. Colectiva na UE",
        "type": "projeto",
        "require_date": True,
        "require_owner": True,
        "disciplinas": [
            "Coordenação",
            "BIM",
            "ARQ", 
            "ArqPAIS", 
            "Estruturas", 
            "AVACR"
        ]
    },
    "A2": {
        "name": "Obras de edifícios escolares na UE",
        "type": "projeto",
        "require_date": True,
        "require_owner": True,
        "disciplinas": [
            "Coordenação",
            "BIM",
            "ARQ", 
            "ArqPAIS", 
            "Estruturas", 
            "AVACR"
        ]
    },
    "A3": {
        "name": "Obras públicas na UE",
        "type": "projeto",
        "require_date": True,
        "require_owner": True,
        "disciplinas": [
            "Coordenação",
            "BIM",
            "ARQ", 
            "ArqPAIS", 
            "Estruturas", 
            "AVACR"
        ]
    },
    "A4": {
        "name": "Obras de reabilitação com reforço sísmico na UE",
        "type": "projeto",
        "require_date": True,
        "require_owner": True,
        "disciplinas": [
            "Coordenação",
            "BIM",
            "ARQ", 
            "ArqPAIS", 
            "Estruturas", 
            "AVACR"
        ]
    },
    "A5": {
        "name": "Horas de formação para a gestão BIM",
        "type": "formação",
        "require_date": False,
        "require_owner": False,
        "disciplinas": [
            "formação BIM"
        ]
    }
}