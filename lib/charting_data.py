import matplotlib.pyplot as plt
from lib.api import ApiResponse

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

CovidChart().show_plot()
# labels = ['Tested Negative', 'Tested Positive']
# sizes = [ApiResponse().get_nr_positives(), ApiResponse().get_nr_negatives()]
# fig1, ax1 = plt.subplots()
# plt.show()