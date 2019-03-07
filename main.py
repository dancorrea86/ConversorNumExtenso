#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

class Janela(object):
	def __init__(self, toplevel):
		self.frame = Frame(toplevel, bg='gray')

		self.entry = Entry(self.frame, width='24')
		self.label = Entry(self.frame, bg='white', width='120')
		self.label_dois = Label(self.frame, text="Utilize '.' para milhares e ',' para centavos", bg='gray', font='Verdana')
		self.botao = Button(self.frame, width='6', text='Calc', command=c.separa)
		self.botao_dois = Button(self.frame, width='6', text='Limpa', command=c.limpa)

		
		self.frame.grid()
		self.label_dois.grid(row=0, column=0)
		self.entry.grid(row=1, column=0, padx=5, pady=5)
		self.botao.grid(row=1, column=1, padx=5, pady=5)
		self.label.grid(row=2, columnspan=3, padx=5, pady=5)
		self.botao_dois.grid(row=1, column=2, padx=5, pady=5)
		
class Calculos(object):

	def separa(self):
		self.entrada = str(j.entry.get())
		self.entradas_div_um = self.entrada.split(',')
		self.entradas_div_dois = self.entradas_div_um[0]
		self.entradas_div_tres = self.entradas_div_dois.split('.')
		self.centavos = self.entradas_div_um[len(self.entradas_div_um) - 1]
		self.reais = self.entradas_div_tres[-1]
		try:
			self.milhar = self.entradas_div_tres[-2]
		except:
			self.milhar = ''
		try:
			self.milhao = self.entradas_div_tres[-3]
		except:
			self.milhao = ''
		
		centavos_ter_casa = c.terceira_casa(self.centavos)
		centavos_seg_casa = c.segunda_casa(self.centavos)
		centavos_prim_casa = c.primeira_casa(self.centavos, centavos_seg_casa)

		reais_ter_casa = c.terceira_casa(self.reais)
		reais_seg_casa = c.segunda_casa(self.reais)
		reais_prim_casa = c.primeira_casa(self.reais, reais_seg_casa)

		milhar_ter_casa = c.terceira_casa(self.milhar)
		milhar_seg_casa = c.segunda_casa(self.milhar)
		milhar_prim_casa = c.primeira_casa(self.milhar, milhar_seg_casa)

		milhoes_ter_casa = c.terceira_casa(self.milhao)
		milhoes_seg_casa = c.segunda_casa(self.milhao)
		milhoes_prim_casa = c.primeira_casa(self.milhao, milhoes_seg_casa)

		if self.centavos == '' or self.centavos == '00':
			self.tipo_centavos = ''
		elif self.centavos == '01':
			self.tipo_centavos = ' centavo'
		else:
			self.tipo_centavos = ' centavos'

		if self.reais == '' or self.reais == '00':
			self.tipo_reais = ''
		elif self.reais == '01' or self.reais == '1' and self.centavos != '00':
			self.tipo_reais = ' real e'
		elif self.reais == '01' or self.reais == '1':
			self.tipo_reais = ' real'
		elif self.centavos != '00':
			self.tipo_reais = ' reais e '
		else:
			self.tipo_reais = ' reais'

		if self.milhar == '' or self.milhar == '00' or self.milhar == '000':
			self.tipo_milhar = ''
		else:
			self.tipo_milhar = ' mil '

		if self.milhao == '' or self.milhao == '00':
			self.tipo_milhao = ''
		elif self.milhao == '01' or self.milhao == '1':
			self.tipo_milhao = ' milhão '
		else:
			self.tipo_milhao = ' milhões '

		
		j.label.insert(0, ("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" %(milhoes_ter_casa, milhoes_seg_casa, milhoes_prim_casa, self.tipo_milhao, milhar_ter_casa, milhar_seg_casa, milhar_prim_casa, self.tipo_milhar, reais_ter_casa, reais_seg_casa, reais_prim_casa, self.tipo_reais, centavos_seg_casa, centavos_prim_casa, self.tipo_centavos)))
 
 	def limpa(self):
		self.entrada = ''
		j.label.delete(0, END)
		j.entry.delete(0, END)

	def terceira_casa(self, x):
		if len(x) == 3:
			if x[0] == '1' and x[1] == '0' and x[2] == '0':
				z = 'cem'
			elif x[0] == '2' and x[1] == '0' and x[2] == '0':
				z = 'duzentos'
			elif x[0] == '3' and x[1] == '0' and x[2] == '0':
				z = 'trezentos'
			elif x[0] == '4' and x[1] == '0' and x[2] == '0':
				z = 'quatrocentos'
			elif x[0] == '5' and x[1] == '0' and x[2] == '0':
				z = 'quinhentos'		
			elif x[0] == '6' and x[1] == '0' and x[2] == '0':
				z = 'seiscentos'
			elif x[0] == '7' and x[1] == '0' and x[2] == '0':
				z = 'setecentos'	
			elif x[0] == '8' and x[1] == '0' and x[2] == '0':
				z = 'oitocentos'
			elif x[0] == '9' and x[1] == '0' and x[2] == '0':
				z = 'novecentos'		
			elif x[0] == '1':
				z = 'cento e '
			elif x[0] == '2':
				z = 'duzentos e '
			elif x[0] == '3':
				z = 'trezentos e '
			elif x[0] == '4':
				z = 'quatrocentos e '
			elif x[0] == '5':
				z = 'quinhentos e '
			elif x[0] == '6':
				z = 'seiscentos e '
			elif x[0] == '7':
				z = 'setecentos e '
			elif x[0] == '8':
				z = 'oitocentos e '
			elif x[0] == '9':
				z = 'novecentos e '
			else:
				z = ''
		else:
			z = ''
		return z

	#função deterninar segunda casa
	def segunda_casa(self, x):
		if len(x) == 1:
			z = ''
		elif len(x) == 0:
			z = ''
		else:
			if len(x) == 2:
				num = 0
			else:
				num = 1	
			
			if x[num] == '1' and x[num + 1] == '1':
				z = 'onze'
			elif x[num] == '1' and x[num + 1] == '2':
				z = 'doze'
			elif x[num] == '1' and x[num + 1] == '3':
				z = 'treze'
			elif x[num] == '1' and x[num + 1] == '4':
				z = 'catorze'
			elif x[num] == '1' and x[num + 1] == '5':
				z = 'quinze'
			elif x[num] == '1' and x[num + 1] == '6':
				z = 'dezesseis'
			elif x[num] == '1' and x[num + 1] == '7':
				z = 'dezessete'
			elif x[num] == '1' and x[num + 1] == '8':
				z = 'dezoito'
			elif x[num] == '1' and x[num + 1] == '9':
				z = 'dezenove'
			elif x[num] == '2' and x[num + 1] == '0':
				z = 'vinte'
			elif x[num] == '3' and x[num + 1] == '0':
				z = 'trinta'
			elif x[num] == '4' and x[num + 1] == '0':
				z = 'quarenta'
			elif x[num] == '5' and x[num + 1] == '0':
				z = 'cinquenta'
			elif x[num] == '6' and x[num + 1] == '0':
				z = 'sessenta'
			elif x[num] == '7' and x[num + 1] == '0':
				z = 'setenta'
			elif x[num] == '8' and x[num + 1] == '0':
				z = 'oitenta'
			elif x[num] == '9' and x[num + 1] == '0':
				z = 'noventa' 
			elif x[num] == '1':
				z = 'dez'
			elif x[num] == '2':
				z = 'vinte e '
			elif x[num] == '3':
				z = 'trinta e '
			elif x[num] == '4':
				z = 'quarenta e '
			elif x[num] == '5':
				z = 'cinquenta e '
			elif x[num] == '6':
				z = 'sessenta e '
			elif x[num] == '7':
				z = 'setenta e '
			elif x[num] == '8':
				z = 'oitenta e '
			elif x[num] == '9':
				z = 'noventa e '
			else:
				z = ''
		return z

	# função deterninar primeira casa
	def primeira_casa(self, x, y):
		if len(x) == 0:
			z = ''
		else:	
			if len(x) == 2:
				num = 0
			elif len(x) == 1:
				num = -1
			else:
				num = 1

			if y == 'dez' or y == 'onze' or y == 'doze' or y == 'treze' or y == 'catorze' or y == 'quinze' or y == 'dezesseis' or y == 'dezessete' or y == 'dezoito' or y =='dezenove':
				z = ''
			else:
				if x[num + 1] == '1':
					z = 'um'
				elif x[num + 1] == '2':
					z = 'dois'
				elif x[num + 1] == '3':
					z = 'tres'
				elif x[num + 1] == '4':
					z = 'quatro'
				elif x[num + 1] == '5':
					z = 'cinco'
				elif x[num + 1] == '6':
					z = 'seis'
				elif x[num + 1] == '7':
					z = 'sete'
				elif x[num + 1] == '8':
					z = 'oito'
				elif x[num + 1] == '9':
					z = 'nove'
				else:
					z = ''
		return z


c = Calculos()

raiz = Tk()
j = Janela(raiz)
raiz.mainloop()	
