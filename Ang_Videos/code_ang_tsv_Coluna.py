#gera angulos a partir do tsv em output_angle.tsv

import csv
import numpy 
import math
import glob


#output_angle = 'D:/Faculdade/PET/Fisioterapia/Fisioterapia_tsv_Videos/angulos/Coluna/ang_Coluna_tsv.tsv'

def calculate_angle2(point1, point2, point3):
    # Calculate vectors from point2 to point1 and point2 to point3
    vector1 = [point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]]
    vector2 = [point3[0] - point2[0], point3[1] - point2[1], point3[2] - point2[2]]

    # Calculate the dot product of the two vectors
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    # Calculate the magnitudes of the two vectors
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    # Calculate the angle in radians
    angle_radians = math.acos(dot_product / (magnitude1 * magnitude2))

    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

def calculate_angle(point1, point2, point3):
    # Calculate vectors from point2 to point1 and point2 to point3
    vector1 = [point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]]
    vector2 = [point3[0] - point2[0], point3[1] - point2[1], point3[2] - point2[2]]

    # Calculate the dot product of the two vectors
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    # Calculate the magnitudes of the two vectors
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    # Calculate the angle in radians
    angle_radians = math.acos(dot_product / (magnitude1 * magnitude2))

    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    # Check if the angle is greater than 180 degrees
    if angle_degrees > 180:
        # If so, adjust it to be its complement
        angle_degrees = 360 - angle_degrees

    return angle_degrees


count = 0
#funçao que calcula o comprimento de um vetor
def modulo_vetor(x, y, z):
                
    v = (x**2 + y**2 + z**2)**0.5
                
    return v
            
'''funçao que retona um vetor normalizado, ou seja, um vetor na mesma direção mas com norma igual a 1'''
def normaliza_vetor(x, y, z):
                
    aux = modulo_vetor(x, y, z)
                
    v = [x/aux, y/aux, z/aux]
                
    return v

'''funçao que recebe como parametro as coordenadas de dois pontos, 
que sao os extremos das duas retas, ou seja, esses dois pontos definem essa reta. ela retorna a direção da reta no espaço'''
def calcula_inclinacao(x1, y1, z1, x2, y2, z2):
                
    vetor_diretor = [(x2 - x1), (y2 - y1), (z2 - z1)]
                
    return normaliza_vetor(*vetor_diretor)
                
'''função recebe as coordenadas de 4 pontos, 2 de uma reta (final e inicial) e 2 de outra'''
def angulo_de_flexao(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4):
    inclinacao_reta1 = calcula_inclinacao(x1, y1, z1, x2, y2, z2)
    inclinacao_reta2 = calcula_inclinacao(x3, y3, z3, x4, y4, z4)
                
    produto_escalar = 0.0
                
    for v1, v2 in zip(inclinacao_reta1, inclinacao_reta2):
        produto_escalar += v1 * v2
             
    angulo = math.acos(produto_escalar)

    # Convertendo para graus
    angulo_graus = math.degrees(angulo)
    
    # Verificando se o ângulo é maior que 180 graus
    if angulo_graus > 180:
        # Se for, ajusta para seu complemento em relação a 360 graus
        angulo_graus = 360 - angulo_graus

    return angulo_graus

#
# explicar csv_out
count = 0
diretorio = 'C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Ang_Videos/output/Coluna'
arquivos_tsv = glob.glob(f'{diretorio}/*.tsv')

# Abra o arquivo de saída uma vez fora do loop
output_angle = 'C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Ang_Videos/angulos/Coluna/output_angulos_TC_FL_F.tsv'
with open(output_angle, 'a', newline='') as tsv_out:
    writer = csv.writer(tsv_out, delimiter='\t')
    
    for input_file in arquivos_tsv:
        with open(input_file, 'r') as tsv_in:
            reader = csv.reader(tsv_in, delimiter='\t')
            frame = 0
            count = 0
            for row in reader:

            
                # flexao cabeca meio cabeça meio ombro meio cintura
                x1_, y1_, z1_ = map(float, row[36:39])  # meio cabeça
                x2_, y2_, z2_ = map(float, row[39:42])  # meio ombro
                x3_, y3_, z3_ = map(float, row[42:45])  # meio cintura

                ponto1 = [x1_, y1_, z1_]
                ponto2= [x2_, y2_, z2_]
                ponto3 = [x3_, y3_, z3_]

                flexao_cabeca = calculate_angle(ponto1, ponto2, ponto3)

                #////////////////////////////////////////////////////////////////////////////////////////

                # flexao tronco meio ombro meio cintura meio knee
                x11, y11, z11 = map(float, row[39:42])  # meio ombro
                x22, y22, z22 = map(float, row[42:45])  # meio cintura
                x33, y33, z33 = map(float, row[45:48])  # meio knee
        
                ponto11 = [x11, y11, z11]
                ponto22= [x22, y22, z22]
                ponto33 = [x33, y33, z33]

                flexao_tronco = calculate_angle(ponto11, ponto22, ponto33)
                
                #///////////////////////////////////////////////////////////////////////////////////////

                # rotação tronco shoulder1 shoulder2 hip1 hip2
                X, Y, Z = map(float, row[6:9])  # shoulder1
                X1, Y1, Z1 = map(float, row[9:12])  # shoulder2
                X2, Y2, Z2 = map(float, row[18:21]) # hip1
                X3, Y3, Z3 = map(float, row[21:24]) # hip2


            

                

                ponto111 = [X, Y, Z ]
                ponto222= [X1, Y1, Z1]
                ponto333 = [X2, Y2, Z2]
                ponto4 = [X3, Y3, Z3]
    
                x_inicial, y_inicial, z_inicial = ponto222
                x_final, y_final, z_final = ponto111
                x1_inicial, y1_inicial, z1_inicial = ponto4
                x1_final, y1_final, z1_final = ponto333


                rotacao_tronco = angulo_de_flexao(x_inicial, y_inicial, z_inicial, x_final, y_final, z_final, x1_inicial, y1_inicial, z1_inicial, x1_final, y1_final, z1_final  )
                
                #///////////////////////////////////////////////////////////////////////////////////////
                # "flexao cabeca:", flexao_cabeca, "flexao tronco:", flexao_tronco, 

                new_row = ["flexao tronco:", flexao_tronco]

                writer.writerow(new_row)



            count += 1
