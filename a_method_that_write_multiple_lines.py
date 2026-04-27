class Writer:
    def __init__(self,writer_file):
        self.writer_file = writer_file
    def main_file(self):
        with open(self.writer_file,'w') as writer_data:
            for line in writer_data: