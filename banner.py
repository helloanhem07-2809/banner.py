import os
import time
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel

console = Console()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner_text = r"""
████████╗██╗   ██╗ █████╗ ███╗   ██╗     █████╗ ███╗   ██╗██╗  ██╗
╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██╔══██╗████╗  ██║██║ ██╔╝
   ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██╔██╗ ██║█████╔╝ 
   ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║╚██╗██║██╔═██╗ 
   ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║██║ ╚████║██║  ██╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""
    console.print(Colorate.Horizontal(Colors.red_to_blue, banner_text, 2))

def menu():
    banner()
    console.print(Panel.fit("[bold cyan]MENU TOOL - CODE BY TUAN ANH[/bold cyan]", border_style="blue"))

    console.print("""
[bold yellow][3][/bold yellow] Tool Đào Mail
  [3.1] TOOL ĐÀO MAIL
  [3.2] TOOL ĐÀO MAIL FULL MAIL
  [3.3] TOOL CHECK LIVE/DIE
  [3.4] TOOL CHECK VALID
  [3.5] TOOL REG ACC GARENA

[bold yellow][4][/bold yellow] Tool Đào & Check Proxies
  [4.1] TOOL CHECK LIVE/DIE [V1]
  [4.2] TOOL CHECK LIVE/DIE [V2]
  [4.3] TOOL CHECK LIVE/DIE [V3 VIP]
  [4.4] TOOL ĐÀO PROXY [V1]
  [4.5] TOOL ĐÀO PROXY [V2]
  [4.6] TOOL ĐÀO PROXY [V3]
  [4.7] TOOL ĐÀO PROXY [V4]
  [4.8] TOOL ĐÀO PROXY [V5 VIP]

[bold yellow][5][/bold yellow] Tool Encode & Decode
  [5.2] TOOL DEC Kramer-Specter_Deobf
  [5.3] TOOL dump_marshal
  [5.4] TOOL Convert_Marshal-PYC

[bold yellow][8][/bold yellow] TOOL Reg ACC Facebook
""", style="bold white")

    chon = input(Colorate.Horizontal(Colors.blue_to_purple, "\n[?] Nhập số để chọn tool: ", 2))

    if chon == "3.1":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Mail_1.py").text)
    elif chon == "3.2":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Mail_2.py").text)
    elif chon == "3.3":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Mail_3.py").text)
    elif chon == "3.4":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Mail_4.py").text)
    elif chon == "3.5":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Reg_Garena.py").text)

    elif chon == "4.1":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Check_Proxy_V1.py").text)
    elif chon == "4.2":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Check_Proxy_V2.py").text)
    elif chon == "4.3":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Check_Proxy_V3.py").text)
    elif chon == "4.4":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Get_Proxy_V1.py").text)
    elif chon == "4.5":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Get_Proxy_V2.py").text)
    elif chon == "4.6":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Get_Proxy_V3.py").text)
    elif chon == "4.7":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Get_Proxy_V4.py").text)
    elif chon == "4.8":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Get_Proxy_V5.py").text)

    elif chon == "5.2":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Kramer-Specter_Deobf.py").text)
    elif chon == "5.3":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/dump_marshal.py").text)
    elif chon == "5.4":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Convert_Marshal-PYC.py").text)

    elif chon == "8":
        exec(requests.get("https://raw.githubusercontent.com/Khanh23047/Tool/main/Reg_Facebook.py").text)
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, "[!] Không hợp lệ, thử lại...", 2))
        time.sleep(2)
        menu()

menu()
