import psutil
import platform
import subprocess
import pandas as pd
import time
from datetime import datetime

# Define o fator de conversão para converter bytes para MB, GB, etc.
MB = 1024 * 1024
GB = MB * 1024

# Coleta informações sobre o sistema
system_info = {
    'cpu_count': psutil.cpu_count(logical=False),
    'cpu_freq': psutil.cpu_freq().current,
    'ram_total': psutil.virtual_memory().total // MB,
    'ram_available': psutil.virtual_memory().available // MB,
    'ram_used': psutil.virtual_memory().used // MB,
    'swap_total': psutil.swap_memory().total // MB,
    'swap_used': psutil.swap_memory().used // MB
}

# Cria um DataFrame vazio para armazenar as informações do sistema
df_system = pd.DataFrame(system_info, index=[0])

# Define o intervalo de tempo em segundos entre cada coleta de informação
interval = 1

# Define a duração em segundos do monitoramento
duration = 60

# Inicia o monitoramento do sistema
for i in range(int(duration/interval)):
    # Coleta as informações do sistema
    cpu_percent = psutil.cpu_percent(percpu=True)
    cpu_freq = [psutil.cpu_freq().current] * len(cpu_percent)
    ram_usage = psutil.virtual_memory().used // MB
    swap_usage = psutil.swap_memory().used // MB
    disk_usage = psutil.disk_usage('/').used // GB
    
    # Converte o tempo para um formato mais legível
    now = datetime.fromtimestamp(time.time())

    # Adiciona as informações coletadas ao DataFrame
    df_monitoring = pd.DataFrame({
        'time': [now],
        'cpu_percent': cpu_percent,
        'cpu_freq': cpu_freq,
        'ram_usage': [ram_usage],
        'swap_usage': [swap_usage],
        'disk_usage': [disk_usage]
    })

    df_system = pd.concat([df_system, df_monitoring], ignore_index=True)

    # Espera o intervalo de tempo definido antes de coletar novamente as informações
    time.sleep(interval)

# Salva as informações coletadas em um arquivo CSV e Excel
df_system.to_csv('system_monitoring.csv', index=False)
df_system.to_excel('system_monitoring.xlsx', index=False)