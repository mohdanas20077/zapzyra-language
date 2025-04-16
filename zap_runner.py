import subprocess
from zapzyra_transpiler import transpile_file
import os

def run_zapzyra(file_path):
    output_py = "temp_zapzyra_output.py"
    transpile_file(file_path, output_py)

    print("🚀 Running ZapZyra code...\n")
    subprocess.run(["python", output_py])

if __name__ == "__main__":
    run_zapzyra("examples/test.zz")
