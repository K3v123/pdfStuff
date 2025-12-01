import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def select_pdf(title):
    filepath = filedialog.askopenfilename(
        title=title,
        filetypes=[("PDF files", "*.pdf")],
        defaultextension=".pdf"
    )
    return filepath if filepath else None


def combine_pdfs():
    file1 = select_pdf("Select First PDF File")
    if not file1:
        return

    file2 = select_pdf("Select Second PDF File")
    if not file2:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Combined PDF As",
        filetypes=[("PDF files", "*.pdf")],
        defaultextension=".pdf"
    )
    if not output_file:
        return

    try:
        merger = PyPDF2.PdfMerger()
        merger.append(file1)
        merger.append(file2)

        with open(output_file, 'wb') as out_file:
            merger.write(out_file)

        messagebox.showinfo(
            "Success",
            f"PDFs combined successfully!\nSaved as: {output_file}"
        )
    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Failed to combine PDFs:\n{str(e)}"
        )


# Set up the GUI
root = tk.Tk()
root.title("PDF Combiner")
root.geometry("400x150")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure('TButton', font=('Arial', 10))
style.configure('TLabel', font=('Arial', 12))

# Create UI elements
label = ttk.Label(
    root,
    text="Combine Two PDF Files",
    justify='center'
)
label.pack(pady=10)

combine_btn = ttk.Button(
    root,
    text="Select PDF Files and Combine",
    command=combine_pdfs
)
combine_btn.pack(pady=10)

exit_btn = ttk.Button(
    root,
    text="Exit",
    command=root.destroy
)
exit_btn.pack(pady=5)

root.mainloop()
