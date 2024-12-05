import glob

# codigo que le todos os angulos de todas as variaveis (tanto pra MMMSS como pra COLUNA) nos arquivos
# e salva todos esses valores em listas contendo o nome das variaveis
# posteriormente usa essas listas para fazer o calculo estatistico


# função que calcula a correlação entre dados que estão presentes em duas listas
def correlacao(lista_ouro, lista_video):
    
    soma_x = 0.0
    soma_y = 0.0
    soma_quadrado_x = 0.0
    soma_quadrado_y = 0.0
    soma_x_y = 0.0

    # i eh o numero de pares ordenados. as listas devem possuir o mesmo tamanho!!

    # usando a menor lista como referencia, para não dar erro de acesso indevido na lista menor
    if(len(lista_ouro) > len(lista_video)):
        
        for i in range(len(lista_video)):
            soma_x += lista_ouro[i]
            soma_y += lista_video[i]
            soma_quadrado_x += lista_ouro[i] ** 2
            soma_quadrado_y += lista_video[i] ** 2
            soma_x_y += lista_ouro[i] * lista_video[i]


        n = len(lista_video)    
        aux_1 = ((n * soma_quadrado_x - soma_x**2)**0.5)
        aux_2 = ((n * soma_quadrado_y - soma_y**2 )**0.5)

        # calculados os termos necessarios, agr eh so aplicar esses numeros na expressao matematica que calcula a correlaçao

        correlacao = ((n * soma_x_y) - soma_x * soma_y ) / (aux_1 * aux_2)

        return correlacao
    
    else:

        for i in range(len(lista_ouro)):
            soma_x += lista_ouro[i]
            soma_y += lista_video[i]
            soma_quadrado_x += lista_ouro[i] ** 2
            soma_quadrado_y += lista_video[i] ** 2
            soma_x_y += lista_ouro[i] * lista_video[i]


        n = len(lista_ouro)    
        aux_1 = ((n * soma_quadrado_x - soma_x**2)**0.5)
        aux_2 = ((n * soma_quadrado_y - soma_y**2 )**0.5)
        
        correlacao = ((n * soma_x_y) - soma_x * soma_y ) / (aux_1 * aux_2)

        return correlacao
   



# função que recebe duas listas e calcula o erro medio absoluto entre os dados
# essas listas devem possuir o mesmo tamanho
# uma lista contém os ângulos calculados a partir dos videos
# a outra lista contém os ângulos calculados a partir dos tsv
def erro_medio_absoluto(lista_ouro, lista_video):
    
    # lista que vai guardar cada um dos erros absoluto entre os ângulos
    #erro_medio = []

    if(len(lista_ouro) > len(lista_video)):
        soma = 0

        for i in range(len(lista_video)):
            soma += abs(lista_ouro[i] - lista_video[i])


        return soma / len(lista_video)    

    else:
        soma = 0

        for i in range(len(lista_ouro)):
            soma += abs(lista_ouro[i] - lista_video[i])

        return soma / len(lista_ouro)
 

    

# DECLARANDO AS LISTAS PARA REPRESENTAR TODAS AS VARIAVEIS
# MMSS
## OBSERVAÇÃO: FRONTAL = 30 FRAMES  // LATERAL = 60 FRAMES

abd_ombro_esquerdo_ouro = []
abd_ombro_esquerdo_video_frontal = []
abd_ombro_esquerdo_video_lateral = []



# COLUNA
# OBSERVACAO: FRONTAL = 60 FRAMES   // LATERAL = 30 FRAMES

flexao_cabeca_ouro = []
flexao_cabeca_video_frontal = []
flexao_cabeca_video_lateral = []


flexao_tronco_ouro = []
flexao_tronco_video_frontal = []
flexao_tronco_video_lateral = []

'''
rotacao_tronco_ouro = []
rotacao_tronco_video_frontal = []
rotacao_tronco_video_lateral = []'''


# busca por todos os arquivos TSV no diretorio especificado

