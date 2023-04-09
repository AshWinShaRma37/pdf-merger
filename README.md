# pdf-merger
This is a Python GUI application that allows you to select multiple PDF files, merge them into a single PDF file, and save it to a location of your choice.

# Requirements
This application requires the following packages:

- PyPDF2
- tkinter

# How to use

- Run the GUI_merge_pdf.py script using Python 3 or run the GUI_merge_pdf.exe
- Click on the "Browse Files" button to select the PDF files you want to merge. You can select multiple files by holding down the "Ctrl" key while clicking.
- Upon selecting the file, the name of each file will appear.
- Click on the "Merge PDFs" button to start the merging process. The progress bar will show you the progress of the merging process.
- Once the merging is complete, a dialog box will appear asking you to select a location to save the merged PDF file.
- Select a location and click "Save" to save the merged PDF file.
- Upon successful merge, a message box saying merge was successful will pop-up.

# Features

- Dark mode GUI.
- Progress bar to show the progress of the merging process.
- Ability to select multiple PDF files at once.
- Ability to save the merged PDF file to a location of your choice.

# Limitations
- The application only supports merging PDF files.
- The merged PDF file will have the same orientation and size as the first PDF file that is added.
- The application may not work correctly if the PDF files are password-protected or encrypted.
