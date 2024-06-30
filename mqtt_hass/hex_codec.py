def convert_hex_string_to_bytes(hex_string: str) -> bytes:
    return bytes.fromhex(hex_string)

def get_bytes(value: bytes, start: int, amount: int) -> bytes:  
    return value[start:start+amount]