#----------- FLEXAO CABECA ------------------------------------------# 
pasta_CB_FL_ouro = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/COLUNA/CB_FL/padrao_ouro/*.tsv")
pasta_CB_FL_video_frontal = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/COLUNA/CB_FL/video_frontal/*.tsv")
#pasta_video_frontal_MMSS = glob.glob("C:/Users/jhona/Downloads/Estatistica-main/MMSS/video_mmss/frontal/*.tsv")
pasta_CB_FL_video_lateral = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/COLUNA/CB_FL/video_lateral/*.tsv")


#-------------- FLEXAO TRONCO --------------------------------------------------#
pasta_TC_FL_ouro = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/COLUNA/TC_FL/padrao_ouro/*.tsv")
pasta_TC_FL_video_frontal = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/COLUNA/TC_FL/video_frontal/*.tsv")
pasta_TC_FL_video_lateral = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/COLUNA/TC_FL/video_lateral/*.tsv")



#-------------------------- ABDUCAO OMBRO ESQUERDO ------------------------------------------#
pasta_OMB_ABD_ouro = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/MMSS/OMB_ABD/padrao_ouro/*.tsv")
pasta_OMB_ABD_video_frontal = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/MMSS/OMB_ABD/video_frontal/*.tsv")
pasta_OMB_ABD_video_lateral = glob.glob("C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Estatistica/MMSS/OMB_ABD/video_lateral/*.tsv")




################################################################################################################
################################################################################################################
#                                   MMSS

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE ABD OMBRO ESQUERDO PADRAO OURO
# E SALVANDO NAS LISTAS OS ANGULOS

for nome_arquivo in pasta_OMB_ABD_ouro:

    with open(nome_arquivo, 'r') as ouro_MMSS:
        for i in ouro_MMSS.readlines():

            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_ouro.append(float(coluna[2]))
            #print(abd_ombro_esquerdo_ouro[0])



# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE ABD OMBRO ESQUERDO VIDEO FRONTAL
# E SALVANDO NAS LISTAS OS ANGULOS

for nome_arquivo in pasta_OMB_ABD_video_frontal:

    with open(nome_arquivo, 'r') as ouro_MMSS:
        for i in ouro_MMSS.readlines():

            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_video_frontal.append(float(coluna[1]))





# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE ABD OMBRO ESQUERDO VDEO LATERAL
# E SALVANDO NAS LISTAS OS ANGULOS

for nome_arquivo in pasta_OMB_ABD_video_lateral:

    with open(nome_arquivo, 'r') as ouro_MMSS:
        print(nome_arquivo)
        for i in ouro_MMSS.readlines():

            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_video_lateral.append(float(coluna[1]))



################################################################################################################
################################################################################################################
#                                   COLUNA

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE FLEXAO CABECA PADRAO OURO
# E SALVANDO NAS LISTAS OS ANGULOS

for nome_arquivo in pasta_CB_FL_ouro:

    with open(nome_arquivo, 'r') as coluna_ouro:

        for i in coluna_ouro.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO CABECA -------------- ##
            flexao_cabeca_ouro.append(float(coluna[1]))
            #print("Lista flexao_cabeca_ouro:", flexao_cabeca_ouro[1])

            ## ----------- FLEXAO TRONCO -------------- ##
            #flexao_tronco_ouro.append(float(coluna[1]))

            ## ----------- ROTACAO TRONCO -------------- ##
            #rotacao_tronco_ouro.append(float(coluna[5]))



# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE FLEXAO CABECA VIDEO FRONTAL
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_CB_FL_video_frontal:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            flexao_cabeca_video_frontal.append(float(coluna[1]))




# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE FLEXAO CABECA VIDEO LATERAL
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_CB_FL_video_lateral:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            flexao_cabeca_video_lateral.append(float(coluna[1]))





# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE FLEXAO TRONCO PADRAO OURO
# E SALVANDO NAS LISTAS OS ANGULOS

for nome_arquivo in pasta_TC_FL_ouro:

    with open(nome_arquivo, 'r') as coluna_ouro:

        for i in coluna_ouro.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO TRONCO -------------- ##
            flexao_tronco_ouro.append(float(coluna[1]))




# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE FLEXAO TRONCO VIDEO FRONTAL
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_TC_FL_video_frontal:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            flexao_tronco_video_frontal.append(float(coluna[1]))




# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DE FLEXAO TRONCO VIDEO LATERAL
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_TC_FL_video_lateral:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            flexao_tronco_video_lateral.append(float(coluna[1]))




##############################################################################################################
#### AQUI TERMINA A LEITURA DOS ANGULOS



#--------------------------- FLEXAO CABECA -------------------------------------------#
print("#=========================== FLEXAO CABECA ==================================#")
print("\n")
erro_CB_FL_ouro_frontal = erro_medio_absoluto(flexao_cabeca_ouro, flexao_cabeca_video_frontal)
print(f"Erro Médio Absoluto para flexao cabeca entre o video FRONTAL e o Padrão Ouro: {erro_CB_FL_ouro_frontal}")

erro_CB_FL_ouro_lateral = erro_medio_absoluto(flexao_cabeca_ouro, flexao_cabeca_video_lateral)
print(f"Erro Médio Absoluto para flexao cabeca entre o video LATERAL e o Padrão Ouro: {erro_CB_FL_ouro_lateral}")

corr_CB_FL_ouro_frontal = correlacao(flexao_cabeca_ouro, flexao_cabeca_video_frontal)
print(f"Correlação para flexao cabeca entre o video FRONTAL e o Padrão Ouro: {corr_CB_FL_ouro_frontal}")

corr_CB_FL_ouro_lateral = correlacao(flexao_cabeca_ouro, flexao_cabeca_video_lateral)
print(f"Correlação para flexao cabeca entre o video LATERAL e o Padrão Ouro: {corr_CB_FL_ouro_lateral}")


print(f"Angulo máximo Padrão Ouro flexao cabeca: {max(flexao_cabeca_ouro)}")
print(f"Angulo mínimo Padrão Ouro flexao cabeca: {min(flexao_cabeca_ouro)}")
print(f"Amplitude Padrão Ouro flexao flexao cabeca: {max(flexao_cabeca_ouro) - min(flexao_cabeca_ouro)}")

print(f"Angulo máximo video FRONTAL flexao cabeca: {max(flexao_cabeca_video_frontal)}")
print(f"Angulo mínimo video FRONTAL flexao cabeca: {min(flexao_cabeca_video_frontal)}")
print(f"Amplitude video FRONTAL flexao cabeca: {max(flexao_cabeca_video_frontal) - min(flexao_cabeca_video_frontal)}")

print(f"Angulo máximo video LATERAL flexao cabeca: {max(flexao_cabeca_video_lateral)}")
print(f"Angulo mínimo video LATERAL flexao cabeca: {min(flexao_cabeca_video_lateral)}")
print(f"Amplitude video LATERAL flexao cabeca: {max(flexao_cabeca_video_lateral) - min(flexao_cabeca_video_lateral)}")
print("\n")


#--------------------------- FLEXAO TRONCO -------------------------------------------#
print("#=========================== FLEXAO TRONCO ==================================#")
print("\n")

erro_TC_FL_ouro_frontal = erro_medio_absoluto(flexao_tronco_ouro, flexao_tronco_video_frontal)
print(f"Erro Médio Absoluto para flexao tronco entre o video FRONTAL e o Padrão Ouro: {erro_TC_FL_ouro_frontal}")


erro_TC_FL_ouro_lateral = erro_medio_absoluto(flexao_tronco_ouro, flexao_tronco_video_lateral)
print(f"Erro Médio Absoluto para flexao tronco entre o video LATERAL e o Padrão Ouro: {erro_TC_FL_ouro_lateral}")

corr_TC_FL_ouro_frontal = correlacao(flexao_tronco_ouro, flexao_tronco_video_frontal)
print(f"Correlação para flexao tronco entre o video FRONTAL e o Padrão Ouro: {corr_TC_FL_ouro_frontal}")

corr_TC_FL_ouro_lateral = correlacao(flexao_tronco_ouro, flexao_tronco_video_lateral)
print(f"Correlação para flexao tronco entre o video LATERAL e o Padrão Ouro: {corr_TC_FL_ouro_lateral}")


print(f"Angulo máximo Padrão Ouro flexao tronco: {max(flexao_tronco_ouro)}")
print(f"Angulo mínimo Padrão Ouro flexao tronco: {min(flexao_tronco_ouro)}")
print(f"Amplitude Padrão Ouro flexao flexao tronco: {max(flexao_tronco_ouro) - min(flexao_tronco_ouro)}")

print(f"Angulo máximo video FRONTAL flexao tronco: {max(flexao_tronco_video_frontal)}")
print(f"Angulo mínimo video FRONTAL flexao tronco: {min(flexao_tronco_video_frontal)}")
print(f"Amplitude video FRONTAL flexao tronco: {max(flexao_tronco_video_frontal) - min(flexao_tronco_video_frontal)}")

print(f"Angulo máximo video LATERAL flexao tronco: {max(flexao_tronco_video_lateral)}")
print(f"Angulo mínimo video LATERAL flexao tronco: {min(flexao_tronco_video_lateral)}")
print(f"Amplitude video LATERAL flexao tronco: {max(flexao_tronco_video_lateral) - min(flexao_tronco_video_lateral)}")





#-------------------------- ABDUCAO OMBRO ESQUERDO ------------------------#
print("\n")
print("#=========================== ABDUCAO OMBRO ESQUERDO ==================================#")
print("\n")

erro_OMB_ABD_ouro_frontal = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_frontal)
print(f"Erro Médio Absoluto para ABDUCAO OMBRO ESQUERDO entre o video FRONTAL e o Padrão Ouro: {erro_OMB_ABD_ouro_frontal}")

erro_OMB_ABD_ouro_lateral = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_lateral)
print(f"Erro Médio Absoluto para ABDUCAO OMBRO ESQUERDO entre o video LATERAL e o Padrão Ouro: {erro_OMB_ABD_ouro_lateral}")

corr_OMB_ABD_ouro_frontal = correlacao(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_frontal)
print(f"Correlação para ABDUCAO OMBRO ESQUERDO entre o video FRONTAL e o Padrão Ouro: {corr_OMB_ABD_ouro_frontal}")

corr_OMB_ABD_ouro_lateral = correlacao(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_lateral)
print(f"Correlação para ABDUCAO OMBRO ESQUERDO entre o video LATERAL e o Padrão Ouro: {corr_OMB_ABD_ouro_lateral}")

print(f"Angulo máximo Padrão Ouro ABDUCAO OMBRO ESQUERDO: {max(abd_ombro_esquerdo_ouro)}")
print(f"Angulo minimo Padrão Ouro ABDUCAO OMBRO ESQUERDO: {min(abd_ombro_esquerdo_ouro)}")
print(f"Amplitude Padrão Ouro ABDUCAO OMBRO ESQUERDO: {max(abd_ombro_esquerdo_ouro) - min(abd_ombro_esquerdo_ouro)}")

print(f"Angulo máximo video FRONTAL ABDUCAO OMBRO ESQUERDO: {max(abd_ombro_esquerdo_video_frontal)}")
print(f"Angulo minimo video FRONTAL ABDUCAO OMBRO ESQUERDO: {min(abd_ombro_esquerdo_video_frontal)}")
print(f"Amplitude video FRONTAL ABDUCAO OMBRO ESQUERDO: {max(abd_ombro_esquerdo_video_frontal) - min(abd_ombro_esquerdo_video_frontal)}")


print(f"Angulo máximo video LATERAL ABDUCAO OMBRO ESQUERDO: {max(abd_ombro_esquerdo_video_lateral)}")
print(f"Angulo minimo video LATERAL ABDUCAO OMBRO ESQUERDO: {min(abd_ombro_esquerdo_video_lateral)}")
print(f"Amplitude video LATERAL ABDUCAO OMBRO ESQUERDO: {max(abd_ombro_esquerdo_video_lateral) - min(abd_ombro_esquerdo_video_lateral)}")
