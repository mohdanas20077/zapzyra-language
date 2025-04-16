import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from zapzyra_transpiler import transpile_file

class ZapZyraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ZapZyra Language GUI")
        self.root.geometry("400x200")
        
        # Label
        self.label = tk.Label(root, text="Choose a ZapZyra (.zz) file to run", font=("Arial", 14))
        self.label.pack(pady=20)
        
        # File path entry
        self.file_path = tk.Entry(root, width=40, font=("Arial", 12))
        self.file_path.pack(pady=10)
        
        # Browse button
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file, font=("Arial", 12))
        self.browse_button.pack(pady=10)
        
        # Run button
        self.run_button = tk.Button(root, text="Run", command=self.run_code, font=("Arial", 12))
        self.run_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("ZapZyra Files", "*.zz")])
        if file_path:
            self.file_path.delete(0, tk.END)  # Clear the entry field
            self.file_path.insert(0, file_path)  # Insert the chosen file path

    def run_code(self):
        zz_file = self.file_path.get()
        if not zz_file:
            messagebox.showerror("Error", "Please select a .zz file")
            return

        output_py = "temp_zapzyra_output.py"
        try:
            # Transpile ZapZyra code to Python
            transpile_file(zz_file, output_py)
            
            # Run the transpiled Python code
            subprocess.run(["python", output_py])
            messagebox.showinfo("Success", "ZapZyra code ran successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


# Create the Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = ZapZyraGUI(root)
    root.mainloop()
