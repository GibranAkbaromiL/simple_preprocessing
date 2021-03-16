import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

content = "kalau tidak ada bangkit!!! orang mati, maka kristus juga tidak bangkit."

data = ["Kalau tidak ada kebangkitan orang mati, maka Kristus, juga tidak dibangkitkan! sebenar-benarnya",
        "Sebab apabila orang bangkit dari antara orang mati, orang_orang tidak kawin dan ()tidak dikawinkan melainkan hidup seperti malaikat di sorga.",
        "Sebab sama seperti maut datang karena satu orang manusia, demikian juga :kebangkitan orang mati datang karena satu ""orang manusia"]

class preprocessing:
    def __init__(self, _input):
        self.clean_container = []
        self.token_container = []
        self.filter_container = []
        self.stem_container = []
        self.term_container = []
        self._input = _input
        
    def cleaning(self): #clean unnecessary data
        if type(self._input) == str:
            output = re.sub(r"[\d\,\(\)\"!\.:\-;&\?]+", " ", self._input)
            self.clean_container.append(output)
        else:
            for x in self._input:    
                output = re.sub(r"[\d\,\(\)\"!\.:\-;&\?]+", " ", x)
                self.clean_container.append(output)
        return self.clean_container
    
    def tokenization(self): #lowercase the input and slit the input
        self.cleaning()
        for i in self.clean_container:
            lowercase = i.lower()
            split_data = lowercase.split()
            self.token_container.append(split_data)
        return self.token_container
    
    def filtering(self, stoplist): # filter data with stoplist
        self.tokenization()
        with open(stoplist, "r") as f:
            content = f.read()
            hasil = set(content.splitlines())
            
        for x in self.token_container:
            temp_container = []
            for y in x:
                if y not in hasil:
                    temp_container.append(y)
            self.filter_container.append(temp_container)
        return self.filter_container
    
    def stemming(self, stoplist=None):#stem the word
        if stoplist:
            self.filtering(stoplist)
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()
            for x in self.filter_container:
                join_array = " ".join(x)
                hasil = stemmer.stem(join_array)
                self.stem_container.append(hasil.split())
            return self.stem_container
            
        else:
            self.tokenisasi()
            factory = StemmerFactory()
            stemmer = factory.create_stemmer()
            for x in self.token_container:
                join_array = " ".join(x)
                hasil = stemmer.stem(join_array)
                self.stem_container.append(hasil.split())
            return self.stem_container
    
    def term(self, stoplist=None): # remove duplicate
        if stoplist:
            self.stemming(stoplist)
            for x in self.stem_container:
                for y in x:
                    if y not in self.term_container:
                        self.term_container.append(y)
            
            return self.term_container
            
        else:
            self.stemming()
            for x in self.stem_container:
                for y in x:
                    if y not in self.term_container:
                        self.term_container.append(y)
            
            return self.term_container

def testing():
    return "test"
# =============================================================================
# data_input = preprocesssing(content)
# 
# print(data_input.stemming())
# =============================================================================
