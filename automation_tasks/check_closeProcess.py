import psutil
import os
import signal

# Informações sobre a memória
mem = psutil.virtual_memory()

print(f"Memória RAM disponível: {mem.available / 1024 / 1024:.2f} MB")
print(f"Memória RAM usada: {mem.used / 1024 / 1024:.2f} MB")

# Lista de processos que consomem muita memória (acima de 100 MB)
processes = []
for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
    try:
        mem_info = proc.memory_info()
        if mem_info.rss > 100 * 1024 * 1024: # Convertendo para bytes
            processes.append((proc.pid, proc.name(), mem_info.rss))
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if processes:
    print("\nProcessos que consomem muita memória:")
    for proc in processes:
        print(f"PID: {proc[0]}, Nome: {proc[1]}, Consumo de memória: {proc[2] / 1024 / 1024:.2f} MB")
    
    # Encerrando processos que consomem muita memória
    while True:
        resposta = input("Deseja encerrar algum processo? (s/n) ")
        if resposta.lower() == 'n':
            break
        elif resposta.lower() == 's':
            pid = input("Informe o PID do processo que deseja encerrar: ")
            try:
                pid = int(pid)
                os.kill(pid, signal.SIGTERM)
                print(f"Processo {pid} encerrado com sucesso!")
            except ValueError:
                print("PID inválido!")
            except os.error:
                print("Erro ao encerrar o processo!")
        else:
            print("Opção inválida!")
else:
    print("Não há processos que consomem muita memória.")