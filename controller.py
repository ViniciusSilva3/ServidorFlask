from json import dumps
# funcoes controladoras

class Controller:
    def __init__(self):
        self.listaCleaner = []
        self.listaStemmer = []
        self.cleanerAtivo = 0       # valor que vai indicar os butoes do cleaner que foram selecionados

    def geraJsonCleaner(self):
        c = '"'
        geravirgulas = 0
        arquivo = open("preprocess.json", "w")
        arquivo.write("\tvar preprocessor = {\n")
        if (len(self.listaCleaner)) != 0:
            for i in range(0, len(self.listaCleaner) ):
                self.cleanerAtivo = 1 # indica para o controlador que foram passados parametros de cleaner
                if ( self.listaCleaner[i] ) == '2':
                    arquivo.write("\t\t %sremoveaccents%s : %sFalse%s" %(c, c, c, c))
                    geravirgulas = 1
                if ( self.listaCleaner[i] ) == '3':
                    if geravirgulas == 1:
                        arquivo.write(",\n")
                    arquivo.write("\t\t %sremove_alpha_numeric%s : %sFalse%s" %(c, c, c, c))
                if (self.listaCleaner[i]) == '5':                    
                    if geravirgulas == 1:
                        arquivo.write(",\n")
                    arquivo.write("\t\t %smax_word_lenght%s : %s3%s" %(c, c, c, c))
        arquivo.write("\n};")
        arquivo.close()  

    def geraDefaultCleaner(self):
        #talvez seja mais facil ja fazer na implementacao junto com o professor
        a = 1          

    def verificaS(self, string):
    	if (string==''):
    		return None
    	else:
    		return string

    def splitWords(self, string):
    	'''
    	Função que recebe a string da caixa de texto da página e retorna na forma de lista
    	Argumento: string referente ao que foi digitado na caixa, separadas por vírgula e/ou espaço em branco
    	Retorno: lista de palavras
    	'''
    	if string != '':
    		lista = string.replace(' ', '')
    		lista = string.split(',')
    		return lista
    	else:
    		return None

    def geraArquivo(self, flagAc, flagAlp, flagToken, flagStem, maxWord=None, lan=None, lista=None):
    	json = {
    		"lang":"portuguese",
    		"stopword_list":None,
    		"remove_accents":True,
    		"tokenize":False,

    		"remove_alpha_numeric":True,
    		"max_word_length":2,

    		"stemmer_obj":None,
    		"fit_reuse":False
    	}
    	if lan != None:
    		if lan == 'portuguese':
    			json['lang'] = lan
    		elif lan == 'english':
    			json['lang'] = lan
    	if lista != None:
    		json['stopword_list'] = lista
    	json['remove_accents'] = flagAc
    	json['tokenize'] = flagToken
    	json['remove_alpha_numeric'] = flagAlp
    	if maxWord != None:
    		json['max_word_length'] = maxWord

    	jsonD = dumps(json, indent=4)
    	return jsonD