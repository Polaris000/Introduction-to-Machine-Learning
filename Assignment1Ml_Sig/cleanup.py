import csv



class Tweet():

	def __init__(self, line):
		self.line_raw = line


	def get_id(self):
		
		self.line = "".join(self.line_raw).split("\t")
		self.id = self.line[0][:-1]

		return self.id


	def get_text(self):
		
		self.line = "".join(self.line_raw).split("\t")
		self.text = self.line[1]

		return self.text

	def get_emotion(self):
		
		self.line = "".join(self.line_raw).split("\t")
		self.emotion = self.line[2][3:]

		return self.emotion


		

with open("jan9-2012.txt", "r") as f:
	with open("cleaned_data.csv", "w") as w:

		
		for line in f:
			t = Tweet(line)

			w.write(t.get_id() + "," + t.get_text() + "," + t.get_emotion())
			
			
