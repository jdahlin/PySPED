# -*- coding: utf-8 -*-


from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor

from geraldo import Report, ReportBand, BAND_WIDTH
from geraldo import ObjectValue, SystemField, Label, Line
import os


DIRNAME = os.path.dirname(__file__)


''' Margens e tamanhos padronizados '''
RETRATO = A4
PAISAGEM = landscape(A4)
MARGEM_SUPERIOR = 0.8*cm
MARGEM_INFERIOR = 1*cm
MARGEM_ESQUERDA = 0.8*cm
MARGEM_DIREITA = 0.8*cm
LARGURA_RETRATO = RETRATO[0] - MARGEM_ESQUERDA - MARGEM_DIREITA
LARGURA_PAISAGEM = PAISAGEM[0] - MARGEM_ESQUERDA - MARGEM_DIREITA


#
# Fontes adicionais
#
FONTES_ADICIONAIS = {
    u'Gentium Book Basic'            : DIRNAME + u'/fonts/genbasr.ttf',
    u'Gentium Book Basic Bold'       : DIRNAME + u'/fonts/genbasb.ttf',
    u'Gentium Book Basic Italic'     : DIRNAME + u'/fonts/genbasi.ttf',
    u'Gentium Book Basic Bold Italic': DIRNAME + u'/fonts/genbasbi.ttf',

}
#FONTES_ADICIONAIS = {
    #u'Gentium Book Basic': (
        #(u'Gentium Book Basic'            , DIRNAME + u'/fonts/genbasr.ttf' , False, False),
        #(u'Gentium Book Basic Bold'       , DIRNAME + u'/fonts/genbasb.ttf' , True , False),
        #(u'Gentium Book Basic Italic'     , DIRNAME + u'/fonts/genbasi.ttf' , False, True),
        #(u'Gentium Book Basic Bold Italic', DIRNAME + u'/fonts/genbasbi.ttf', True , True),
    #)
#}

#addMapping('Gentium Basic', 0, 0, 'Gentium Basic')
#addMapping('Gentium Basic', 1, 0, 'Gentium Basic Bold')
#addMapping('Gentium Basic', 0, 1, 'Gentium Basic Italic')
#addMapping('Gentium Basic', 1, 1, 'Gentium Basic Bold Italic')    

''' Estilos padronizados '''
#FONTE_NORMAL = 'Times New Roman'
#FONTE_NORMAL = 'Liberation Serif'
FONTE_NORMAL = 'Gentium Book Basic'
#FONTE_NORMAL = 'Libertine'
FONTE_NEGRITO = FONTE_NORMAL + ' Bold'
FONTE_ITALICO = FONTE_NORMAL + ' Italic'
FONTE_NEGRITO_ITALICO = FONTE_NORMAL + ' Bold Italic'

FONTE_TAMANHO_5 = 5
FONTE_TAMANHO_6 = FONTE_TAMANHO_5 + 1
FONTE_TAMANHO_7 = FONTE_TAMANHO_5 + 2
FONTE_TAMANHO_8 = FONTE_TAMANHO_5 + 3
FONTE_TAMANHO_85 = FONTE_TAMANHO_5 + 3.5
FONTE_TAMANHO_9 = FONTE_TAMANHO_5 + 4
FONTE_TAMANHO_10 = FONTE_TAMANHO_5 * 2
FONTE_TAMANHO_11 = FONTE_TAMANHO_10 + 1
FONTE_TAMANHO_12 = FONTE_TAMANHO_10 + 2
FONTE_TAMANHO_18 = FONTE_TAMANHO_10 + 8
FONTE_TAMANHO_40 = FONTE_TAMANHO_10 * 4

DESCRITIVO_BLOCO = {'fontName': FONTE_NEGRITO, 'fontSize': FONTE_TAMANHO_8}
DESCRITIVO_CAMPO = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_5}
DESCRITIVO_PRODUTO = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_5, 'alignment': TA_CENTER, 'leading': FONTE_TAMANHO_7}

DADO_CHAVE = {'fontName': FONTE_NEGRITO, 'fontSize': FONTE_TAMANHO_85, 'alignment': TA_CENTER}
DADO_VARIAVEL = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_9, 'alignment': TA_CENTER, 'leading': FONTE_TAMANHO_11}

DADO_CAMPO = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_10, 'leading': FONTE_TAMANHO_12}
DADO_CAMPO_NUMERICO = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_10, 'alignment': TA_RIGHT, 'leading': FONTE_TAMANHO_12}

DADO_PRODUTO = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_6, 'leading': FONTE_TAMANHO_8}
DADO_PRODUTO_NUMERICO = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_6, 'alignment': TA_RIGHT, 'leading': FONTE_TAMANHO_8}
DADO_PRODUTO_CENTRALIZADO = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_6, 'alignment': TA_CENTER, 'leading': FONTE_TAMANHO_8}

