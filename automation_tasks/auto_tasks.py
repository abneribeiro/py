from fpdf import FPDF


class PDF(FPDF):
    def section_header(self, title):
        # Define as cores de fundo e de texto da seção
        self.set_fill_color(50, 50, 50)
        self.set_text_color(255, 255, 255)

        # Adiciona o título da seção
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 1, 1, 'L', 1)

        # Define as cores de fundo e de texto do conteúdo da seção
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)

    def section_content(self, content):
        # Adiciona o conteúdo da seção
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 7, content, 0, 1)

# Pede as informações do candidato
nome_completo = input('Digite seu nome completo: ')
telefone = input('Digite seu telefone: ')
objetivo = input('Digite seu objetivo profissional: ')

# Cria o PDF
pdf = PDF()

# Define as cores do documento
pdf.set_fill_color(50, 50, 50)
pdf.set_text_color(255, 255, 255)

# Adiciona uma nova página
pdf.add_page()

# Adiciona o cabeçalho
pdf.set_font('Arial', 'B', 20)
pdf.cell(0, 10, nome_completo, 1, 1, 'C', 1)
pdf.ln(5)

# Adiciona informações de contato
pdf.section_header('Informações de Contato')
pdf.set_font('Arial', '', 12)
pdf.cell(0, 7, telefone, 0, 1)
pdf.ln(10)

# Adiciona objetivo profissional
pdf.section_header('Objetivo Profissional')
pdf.section_content(objetivo)
pdf.ln(10)

# Salva o PDF
pdf.output('curriculum_vitae.pdf', 'F')





