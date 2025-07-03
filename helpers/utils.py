def strip_quotes(s: str) -> str:

    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    return s



def is_int(s: str) -> bool:

    try:
        int(s)
        return True
    except ValueError:
        return False
