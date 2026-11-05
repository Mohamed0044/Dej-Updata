from ..client import ContentClient

def validate_text_input(text: str, min_length: int, field_name: str) -> str:
    if not isinstance(text, str):
        raise ValueError(f"{field_name} must be text.")

    text = text.strip()
    if len(text) < min_length:
        raise ValueError(f"{field_name} must be at least {min_length} characters.")

    return text



def validate_title(title: str, min_length: int = 5) -> str:
    """Title validation is just text validation with a shorter minimum."""
    return validate_text_input(title, min_length, field_name="Title")

def generate_ai_content(prompt: str, system: str = None) -> str:
    client = ContentClient()
    result = client.generate(prompt, system=system)
    print("result", result)
    if not isinstance(result, str):
        raise ValueError("Model output was empty or invalid.")
    cleaned_result = result.strip()
    print("cleaned_result", cleaned_result)
    if not cleaned_result:
        raise ValueError("Model output was empty or invalid.")

    return cleaned_result