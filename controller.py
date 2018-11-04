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


# git bug

















