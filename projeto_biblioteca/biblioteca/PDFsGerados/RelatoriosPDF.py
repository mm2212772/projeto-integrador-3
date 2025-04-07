from datetime import date, datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer, Table,
                                TableStyle)


class Relatorio():
    def __init__(self, dados, nome_relatorio):
        self._dados = dados
        self._nome_relatorio = nome_relatorio
        
    def Gerar(self, response):
        data_e_hora = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        response['Content-Disposition'] = f'attachment; filename="{self._nome_relatorio}-{data_e_hora}.pdf"'
        self._pdf = SimpleDocTemplate(response, pagesize=A4, leftMargin=20, rightMargin=20, topMargin=20, bottomMargin=20)
    
    def _config_tabela(self, dados, col_width=None):
        table = Table(dados, col_width)
       
        table.setStyle(         TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cabeçalho cinza
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto branco no cabeçalho
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centraliza o texto
            ('VALIGN', (-1, -1), (-1, -1), 'MIDDLE'),  # Centraliza o texto
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Cabeçalho em negrito
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),  # Espaçamento no cabeçalho
            ('TOPPADDING', (0, 0), (-1, 0), 6),  # Espaçamento no cabeçalho
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Fundo branco para os dados
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grade preta
        ]))
        return table
        
    def _titulo_pdf(self, titulo):
        styles = getSampleStyleSheet()
        titulo_style = styles['Title']
        data_atual = date.today().strftime("%d/%m/%Y")
        return Paragraph(f"{titulo} - {data_atual}", titulo_style)
        
        



class RelatorioDevedores(Relatorio):           
    def Gerar(self, response):        
        super().Gerar(response)       
        emprestimos = self._dados    

        styles = getSampleStyleSheet()
        estilo_normal = styles["Normal"]

        # Estilo para os títulos da tabela (centralizado)
        estilo_titulo_coluna = ParagraphStyle(
            name="TituloColuna",
            parent=styles["Normal"],
            alignment=1,  # 0 = esquerda, 1 = centro, 2 = direita
            fontSize=10,
            spaceAfter=4,
            spaceBefore=4,
            textColor=colors.whitesmoke,
        )

        # Cabeçalhos com Paragraph centralizado
        dados = [[
            Paragraph("Leitor", estilo_titulo_coluna),
            Paragraph("Exemplar", estilo_titulo_coluna),
            Paragraph("Data de Empréstimo", estilo_titulo_coluna),
            Paragraph("Data de Devolução", estilo_titulo_coluna),
            Paragraph("Dias de Atraso", estilo_titulo_coluna),
        ]]
        
        titulo = self._titulo_pdf("Relatório de Devedores")
        
        # Preenchendo os dados
        for emprestimo in emprestimos:
            dias_atraso = (date.today() - emprestimo.data_devolucao).days
            dados.append([
                Paragraph(emprestimo.leitor.nome, estilo_normal),
                Paragraph(emprestimo.exemplar.livro.titulo, estilo_normal),
                emprestimo.data_emprestimo.strftime("%d/%m/%Y"),
                emprestimo.data_devolucao.strftime("%d/%m/%Y"),
                str(dias_atraso),
            ])
        
        # Aumentando as colunas de datas e atraso
        col_widths = [120, 150, 110, 110, 90]
        
        table = Table(dados, colWidths=col_widths)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 1), (-1, -1), "LEFT"),  # Dados normais à esquerda
            ("ALIGN", (2, 1), (4, -1), "CENTER"), # Datas e atraso centralizados
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elementos = [titulo, Spacer(1, 10), table]
        self._pdf.build(elementos)

        
class RelatorioLeitores(Relatorio):
    def Gerar(self, response):
        super().Gerar(response)       
        leitores = self._dados    
        # Cabeçalho da tabela
        dados = [["Leitor", "Quantidade de Empréstimos"]]
        titulo = self._titulo_pdf("Relatório de Empréstimos por Leitor")
        
        # Preenchendo os dados
        for leitor in leitores:            
            dados.append([
                leitor.nome,
                leitor.quantidade_emprestada,                               
            ])
        col_widths = [530 / len(dados[0])] * len(dados[0])   
        table = self._config_tabela(dados, col_widths)       
        elementos =[titulo, Spacer(1,10), table]
        self._pdf.build(elementos)
        

