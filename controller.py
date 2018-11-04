# funcoes controladoras

class Controller:
    def __init__(self):
        self.listaCleaner = []
        self.listaStemmer = []
        self.cleanerAtivo = 0       # valor que vai indicar os butoes do cleaner que foram selecionados

    def getOpcoesCleaner(self, listaCleaner):
    # Retorna um inteiro que representa quais opcoes foram selecionadas para o cleaner
        if len(listaCleaner) != 0 :
            verificador = len(listaCleaner)
            addr = 1
            i = 0
            while(1):
                if i == verificador:
                    break	
                addr = addr * int(listaCleaner[i])
                i = i + 1
            self.cleanerAtivo = addr
            return addr


    def geraJsonCleaner(self):
        c = '"'
        arquivo = open("preprocess.json", "w")
        arquivo.write("\tvar preprocessor = {\n")
        if (self.cleanerAtivo) != 0:
            if (self.cleanerAtivo % 2) == 0:
                    arquivo.write("\t\t %sremoveaccents%s : %sFalse%s,\n" %(c, c, c, c))
            if (self.cleanerAtivo % 3) == 0:
                    arquivo.write("\t\t %sremove_alpha_numeric%s : %sFalse%s,\n" %(c, c, c, c))
            if (self.cleanerAtivo % 5) == 0:
                    arquivo.write("\t\t %smax_word_lenght%s : %s3%s\n" %(c, c, c, c))
        arquivo.write("};")
        arquivo.close()            


# git bug

















