import psutil
from reportlab.pdfgen import canvas

# Obter informações sobre o uso do sistema
cpu_percent = psutil.cpu_percent()
memory_percent = psutil.virtual_memory().percent
disk_percent = psutil.disk_usage('/').percent

# Gerar o relatório em PDF
pdf = canvas.Canvas('relatorio_desempenho.pdf')
pdf.drawString(100, 750, "Relatório de Desempenho do Servidor")
pdf.drawString(100, 700, f"Uso da CPU: {cpu_percent}%")
pdf.drawString(100, 680, f"Uso de Memória: {memory_percent}%")
pdf.drawString(100, 660, f"Uso do Disco: {disk_percent}%")
pdf.save()