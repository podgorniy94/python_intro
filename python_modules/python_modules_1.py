# Vytvořit si vlastní modul (10)
import sys
file_path = '../my_modules'
sys.path.append(file_path)
import divide_two_numbers as dtn

dtn.divide_two_numbers()
