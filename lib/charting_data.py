import matplotlib.pyplot as plt
from lib.api import ApiResponse
from datetime import date
from os import remove
from shutil import move

class CovidChart:

    def __init__(self):
        self.labels = self.data_labels()
        self.sizes = self.plot_sizes()

    def data_labels(self):
        labels = ['Tested Negative', 'Tested Positive']
        return labels

    def plot_sizes(self):
        sizes = [ApiResponse().get_nr_positives(), ApiResponse().get_nr_negatives()]
        return sizes

    def plots(self):
        fig1, ax1 = plt.subplots()
        ax1.pie(self.sizes, labels=self.labels, autopct="%1.1f%%", startangle=90)
        ax1.axis('equal')

    def show_plot(self):
        self.plots()
        plt.show()

    def return_plot_image(self):
        self.plots()

    def save_plot(self):
        self.plots()
        plt.savefig(f"{date.today()}", dpi=300, bbox_inches='tight')
        move(f"{date.today}.png", "\\gui")

    def delete_plot(self):
        remove(f"{date.today()}.png")

# CovidChart().show_plot()
# CovidChart().save_plot()
# CovidChart().delete_plot()
