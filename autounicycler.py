import os
import argparse
import subprocess


parser = argparse.ArgumentParser(
    description='running autounicycler')

parser.add_argument('-i', '--input', metavar='', type=str, required=True,
                    help='Path to the files i.e: home/usr/Desktop/myfiles')
parser.add_argument('-t', '--thread', metavar='', type=int, required=False,
                    help='[OPTIONAL] Number of threads i.e: 8')

args = parser.parse_args()

diretorio = os.path.expanduser(f'{args.input}') 


def function(diretorio):
    lista = []
    os.chdir(diretorio)
    if 'results_autounicycler' not in os.listdir():
        os.mkdir('results_autounicycler')
        
    for files_to_be_aseembled in os.listdir():
        if files_to_be_aseembled.endswith('.fastq'):
            lista.append(files_to_be_aseembled)
            
    lista.sort()
    
    lista2 = []
    for cada_item_da_lista in range(0, len(lista), 2):
        
        lista2 = lista[cada_item_da_lista:cada_item_da_lista+2]

        os.mkdir(os.path.join(f'{diretorio}', 'results_autounicycler', f'{lista2[0]}'))
        caminho = os.path.join(f'{diretorio}', 'results_autounicycler', f'{lista2[0]}')
        
        if args.thread:
            command_line = ['unicycler', '-1', f'{lista2[0]}', '-2', f'{lista2[1]}', '-o', f'{caminho}', '-t', args.thread]
            print(command_line)
            
        else:
            command_line = ['unicycler', '-1', f'{lista2[0]}', '-2', f'{lista2[1]}', '-o', f'{caminho}']
            print(command_line)
            
if __name__ == '__main__':
    function(diretorio)