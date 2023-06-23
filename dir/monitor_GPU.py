import subprocess
import time

while True:
    # 使用nvidia-smi命令获取显卡显存使用情况
    cmd = "nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits"
    result = subprocess.check_output(cmd, shell=True).decode().strip().split('\n')

    # 解析结果
    gpu_memory_used = [int(x) for x in result]

    # 显示显卡显存使用情况
    for i, memory_used in enumerate(gpu_memory_used):
        print(f"GPU {i}: Memory Used - {memory_used} MiB")

    # 可以在这里添加判断逻辑，根据显存使用情况执行相应的操作

    # 等待一段时间后继续监控
    time.sleep(10)  # 每10秒检查一次