DADO_COMPLEMENTAR = {'fontName': FONTE_NORMAL, 'fontSize': FONTE_TAMANHO_6, 'leading': FONTE_TAMANHO_8}

DESCRITIVO_DANFE = {'fontName': FONTE_NEGRITO, 'fontSize': FONTE_TAMANHO_12, 'alignment': TA_CENTER}
DESCRITIVO_NUMERO = {'fontName': FONTE_NEGRITO, 'fontSize': FONTE_TAMANHO_10, 'alignment': TA_CENTER}

OBS_CONTINGENCIA = {'fontName': FONTE_NEGRITO, 'fontSize': FONTE_TAMANHO_18, 'alignment': TA_CENTER, 'textColor': HexColor(0xc3c3c3)}
OBS_HOMOLOGACAO = {'fontName': FONTE_NEGRITO, 'fontSize': FONTE_TAMANHO_40, 'alignment': TA_CENTER, 'textColor': HexColor(0xc3c3c3)}


class LabelMargemEsquerda(Label):
    def __init__(self):
        super(LabelMargemEsquerda, self).__init__()
        #self.borders_stroke_width = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        self.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': False}
        self.margin_top = 0.08*cm
        self.margin_left = 0.08*cm
        self.margin_bottom = 0.08*cm
        self.margin_right = 0.08*cm
        self.style = DESCRITIVO_CAMPO
        self.height = 0.70*cm

        
class LabelMargemDireita(LabelMargemEsquerda):
    def __init__(self):
        super(LabelMargemDireita, self).__init__()
        self.borders = {'top': 0.1, 'right': False, 'bottom': 0.1, 'left': 0.1}


class Campo(ObjectValue):
    def __init__(self):
        super(Campo, self).__init__()
        self.margin_top = 0.1*cm
        self.margin_left = 0.1*cm
        self.margin_bottom = 0.1*cm
        self.margin_right = 0.1*cm
        self.style = DADO_CAMPO
        self.height = 0.70*cm


class Texto(Label):
    def __init__(self):
        super(Texto, self).__init__()
        self.margin_top = 0.1*cm
        self.margin_left = 0.1*cm
        self.margin_bottom = 0.1*cm
        self.margin_right = 0.1*cm
        self.style = DADO_CAMPO
        self.height = 0.70*cm
        

class Descritivo(Label):
    def __init__(self):
        super(Descritivo, self).__init__()
        #self.borders_stroke_width = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        self.borders = {'top': 0.1, 'right': False, 'bottom': 0.1, 'left': False}
        self.margin_top = 0.08*cm
        self.margin_left = 0.1*cm
        self.margin_bottom = 0.1*cm
        self.margin_right = 0.1*cm
        self.style = DESCRITIVO_BLOCO
        self.height = 0.42*cm


