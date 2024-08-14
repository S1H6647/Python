letter = '''Dear <|Name|>
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Sanjit").replace("<|Date|>", "1 Oct"))