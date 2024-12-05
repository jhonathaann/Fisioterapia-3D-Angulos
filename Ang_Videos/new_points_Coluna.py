import csv
import glob
import os

# Função para calcular o ponto médio entre dois conjuntos de valores xyz
def calculate_midpoint(x1, y1, z1, x2, y2, z2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    midpoint_z = (z1 + z2) / 2
    return midpoint_x, midpoint_y, midpoint_z

# Especifica o diretório onde os arquivos TSV estão
diretorio = 'C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Ang_Videos/input/Coluna'
# Busca por todos os arquivos TSV no diretório especificado
arquivos_tsv = glob.glob(f'{diretorio}/*.tsv')

for input_file in arquivos_tsv:
    # Define o nome do arquivo de saída com base no nome do arquivo de entrada
    nome_arquivo = os.path.basename(input_file)
    output_file_points = os.path.join('C:/Users/jhona/OneDrive/Faculdade/PET/Fisioterapia 3D/Ang_Videos/output/Coluna', f'output_file_points_{nome_arquivo}')

    with open(input_file, 'r') as tsv_in, open(output_file_points, 'w', newline='') as tsv_out:
        reader = csv.reader(tsv_in, delimiter='\t')
        writer = csv.writer(tsv_out, delimiter='\t')

        for row in reader:

        
            #ponto medio do olho1 e olho2
            #_____________________________________________________________________________________________________________
            x1, y1, z1 = map(float, row[30:33]) #OLHO_1 
            x2, y2, z2 = map(float, row[33:36]) #OLHO_2

            midpoint_xC_D, midpoint_yC_D, midpoint_zC_D = calculate_midpoint(x1, y1, z1, x2, y2, z2)
            #_____________________________________________________________________________________________________________


            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////

            
            #ponto medio do shoulder1 e shoulder2
            #_____________________________________________________________________________________________________________
            x11, y11, z11 = map(float, row[6:9]) # shoulder1
            x22, y22, z22 = map(float, row[9:12]) # shoulder2

            midpoint_xP_D, midpoint_yP_D, midpoint_zP_D = calculate_midpoint(x11, y11, z11, x22, y22, z22)
            #_____________________________________________________________________________________________________________


            #/////////////////////////////////////////////////////////////////////////////////////////////////////////////


            #ponto medio do hip1 e hip2
            #_____________________________________________________________________________________________________________

            x111, y111, z111 = map(float, row[18:21]) #hip1
            x222, y222, z222 = map(float, row[21:24]) #hip2

            midpoint_xC_E, midpoint_yC_E, midpoint_zC_E = calculate_midpoint(x111, y111, z111, x222, y222, z222)
            #_____________________________________________________________________________________________________________


            #ponto medio do knee1 e knee2
            #_____________________________________________________________________________________________________________

            x14, y14, z14 = map(float, row[24:27]) # KNEE1
            x24, y24, z24 = map(float, row[27:30]) # KNEE2

            midpoint_xP_E, midpoint_yP_E, midpoint_zP_E = calculate_midpoint(x14, y14, z14, x24, y24, z24)
            
            # Append the midpoint xyz values to the row (MEIO CABEÇA 36:39) (MEIO OMBRO 39:42) (MEIO CINTURA 42:45) (MEIO KNEE 45:48)
            row.extend([midpoint_xC_D, midpoint_yC_D, midpoint_zC_D,
                        midpoint_xP_D, midpoint_yP_D, midpoint_zP_D,
                        midpoint_xC_E, midpoint_yC_E, midpoint_zC_E,
                        midpoint_xP_E, midpoint_yP_E, midpoint_zP_E])

            # Escreva a linha atualizada no arquivo de saída
            writer.writerow(row)
        