class BandaDANFE(ReportBand):
    def __init__(self):
        super(BandaDANFE, self).__init__()

    def _inclui_titulo(self, nome, titulo, top, left, width, height=None, margem_direita=False):
        # Prepara o Label com o título
        if margem_direita:
            lbl = LabelMargemDireita()
        else:
            lbl = LabelMargemEsquerda()
            
        lbl.name = 'lbl_' + nome
        lbl.text = titulo
        lbl.top = top
        lbl.left = left
        lbl.width = width
        
        if height:
            lbl.height = height
            
        return lbl
        
    def _inclui_campo(self, nome, conteudo, top, left, width, height=None):
        fld = Campo()
        fld.name = 'fld_' + nome
        fld.top = top
        fld.left = left
        fld.width = width
        
        if height:
            fld.height = height
            
        return fld
        
    def _inclui_texto(self, nome, texto, top, left, width, height=None):
        lbl = Texto()
        lbl.name = 'txt_' + nome
        lbl.text = texto
        lbl.top = top
        lbl.left = left
        lbl.width = width
        
        if height:
            lbl.height = height
            
        return lbl
        
    def inclui_campo(self, nome, titulo, conteudo, top, left, width, height=None, margem_direita=False):
        lbl = self._inclui_titulo(nome, titulo, top, left, width, height, margem_direita)
        self.elements.append(lbl)
        
        fld = self._inclui_campo(nome, conteudo, top, left, width, height)
        fld.margin_top = 0.32*cm
        self.elements.append(fld)
        
        return lbl, fld
        
    def inclui_campo_numerico(self, nome, titulo, conteudo, top, left, width, height=None, margem_direita=False):
        lbl, fld = self.inclui_campo(nome, titulo, conteudo, top, left, width, height, margem_direita)
        fld.style = DADO_CAMPO_NUMERICO
        
        return lbl, fld
        
    def inclui_texto(self, nome, titulo, texto, top, left, width, height=None, margem_direita=False):
        lbl = self._inclui_titulo(nome, titulo, top, left, width, height, margem_direita)
        self.elements.append(lbl)

        if texto:
            txt = self._inclui_texto(nome, texto, top, left, width, height)
            txt.margin_top = 0.32*cm
            self.elements.append(txt)
        else:
            txt = None
        
        return lbl, txt

    def inclui_texto_numerico(self, nome, titulo, texto, top, left, width, height=None, margem_direita=False):
        lbl, txt = self.inclui_texto(nome, titulo, texto, top, left, width, height, margem_direita)
        
        if txt:
            txt.style = DADO_CAMPO_NUMERICO
        
        return lbl, txt

    def inclui_descritivo(self, nome, titulo, top, left, width, height=None):
        lbl = Descritivo()
        
        lbl.name = 'dsc_' + nome
        lbl.text = titulo
        lbl.top = top
        lbl.left = left
        lbl.width = width
        
        if height:
            lbl.height = height
            
        self.elements.append(lbl)
            
        return lbl
        
    def inclui_texto_sem_borda(self, nome, texto, top, left, width, height=None, margem_direita=False):
        txt = self._inclui_texto(nome, texto, top, left, width, height)
        txt.margin_top = 0.1*cm
        self.elements.append(txt)
        
        return txt
        
    def inclui_descritivo_produto(self, nome, titulo, top, left, width, height=None, margem_direita=False):
        lbl = self._inclui_titulo(nome, titulo, top, left, width, height, margem_direita)
        lbl.style = DESCRITIVO_PRODUTO
        lbl.margin_top = 0.05*cm
        lbl.margin_left = 0.05*cm
        lbl.margin_bottom = 0.05*cm
        lbl.margin_right = 0.05*cm
        
        if height:
            lbl.height = height
        else:
            lbl.height = 0.52*cm
            
        self.elements.append(lbl)
        return lbl
        
    def inclui_campo_produto(self, nome, conteudo, top, left, width, height=None, margem_direita=False):
        fld = self._inclui_campo(nome, conteudo, top, left, width, height, margem_direita)
        fld.borders_stroke_width = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        
        if margem_direita:
            fld.borders = {'top': 0.1, 'right': False, 'bottom': 0.1, 'left': 0.1}
        else:
            fld.borders = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': False}
            
        fld.style = DADO_PRODUTO
        fld.margin_top = 0.05*cm
        fld.margin_left = 0.05*cm
        fld.margin_bottom = 0.05*cm
        fld.margin_right = 0.05*cm
        fld.auto_expand_height = True

        if height:
            fld.height = height
        else:
            fld.height = 0.28*cm

        self.elements.append(fld)
            
        return fld

    def inclui_campo_numerico_produto(self, nome, conteudo, top, left, width, height=None, margem_direita=False):
        fld = self.inclui_campo_produto(nome, conteudo, top, left, width, height, margem_direita)
        
        fld.style = DADO_PRODUTO_NUMERICO
        
        return fld

    def inclui_campo_centralizado_produto(self, nome, conteudo, top, left, width, height=None, margem_direita=False):
        fld = self.inclui_campo_produto(nome, conteudo, top, left, width, height, margem_direita)
        
        fld.style = DADO_PRODUTO_CENTRALIZADO
        
        return fld

    def inclui_texto_produto(self, nome, texto, top, left, width, height=None, margem_direita=False):
        txt = self._inclui_texto(nome, texto, top, left, width, height)
        txt.borders_stroke_width = {'top': 0.1, 'right': 0.1, 'bottom': 0.1, 'left': 0.1}
        
        if margem_direita:
            txt.borders = {'top': True, 'right': False, 'bottom': True, 'left': True}
        else:
            txt.borders = {'top': True, 'right': True, 'bottom': True, 'left': False}
            
        txt.style = DADO_PRODUTO
        txt.margin_top = 0.05*cm
        txt.margin_left = 0.05*cm
        txt.margin_bottom = 0.05*cm
        txt.margin_right = 0.05*cm
        txt.auto_expand_height = True
        
        if height:
            txt.height = height
        else:
            txt.height = 0.28*cm
        
        self.elements.append(txt)
            
        return txt

    def inclui_texto_numerico_produto(self, nome, texto, top, left, width, height=None, margem_direita=False):
        txt = self.inclui_texto_produto(nome, texto, top, left, width, height, margem_direita)
        
        txt.style = DADO_PRODUTO_NUMERICO

        return txt

    def inclui_texto_centralizado_produto(self, nome, texto, top, left, width, height=None, margem_direita=False):
        txt = self.inclui_texto_produto(nome, texto, top, left, width, height, margem_direita)
        
        txt.style = DADO_PRODUTO_CENTRALIZADO

        return txt