class RelatorioEmprestimosMensal(Relatorio):
    def Gerar(self, response, mes, ano):
        super().Gerar(response)       
        emprestimos = self._dados    

        styles = getSampleStyleSheet()
        estilo_normal = styles["Normal"]

        # Estilo para o cabeçalho centralizado
        estilo_titulo_coluna = ParagraphStyle(
            name="TituloColuna",
            parent=styles["Normal"],
            alignment=1,  # 0 = esquerda, 1 = centro, 2 = direita
            fontSize=10,
            spaceAfter=4,
            spaceBefore=4,
            textColor=colors.whitesmoke,
        )

        # Cabeçalho da tabela com Paragraphs centralizados
        dados = [[
            Paragraph("Leitor", estilo_titulo_coluna),
            Paragraph("Exemplar", estilo_titulo_coluna),
            Paragraph("Data de Devolução", estilo_titulo_coluna),
            Paragraph("Devolvido", estilo_titulo_coluna),
        ]]

        mes = mes.rjust(2, "0")
        titulo = self._titulo_pdf(f"Relatório de Empréstimos de {mes}/{ano}")
        
        valor_quantidade = len(emprestimos)
        estilo_qtd = styles["Normal"]
        estilo_qtd.fontSize = 12
        quantidade = Paragraph(f"<b>Total de empréstimos:</b> {valor_quantidade}.", estilo_qtd)

        # Preenchendo os dados
        for emprestimo in emprestimos:            
            obra = f"(ID: {emprestimo.exemplar.id}) {emprestimo.exemplar.livro.titulo}"
            data = emprestimo.data_devolucao.strftime('%d/%m/%Y')
            devolvido = "Sim" if emprestimo.devolvido else "Não"
            dados.append([
                Paragraph(emprestimo.leitor.nome, estilo_normal),
                Paragraph(obra, estilo_normal),                
                data,
                devolvido,                            
            ])        

        # Definindo larguras das colunas
        col_widths = [120, 200, 100, 70]

        table = Table(dados, colWidths=col_widths)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 1), (-2, -1), "LEFT"),
            ("ALIGN", (-2, 1), (-1, -1), "CENTER"),  # Alinha 'Data' e 'Devolvido' ao centro
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elementos = [titulo, Spacer(1, 10), quantidade, Spacer(1, 15), table]
        self._pdf.build(elementos)

        
class RelatorioEmprestimosAnual(Relatorio):
    def Gerar(self, response, ano):
        super().Gerar(response)       
        emprestimos = self._dados    

        styles = getSampleStyleSheet()
        estilo_normal = styles["Normal"]

        # Estilo do cabeçalho da tabela centralizado
        estilo_titulo_coluna = ParagraphStyle(
            name="TituloColuna",
            parent=styles["Normal"],
            alignment=1,
            fontSize=10,
            spaceAfter=4,
            spaceBefore=4,
            textColor=colors.whitesmoke,
        )

        # Cabeçalho da tabela
        dados = [[
            Paragraph("Leitor", estilo_titulo_coluna),
            Paragraph("Exemplar", estilo_titulo_coluna),
            Paragraph("Data de Devolução", estilo_titulo_coluna),
            Paragraph("Devolvido", estilo_titulo_coluna),
        ]]

        titulo = self._titulo_pdf(f"Relatório de Empréstimos de {ano}")

        estilo_qtd = styles["Normal"]
        estilo_qtd.fontSize = 12
        valor_quantidade = len(emprestimos)
        quantidade = Paragraph(f"<b>Total de empréstimos:</b> {valor_quantidade}.", estilo_qtd)

        # Preenchendo os dados
        for emprestimo in emprestimos:            
            obra_html = f"(ID: {emprestimo.exemplar.id}) {emprestimo.exemplar.livro.titulo}"
            data = emprestimo.data_devolucao.strftime('%d/%m/%Y')
            devolvido = "Sim" if emprestimo.devolvido else "Não"
            dados.append([
                Paragraph(emprestimo.leitor.nome, estilo_normal),
                Paragraph(obra_html, estilo_normal),                
                data,
                devolvido,                            
            ])

        # Larguras das colunas ajustadas
        col_widths = [120, 200, 100, 70]

        table = Table(dados, colWidths=col_widths)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 1), (-2, -1), "LEFT"),
            ("ALIGN", (-2, 1), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elementos = [titulo, Spacer(1, 10), quantidade, Spacer(1, 15), table]
        self._pdf.build(elementos)