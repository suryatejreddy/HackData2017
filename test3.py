import pickle
import pandas as pd
import ast

class Building:


	def __init__(self):
		self.coordinate = []
		self.address = ''
		self.heat_factor = 0.0
		self.confidence = 0.0
		self.blight = 0


	def makeFromRow(self,L):
		self.coordinate = L[0]
		self.address = L[2]
		self.heat_factor = float(5)
		self.confidence = self.getConfidence()

	def getConfidence():
		return 1



lat =  42.40089685923913 
lon =  -83.15689086914062


func(lat, lon, data)
