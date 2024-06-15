"""
This file created for place code, that can make convenient to use any
internal functionality of system(not business logic).
"""
def from_camel_to_snake_case(string: str):
    """
    Examples:
        from_camel_to_snake_case("Product") -> product
        from_camel_to_snake_case("UserProfile") -> user_profile
        from_camel_to_snake_case("Index") -> indice
    """
    string_by_chars = [*string]
    plural_transformations = {
        "y": "ie",  
        "s": "se",  
        "fe": "ve", 
        "us": "i",  
        "is": "es", 
        "on": "a",  
        "um": "a",  
        "a": "ae",  
        "ex": "ice",
        "ix": "ice", 
        "f": "ve",  
        "o": "oe",  
        "ch": "che",
        "sh": "she",
        "x": "xe",  
        "z": "ze",  
    }

    string_by_chars[0] = string_by_chars[0].lower()
    
    for i, char in enumerate(string_by_chars[1:], 1):
        if char.isupper():
            string_by_chars[i] = f"_{char.lower()}"
    
    char_ending, two_chars_endig = string[-1], string[-3:]
    string_by_chars = "".join(string_by_chars)

    if two_chars_endig in plural_transformations:
        string_by_chars = string_by_chars[:-3] + plural_transformations[two_chars_endig]
    elif char_ending in plural_transformations:
        string_by_chars = string_by_chars[:-1] + plural_transformations[char_ending]

    return string_by_chars
