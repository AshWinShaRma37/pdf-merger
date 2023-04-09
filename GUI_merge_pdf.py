import tkinter as tk
from tkinter import filedialog
import os
from PyPDF2 import PdfReader, PdfWriter
from tkinter.ttk import Progressbar
from tkinter import messagebox
import PyPDF2

def browseFiles():
    file_list.delete(0, tk.END)
    filetypes = [("PDF Files", "*.pdf")]
    filenames = filedialog.askopenfilenames(title="Select PDF Files", filetypes=filetypes)
    for file in filenames:
        file_list.insert(tk.END, file)


def mergePDFs():
    if file_list.size() == 0:
        messagebox.showwarning("Error", "No files selected!")
        return

    # Set up progress bar
    progress_label = tk.Label(root, text="Merging PDFs...")
    progress_label.pack(pady=10)
    progress = Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
    progress.pack(pady=10)

    # Get save file location
    save_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

    if save_filename:
        # Create output PDF
        output_pdf = PyPDF2.PdfWriter()

        # Merge input PDFs into output PDF
        num_files = file_list.size()
        for i in range(num_files):
            input_pdf = PdfReader(file_list.get(i), 'rb')
            for page in range(len(input_pdf.pages)):
                output_pdf.add_page(input_pdf.pages[page])

            # Update progress bar
            progress['value'] = (i+1) * 100 // num_files
            progress.update()

        # Save output PDF to file
        with open(save_filename, 'wb') as f:
            output_pdf.write(f)

        # Show success message
        messagebox.showinfo("Success", "PDFs merged successfully!")

    # Reset GUI
    progress_label.destroy()
    progress.destroy()
    file_list.delete(0, tk.END)


# Create GUI
root = tk.Tk()
root.title("PDF Merger")
root.geometry("400x300")
root.config(bg="#222222")

# Dark mode styling
root.option_add("*Background", "#222222")
root.option_add("*Foreground", "#ffffff")
root.option_add("*Font", "Arial")

# Create file list frame
file_frame = tk.Frame(root)
file_frame.pack(pady=10)

# Create file list
file_list = tk.Listbox(file_frame, selectmode=tk.MULTIPLE, font=('Arial', 10), bg="#333333", fg="#ffffff")
file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=10)

# Create scrollbar for file list
scrollbar = tk.Scrollbar(file_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=file_list.yview)
file_list.config(yscrollcommand=scrollbar.set)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
browse_button = tk.Button(button_frame, text="Browse Files", command=browseFiles, bg="#444444", fg="#ffffff")
browse_button.pack(side=tk.LEFT, padx=10)
merge_button = tk.Button(button_frame, text="Merge PDFs", command=mergePDFs, bg="#444444", fg="#ffffff")
merge_button.pack(side=tk.LEFT, padx=10)

# Start GUI
root.mainloop()
