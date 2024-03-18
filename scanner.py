import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
import pandas as pd

class ExcelToCSVConverter(QWidget):
    def __init__(self):
        super().__init__()

        # Create the UI components
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Select an Excel file")
        layout.addWidget(self.label)

        btn = QPushButton("Browse")
        btn.clicked.connect(self.open_file_dialog)
        layout.addWidget(btn)

    def open_file_dialog(self):
        # Show a file dialog to select an Excel file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Excel Files (*.xlsx *.xls)", options=options)

        if fileName:
            self.label.setText(f"Selected File: {fileName}")
            self.convert_excel_to_csv(fileName)

    def convert_excel_to_csv(self, file_path):
        # Read the Excel file and save each sheet as a separate CSV file
        xls = pd.ExcelFile(file_path)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            output_file = f"{sheet_name}.csv"
            df.to_csv(output_file, index=False)
            print(f"Created {output_file}")

# Run the application
app = QApplication(sys.argv)
window = ExcelToCSVConverter()
window.show()
sys.exit(app.exec_())

