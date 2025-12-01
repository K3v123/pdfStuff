import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pypdf import PdfReader, PdfWriter
import threading
import os

def compress_pdf_pypdf(input_path, output_path):
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        # Copy metadata
        writer.add_metadata(reader.metadata)

        # Compress content streams (text/vector only)
        for page in writer.pages:
            page.compress_content_streams()

        # Write output
        with open(output_path, "wb") as f:
            writer.write(f)

        return True, ""
    except Exception as e:
        return False, str(e)

def select_file():
    filepath = filedialog.askopenfilename(
        title="Select PDF to Compress",
        filetypes=[("PDF files", "*.pdf")]
    )
    if filepath:
        input_var.set(filepath)

def start_compression():
    input_path = input_var.get()
    if not input_path:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    output_path = input_path.replace(".pdf", "_compressed_pypdf.pdf")

    def run():
        progress.start()
        btn_compress.config(state="disabled")
        success, error = compress_pdf_pypdf(input_path, output_path)
        progress.stop()
        btn_compress.config(state="normal")

        if success:
            orig_size = os.path.getsize(input_path) / (1024 * 1024)
            new_size = os.path.getsize(output_path) / (1024 * 1024)
            reduction = (1 - new_size / orig_size) * 100
            messagebox.showinfo(
                "Finished",
                f"Original: {orig_size:.1f} MB\n"
                f"Compressed: {new_size:.1f} MB\n"
                f"Reduction: {reduction:.1f}%\n\n"
                f"Saved to:\n{output_path}"
            )
        else:
            messagebox.showerror("Error", f"Compression failed:\n{error}")

    threading.Thread(target=run, daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("PDF Compressor (pypdf only)")
root.geometry("500x220")
root.resizable(False, False)

tk.Label(root, text="Select a PDF to compress:", font=("Arial", 10)).pack(pady=(20, 5))
input_var = tk.StringVar()
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Entry(frame, textvariable=input_var, width=50, state="readonly").pack(side="left", padx=(0, 5))
tk.Button(frame, text="Browse", command=select_file).pack(side="left")

btn_compress = tk.Button(
    root, text="Compress PDF", command=start_compression,
    bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), height=2
)
btn_compress.pack(pady=20)

progress = ttk.Progressbar(root, mode="indeterminate", length=300)
progress.pack()

tk.Label(
    root, text="Note: Only compresses text/vector data.\nImage-heavy PDFs will see little size reduction.",
    fg="orange", font=("Arial", 8), justify="center"
).pack(side="bottom", pady=5)

root.mainloop()
