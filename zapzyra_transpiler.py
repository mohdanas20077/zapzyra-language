import re

def transpile_line(line):
    stripped = line.lstrip()
    indent = " " * (len(line) - len(stripped))

    # Function definition
    if stripped.startswith("fz_fctn:"):
        return indent + "def " + stripped.replace("fz_fctn:", "").strip() + ":"

    # say(...) → print(...)
    elif stripped.startswith("say("):
        return indent + stripped.replace("say(", "print(", 1)

    # Type-based input
    elif ": int = input(" in stripped:
        var_name = stripped.split(":")[0].strip()
        return indent + f"{var_name} = int({stripped.split('=')[1].strip()})"
    elif ": str = input(" in stripped:
        var_name = stripped.split(":")[0].strip()
        return indent + f"{var_name} = str({stripped.split('=')[1].strip()})"
    elif ": float = input(" in stripped:
        var_name = stripped.split(":")[0].strip()
        return indent + f"{var_name} = float({stripped.split('=')[1].strip()})"

    return line

def transpile_file(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    transpiled = [transpile_line(line.rstrip()) for line in lines]

    with open(output_path, 'w') as f:
        f.write("\n".join(transpiled))

    print(f"✅ Transpiled to {output_path}")
