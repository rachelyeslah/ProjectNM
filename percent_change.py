import csv
import pandas as pd
	
df = pd.read_csv('data_C3-C4.csv')

#build class Trial
class Trial:
	def __init__(self, channel_name, time, stim_intensity, rep_rate, a = []):
		self.channel_name = channel_name
		self.time = time
		self.stim_intensity = stim_intensity
		self.rep_rate = rep_rate
		self.datapoints = Datapoints()

	# class Datapoints:
	# 	def __init__(self, datapoints):
	# 		self.datapoints = datapoints



        

#    def LoadDatapoints(self, datapoints):
#       datapoints.append(datapoints)

#creating instances of trials and putting into triallist
triallist = []
# for col_name, data in df.items():
# 	trial = Trial(data[0], data[1], data[6], data[8])
# 	triallist.append(trial)

print(df['1'])



 
#for col_name, data in df.items():
#	trial.LoadDatapoints()


# ..... 

#	var datapoints: [Datapoint] = []

#	for column in spamreader:
#		let datapoint = makeDatapoint(column)
#		datapoints.append(datapoint)

#	doComputation(datapoints)
#	getAverage(datapoints)
#	getMaxPeriod(datapoints)
#	getMinLowcut(datapoints)


#class Datapoint {
#	let index: Int
#	let name: String
#	let time: Int
#	let highcut: Double
#	let data: [DataObject]
#	// ...
#}

#class DataObject {
#	let index: Int
#	let value: Double
#}

#func makeDatapoint(column: String) -> Datapoint {
#	return Datapoint(
#			index: index,
#			name: name, 
#			time: time,
#		)
#}