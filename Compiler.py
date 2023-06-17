import re

# Token types
TOKENS = {
    'write': 'WRITE',       # نوع توکن برای دستور write
    'read': 'READ',         # نوع توکن برای دستور read
    'ifso': 'IF',           # نوع توکن برای دستور if
    'selector': 'SWITCH',   # نوع توکن برای دستور switch
    'loop': 'FOR',          # نوع توکن برای دستور for
    'until': 'WHILE',       # نوع توکن برای دستور while
    'int': 'INT',           # نوع توکن برای اعداد صحیح
    'float': 'FLOAT',       # نوع توکن برای اعداد اعشاری
    'char': 'CHAR',         # نوع توکن برای کاراکترها
    'identifier': 'IDENTIFIER',   # نوع توکن برای شناسه‌ها
    'number': 'NUMBER',     # نوع توکن برای اعداد
    'string': 'STRING',     # نوع توکن برای رشته‌ها
    'operator': 'OPERATOR', # نوع توکن برای عملگرها
    'delimiter': 'DELIMITER',     # نوع توکن برای ;
}

# Regular expressions for matching tokens
TOKEN_REGEX = {
    'identifier': r'[a-zA-Z_][a-zA-Z0-9_]*',   # الگو برای شناسه‌ها
    'number': r'[0-9]+\.[0-9]+|[0-9]+',         # الگو برای اعداد
    'string': r'"([^"]*)"',                     # الگو برای رشته‌ها
    'operator': r'[+\-*/=<>!]+',                # الگو برای عملگرها
    'delimiter': r'[,;]',                       # الگو برای ;
    'whitespace': r'\s+',                        # الگو برای فاصله
}


def tokenize(code):
    tokens = []
    pos = 0

    while pos < len(code):
        match = None
        error = False

        for token_type, pattern in TOKEN_REGEX.items():
            regex = re.compile(pattern)
            match = regex.search(code, pos)
            if match:
                token_value = match.group(0)
                tokens.append((token_type, token_value))
                break

        if not match:
            error = True
            invalid_token = code[pos]
            print("Invalid token:", invalid_token)
            pos += 1

        if error:
            continue

        pos = match.end(0)

    return tokens


def parse(tokens):
    intermediate_code = []

    pos = 0
    while pos < len(tokens):
        token_type, token_value = tokens[pos]
        print(f"Processing token: {token_type} ({token_value})")

        if token_type == 'WRITE':
            expression = tokens[pos + 1][1]
            intermediate_code.append(f'write {expression}')
            pos += 2

        elif token_type == 'READ':
            identifier = tokens[pos + 1][1]
            intermediate_code.append(f'read {identifier}')
            pos += 2

        elif token_type == 'IF':
            condition = tokens[pos + 1][1]
            intermediate_code.append(f'if {condition} then')
            pos += 2

        elif token_type == 'SWITCH':
            selector = tokens[pos + 1][1]
            intermediate_code.append(f'selector {selector}')
            pos += 2

        elif token_type == 'FOR':
            expression = tokens[pos + 1][1]
            intermediate_code.append(f'for {expression}')
            pos += 2

        elif token_type == 'WHILE':
            condition = tokens[pos + 1][1]
            intermediate_code.append(f'while {condition}')
            pos += 2

        pos += 1

    return intermediate_code


def process_code(code):
    tokens = tokenize(code)
    if tokens:
        intermediate_code = parse(tokens)
        if intermediate_code:
            print("Intermediate Code:")
            for instruction in intermediate_code:
                print(instruction)


file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    code = file.read()

process_code(code)
