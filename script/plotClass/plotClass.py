import json

class plotClass:
    def __init__(self, dataFilePath, outputFolder, appendix):
        self.dataFilePath = dataFilePath
        self.outputFolder =outputFolder
        self.plots = []
        self.subplots = []
        self.appendix = appendix

    def getNumberOfPlots(self):
        return len(self.plots)

    def getNumberOfSubPlots(self, plotNumber):
        return len(self.plots[plotNumber])
    
    def addPlot(self, plot_title):
        self.plots.append( {
            "plot_title": plot_title
            }
        )
    
    def addSubPlot(self, 
        plotNumber, 
        x_index,
        y_index,
        x_label,
        y_label,
        **kwargs):
        self.plots[plotNumber].append( {
                "subplots"
            }
        )

    def writeToJson(self):
        plotJson = {
            "file_path": self.dataFilePath,
            "output_folder": self.outputFolder,
            "appendix": self.appendix,
            "plots": [
                {
                    "subplots": [
                        {
                            
                        }
                    ]   
                }
            ]
        }

        with open('data.json', 'w') as outfile:
            json.dump(plotJson, outfile, indent=4)
