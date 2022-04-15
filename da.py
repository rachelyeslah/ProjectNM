


import csv 
import pandas as pd 
import matplotlib.pyplot as plt


CSV_LOAD_PATH = "data_C3-C4.csv"

ROW_INDEX = {
	'name': 0,
	'time': 1,
	'stim_intensity': 6,
	'rep_rate': 8
}





def plot_signal(datapoints):
	plt.plot(datapoints)
	# plt.title('Max: ', max(datapoints), 'min: ', min(datapoints))
	plt.show()


def percent_change(trial_a_signal, trial_b_signal):
	amp_a = max(trial_a_signal) - min(trial_a_signal)
	amp_b = max(trial_b_signal) - min(trial_b_signal)
	return (amp_b - amp_a) / amp_a



class Trial:

	def __init__(self, column):
		self.channel_name = column[ROW_INDEX['name']]
		self.time = column[ROW_INDEX['time']]
		self.stim_intensity = column[ROW_INDEX['stim_intensity']]
		self.rep_rate = column[ROW_INDEX['rep_rate']]

		self.signal = self.read_signal(column)

	def read_signal(self, column):
		# return a list of floats of signal
		list_of_strings = list(column[9:])
		return [float(i) for i in list_of_strings]


def main():
	# load csv
	df = pd.read_csv('data_C3-C4.csv')

	print(df.head(20))

	list_of_trials = []
	for col_index in range(1, 19):
		index = str(col_index)
		curr_trial = Trial(df[index])
		list_of_trials.append(curr_trial)

	
	trial_1_signal = list_of_trials[0].signal # -> do what you want here.

	trial_2_signal = list_of_trials[1].signal


	print(percent_change(trial_1_signal, trial_2_signal))


	# for trial in list_of_trials:
		# plot_signal(trial.signal)

	# print(type(trial_1.time))





if __name__ == "__main__":
	main()

