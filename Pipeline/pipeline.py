from Extract.rule_extract import RuleExtract


class Pipeline:
    
    def __init__ (self , extractor : RuleExtract):  #if RuleExtract is not defined here pipeline will can take any extractor that nor follow the rules
        self.extractor = extractor
        
    def run(self):
    
        rows , header = self.extractor.extract()  #extract come from RuleExtract 
        
        print([dict(zip(header , row)) for row in rows])
        