# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#

from __future__ import division, print_function, unicode_literals

from pysped.xml_sped import (ABERTURA, TagInteiro, TagCaracter, XMLNFe,
                             _Alerta, _Erro, )
from pysped.nfse.versao_100 import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)


class _Cabecalho(XMLNFe):

    def __init__(self):
        super(_Cabecalho, self).__init__()
        self.CodCid           = TagInteiro(nome='CodCid'           , tamanho=[ 1, 10, 1], raiz='//nfse:RetornoConsultaSeqRps/Cabecalho')
        self.CPFCNPJRemetente = TagCaracter(nome='CPFCNPJRemetente', tamanho=[11, 14]   , raiz='//nfse:RetornoConsultaSeqRps/Cabecalho')
        self.IMPrestador      = TagCaracter(nome='IMPrestador'     , tamanho=[ 6, 11]   , raiz='//nfse:RetornoConsultaSeqRps/Cabecalho')
        self.NroUltimoRps     = TagInteiro(nome='NroUltimoRps'     , tamanho=[ 1, 12, 1], raiz='//nfse:RetornoConsultaSeqRps/Cabecalho')
        self.SeriePrestacao   = TagCaracter(nome='SeriePrestacao'  , tamanho=[ 2, 2]   , raiz='//nfse:RetornoConsultaSeqRps/Cabecalho', valor='99', obrigatorio=False)
        self.Versao           = TagInteiro(nome='Versao'           , tamanho=[ 1, 3, 1], raiz='//nfse:RetornoConsultaSeqRps/Cabecalho', valor=1)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<Cabecalho>'
        xml += self.CodCid.xml
        xml += self.CPFCNPJRemetente.xml
        xml += self.IMPrestador.xml
        xml += self.NroUltimoRps.xml
        xml += self.SeriePrestacao.xml
        xml += self.Versao.xml
        xml += '</Cabecalho>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CodCid.xml           = arquivo
            self.CPFCNPJRemetente.xml = arquivo
            self.IMPrestador.xml      = arquivo
            self.NroUltimoRps.xml     = arquivo
            self.SeriePrestacao.xml   = arquivo
            self.Versao.xml           = arquivo

    xml = property(get_xml, set_xml)


class RetornoConsultaSeqRPS(XMLNFe):

    def __init__(self):
        super(RetornoConsultaSeqRPS, self).__init__()
        self.caminho_esquema  = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema  = 'RetornoConsultaSeqRps.xsd'
        self.Cabecalho = _Cabecalho()
        self.Alertas   = []
        self.Erros     = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += '<nfse:RetornoConsultaSeqRps xmlns:nfse="http://localhost:8080/WsNFe2/lote" xmlns:tipos="http://localhost:8080/WsNFe2/tp" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://localhost:8080/WsNFe2/lote http://localhost:8080/WsNFe2/xsd/RetornoConsultaSeqRps.xsd">'
        xml += self.Cabecalho.xml

        if len(self.Alertas):
            xml += '<Alertas>'

            for a in self.Alertas:
                xml += a.xml

            xml += '</Alertas>'

        if len(self.Erros):
            xml += '<Erros>'

            for e in self.Erros:
                xml += e.xml

            xml += '</Erros>'

        xml += '</nfse:RetornoConsultaSeqRps>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Cabecalho.xml = arquivo

            alertas = self._le_nohs('//nfse:RetornoConsultaSeqRps/Alertas/Alerta')
            self.Alertas = []
            if alertas is not None:
                self.Alertas = [_Alerta() for a in alertas]
                for i in range(len(alertas)):
                    self.Alertas[i].xml = alertas[i]

            erros = self._le_nohs('//nfse:RetornoConsultaSeqRps/Erros/Erro')
            self.Erros = []
            if erros is not None:
                self.Erros = [_Erro() for e in erros]
                for i in range(len(erros)):
                    self.Erros[i].xml = erros[i]

    xml = property(get_xml, set_xml)
