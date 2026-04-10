from datetime import datetime
import re
import pandas as pd
from src.config.config_linear import CURRENT_DATE, DATE_LIMITS, ACCEPTED_DATE_FORMATS


def parse_date(date_input) -> tuple:
    """
    Parse date from multiple formats: dd/mm/yyyy, dd/mm/yy, yyyy, or datetime object
    Returns: (datetime_obj, is_valid, observation)
    
    - datetime_obj: parsed date or None
    - is_valid: True if format is correct, False if unparseable
    - observation: error message if invalid

    Parsing rules:
    - yyyy → January 1st of that year
    - mm/yyyy → First day of that month
    - dd/mm/yyyy or dd/mm/yy → Exact date
    """

    if isinstance(date_input, datetime):
        return date_input, True, ""
    
    if pd.isna(date_input) or date_input is None or str(date_input).strip() == "":
        return None, False, "sem data"
    
    date_str = str(date_input).strip()
    
    # Try yyyy format
    if re.match(r'^\d{4}$', date_str):
        try:
            year = int(date_str)
            return datetime(year, 1, 1), True, ""
        except:
            return None, False, f"formato de data invalido: '{date_str}'"
    
    # Try mm/yyyy format
    if re.match(r'^\d{1,2}/\d{4}$', date_str):
        try:
            parts = date_str.split('/')
            month = int(parts[0])
            year = int(parts[1])
            if 1 <= month <= 12:
                return datetime(year, month, 1), True, ""
            else:
                return None, False, f"mês invalido: '{month}'"
        except:
            return None, False, f"formato de data invalido: '{date_str}'"
    
    # Try dd/mm/yyyy or dd/mm/yy
    for fmt in ACCEPTED_DATE_FORMATS:
        try:
            parsed = datetime.strptime(date_str, fmt)
            return parsed, True, ""
        except:
            continue
    # if we reach here, format is invalid
    return None, False, f"formato de data invalido: '{date_str}'"


def validate_date(date_obj: datetime, item_type: str = "projeto") -> tuple:
    """
    Validate date against age limit.
    Returns: (is_valid, status, observation)
    
    - is_valid: True if passes validation
    - status: "" (empty/valid), "DESCL" (disqualified), or "AVISO" (warning)
    - observation: reason/note
    """
    if date_obj is None:
        return False, "DESCL", "sem data ou formato invalido"
    
    limit_years = DATE_LIMITS.get(item_type, 10)
    year_diff = CURRENT_DATE.year - date_obj.year
    
    # Account for months (if project is in same year but after current date, it's -1)
    if date_obj.month > CURRENT_DATE.month:
        year_diff -= 1
    elif date_obj.month == CURRENT_DATE.month and date_obj.day > CURRENT_DATE.day:
        year_diff -= 1
    
    if year_diff > limit_years:
        return False, "DESCL", f"Excede limite de {limit_years} anos (antiguedade: {year_diff} anos)"
    elif year_diff == limit_years:
        return True, "AVISO", f"No limite de {limit_years} anos (antiguedade: {year_diff} anos. Verificar data)"
    else:
        return True, "", ""