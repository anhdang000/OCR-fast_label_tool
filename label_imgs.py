import os
import sys
sys.path.append(os.getcwd())

from configs import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--prev-row', default=0, type=int, help='Previous working row. For resuming.')
parser.add_argument('--num-examples', default=1000, type=int, help='Number of examples will be loaded into the table.')
parser.add_argument('--num-cols', default=5, type=int, help='Number of main columns.')
FLAGS = parser.parse_args()
# print(FLAGS.accumulate(FLAGS.integers))

CURR_ROW = FLAGS.prev_row
N_COLS = FLAGS.num_cols
NUM_EXAMPLES = FLAGS.num_examples
N_ROWS = NUM_EXAMPLES // N_COLS

class ImageWidget(QtWidgets.QWidget):

	def __init__(self, imagePath, parent):
		super(ImageWidget, self).__init__(parent)
		self.picture = QtGui.QPixmap(imagePath)
		self.picture = self.picture.scaledToHeight(25)

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.drawPixmap(0, 0, self.picture)


class TableWidget(QtWidgets.QTableWidget):

    def setImage(self, row, col, imagePath):
        image = ImageWidget(imagePath, self)
        self.setCellWidget(row, col, image)

#Main Window
class App(QWidget):
	def __init__(self):
		super().__init__()
		self.title = 'Label Images'
		self.left = 0
		self.top = 0
		self.width = 500
		self.height = 600

		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.createTable()
		self.createSubmitButton()
		self.createClearButton()
		self.textbox = QLineEdit()

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.tableWidget)
		self.layout.addWidget(self.submit_button)
		self.layout.addWidget(self.clear_button)
		self.layout.addWidget(self.textbox)

		self.setLayout(self.layout)

		# Set current working row
		self.tableWidget.setCurrentCell(CURR_ROW, 1, QtCore.QItemSelectionModel.Select)
		self.tableWidget.item(CURR_ROW, 1).setBackground(QtGui.QColor(100,100,150))
		# Initial notification
		self.textbox.setText(f'Loaded {NUM_EXAMPLES} images')
		
		#Show window
		self.show()

		
	#Create table
	def createTable(self):
		self.tableWidget = TableWidget()

		#Row count
		self.tableWidget.setRowCount(N_ROWS)

		#Column count
		self.tableWidget.setColumnCount(N_COLS*2)

		#Column
		self.tableWidget.setHorizontalHeaderLabels(['Input', 'Label']*N_COLS)

		# Load images and recognized results
		curr_col = 0
		curr_row = 0
		i = 0
		while i < min(len(IMG_PATHS), N_ROWS*N_COLS):
			self.tableWidget.setImage(curr_row, curr_col, IMG_PATHS[i])
			# print(IMG_PATHS[i])
			list_rec_res = [elem for elem in CONTENT if elem and elem[0] == IMG_PATHS[i]]
			# print(list_rec_res)
			rec_res = list_rec_res[0] if len(list_rec_res) > 0 else None
			# print(rec_res)
			if rec_res and len(rec_res) > 1:
				# print(i, CONTENT[i][1])
				self.tableWidget.setItem(curr_row, curr_col + 1, QTableWidgetItem(rec_res[1]))
			self.tableWidget.setItem(curr_row, curr_col + 1, QTableWidgetItem(CONTENT[i][1]))
			if curr_col == N_COLS*2 - 2:
				curr_row += 1
				curr_col = 0
			else:
				curr_col += 2
			
			i += 1

		#Table will fit the screen horizontally
		self.tableWidget.horizontalHeader().setStretchLastSection(True)

		for i in range(0, N_COLS*2, 2):
			# self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
			# self.tableWidget.horizontalHeader().setSectionResizeMode(i+1, QHeaderView.Stretch)
			self.tableWidget.setColumnWidth(i, 200)


	# Submit button
	def createSubmitButton(self):
		# creating a push button
		self.submit_button = QPushButton("SUBMIT", self)
		# setting geometry of button
		self.submit_button.setGeometry(200, 150, 100, 30)
		# adding action to a button
		self.submit_button.clicked.connect(self.save_results)

	# action method
	def save_results(self):
		curr_row = self.tableWidget.currentRow()
		with open('output.txt', 'r', encoding="utf8") as f:
			previous_content = [line.strip().split('\t')[0] for line in f.readlines()]

		with open('output.txt', 'a', encoding="utf8") as f:
			self.textbox.setText('Writing to output.txt')
			print('Writing to output.txt')
			count = 0
			for row in range(curr_row+1):
				for col in range(1, N_COLS*2, 2):
					table_cell = self.tableWidget.item(row, col)
					if table_cell is not None:
						if len(table_cell.text().strip()) == 0:
							continue
						else:
							count += 1
							idx = row*N_COLS + col//2
							print(f'Index: {idx}, Row: {row}, Col: {col}')

							if IMG_PATHS[idx] not in previous_content:
								f.write(IMG_PATHS[idx] + '\t' + table_cell.text() + '\n')

							# Write to `output_diff.txt` if difference(s) were found
							if table_cell.text() != CONTENT[idx][1]:
								print(table_cell.text() + '\t' + CONTENT[idx][1])
								with open('output_diff.txt', 'r', encoding="utf8") as f1:
									previous_content_diff = [line.strip().split('\t')[0] for line in f1.readlines()]

								with open('output_diff.txt', 'a', encoding="utf8") as f1:
									if IMG_PATHS[idx] not in previous_content_diff:
										f1.write(IMG_PATHS[idx] + '\t' + table_cell.text() + '\n')
			
			self.textbox.setText(f'Done with {count} images')
			print(f'Done with {count} images')

	def createClearButton(self):
		# creating a push button
		self.clear_button = QPushButton("CLEAR", self)
		# setting geometry of button
		self.clear_button.setGeometry(200, 150, 100, 30)
		# adding action to a button
		self.clear_button.clicked.connect(self.clear_board)

	def clear_board(self):
		for row in range(N_ROWS):
			for col in range(1, N_COLS*2, 2):
				table_cell = self.tableWidget.item(row, col)
				if table_cell is not None:
					table_cell.setText('')
		
		self.textbox.setText('Cleared!')


	def keyPressEvent(self, event):
		super().keyPressEvent(event)
		if event.key() == QtCore.Qt.Key_Return:
			row = self.tableWidget.currentRow()
			col = self.tableWidget.currentColumn()

			if col == N_COLS*2 - 1:
				row = row + 1
				col = 1
				self.textbox.setText(f'Moved to the next row. Current row: {row + 1}, current col: {col//2 + 1}')
				self.tableWidget.setCurrentCell(row, col, QtCore.QItemSelectionModel.Select)
			else:
				col = col + 2
				self.tableWidget.setCurrentCell(row, col, QtCore.QItemSelectionModel.Select)

			self.tableWidget.edit(self.tableWidget.currentIndex())

			self.textbox.setText(f'Current row: {row + 1}, current col: {col//2 + 1}')



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
