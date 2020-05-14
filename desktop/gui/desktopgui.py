import sys
from lib import api
from lib.charting_data import CovidChart
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


app = QApplication(sys.argv)


class MainGuiWindow:

    def __init__(self):
        self.main_window = QWidget()
        self.main_window.setWindowTitle('Covid19 Tracker')
        self.main_window.setGeometry(500, 500, 500, 500)
        self.main_window.move(10, 15)
        self.refresh_nr = 0

    def window_label(self):
        win_label = QLabel("<h1>USA COVID-19 Tracker!</h1>", parent=self.main_window)
        win_label.move(10, 15)

    def number_of_positively_tested(self):
        nr_positive = QLabel(f"<h3>Number of positive tests are: {api.ApiResponse().get_nr_positives()} </h3>",
                             parent=self.main_window)
        nr_positive.move(10, 80)

    def number_of_negative_tested(self):
        nr_negative = QLabel(f"<h3>Number of negative tests are: {api.ApiResponse().get_nr_negatives()}</h3>",
                             parent=self.main_window)
        nr_negative.move(10, 100)

    def total_number_of_tested(self):
        nr_total = QLabel(f"<h2><u>Total number of cases tests done: {int(api.ApiResponse().get_nr_positives()) + int(api.ApiResponse().get_nr_negatives())}</h2></u>", parent=self.main_window)
        nr_total.move(10, 120)

    def show_pie_chart(self):
        cov_chart = QWidget()
        cov_chart.setWindowTitle('Cov19 Pychart')
        cov_chart.setGeometry(500, 500, 500, 500)
        cov_chart.move(100, 150)
        chart = CovidChart().show_plot()

    def start_gui(self):

        self.window_label()
        self.number_of_positively_tested()
        self.number_of_negative_tested()
        self.total_number_of_tested()
        self.main_window.show()
        sys.exit(app.exec_())


MainGuiWindow().start_gui()