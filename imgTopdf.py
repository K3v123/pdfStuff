import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import io


def simple_convert_to_jpeg():
    file_path = filedialog.askopenfilename(
        title="Select Image to Convert",
        filetypes=(("Image files", "*.jpg *.jpeg *.png"),)
    )

    if not file_path:
        return

    output_path = filedialog.asksaveasfilename(
        title="Save JPEG As",
        filetypes=[("JPEG files", "*.jpg")],
        defaultextension=".jpg"
    )

    if not output_path:
        return

    try:
        # Read the input file
        with open(file_path, 'rb') as f:
            img_data = f.read()

        # Get base file name and extension
        base_name, ext = os.path.splitext(file_path)
        ext = ext.lower()

        # This is a simplified conversion that only works well for files already in JPEG format
        # For PNG to JPEG, we'd normally need to decode/re-encode
        if ext in ('.jpg', '.jpeg'):
            # If already JPEG, just copy to new location
            with open(output_path, 'wb') as out_f:
                out_f.write(img_data)
        else:
            # Show warning message
            messagebox.showwarning(
                "Conversion Limitation",
                "This simple conversion only works with files that are already in JPEG format.\n\n"
                "For converting PNG to JPEG, please install Pillow:\n"
                "Run: pip install pillow"
            )
            return

        messagebox.showinfo(
            "Success",
            f"File saved as JPEG at:\n{output_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert: {str(e)}")


# Create GUI
root = tk.Tk()
root.title("Basic Image to JPEG Converter")
root.geometry("500x250")

# Style
style = ttk.Style()
style.configure('TButton', font=('Arial', 10))

# UI Elements
label = ttk.Label(
    root,
    text="Simple Image to JPEG Conversion",
    font=('Arial', 12)
)
label.pack(pady=15)

convert_btn = ttk.Button(
    root,
    text="Select Image and Convert",
    command=simple_convert_to_jpeg
)
convert_btn.pack(pady=10)

warning = ttk.Label(
    root,
    text="Note: Only basic conversion available without Pillow",
    foreground="red"
)
warning.pack(pady=15)

install_note = ttk.Label(
    root,
    text="For full functionality, install Pillow with:\npip install pillow",
    foreground="blue"
)
install_note.pack(side='bottom', pady=10)

root.mainloop()
