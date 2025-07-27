import requests
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
import sys

console = Console()

def show_banner():
    banner_text = """
████████╗██╗   ██╗ █████╗ ███╗   ██╗ █████╗ ███╗   ██╗██╗  ██╗
╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔══██╗████╗  ██║██║ ██╔╝
   ██║   ██║   ██║███████║██╔██╗ ██║███████║██╔██╗ ██║█████╔╝ 
   ██║   ██║   ██║██╔══██║██║╚██╗██║██╔══██║██║╚██╗██║██╔═██╗ 
   ██║   ╚██████╔╝██║  ██║██║ ╚████║██║  ██║██║ ╚████║██║  ██╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
    """
    console.print(Panel(banner_text, title="[bold green]TOOL MENU BY TUAN ANH[/bold green]", border_style="blue", subtitle="Zalo: 0878933844"))

def show_menu():
    table = Table(title="[bold yellow]Danh sách các tool có sẵn[/bold yellow]", box=box.SQUARE)

    table.add_column("Mã", justify="center", style="cyan", no_wrap=True)
    table.add_column("Tên Tool", justify="left", style="magenta")

    table.add_row("3.1", "Tool Đào Mail")
    table.add_row("3.2", "Tool Đào Mail Full Mail")
    table.add_row("3.3", "Tool Check Live/Die Email")
    table.add_row("3.4", "Tool Check Email Valid")
    table.add_row("3.5", "Tool Reg Acc Garena")

    table.add_row("4.1", "Check Proxy Live/Die V1")
    table.add_row("4.2", "Check Proxy Live/Die V2")
    table.add_row("4.3", "Check Proxy Live/Die V3 VIP")
    table.add_row("4.4", "Đào Proxy V1")
    table.add_row("4.5", "Đào Proxy V2")
    table.add_row("4.6", "Đào Proxy V3")
    table.add_row("4.7", "Đào Proxy V4")
    table.add_row("4.8", "Đào Proxy V5 VIP")

    table.add_row("5.2", "Tool Decode Kramer‑Specter")
    table.add_row("5.3", "Tool dump_marshal")
    table.add_row("5.4", "Tool Convert Marshal‑PYC")

    table.add_row("8", "Tool Reg Facebook")

    table.add_row("0", "[red]Thoát Tool[/red]")

    console.print(table)

def run_tool(choice: str):
    if choice == "0":
        console.print("[bold red]👉 Đã thoát tool. Tạm biệt bạn![/bold red]")
        sys.exit()

    base_url = "https://raw.githubusercontent.com/helloanhem07-2809/banner.py/main/tool/"
    tools = {
        "3.1": "dao_mail.py",
        "3.2": "dao_mail_full.py",
        "3.3": "check_email_live.py",
        "3.4": "check_email_valid.py",
        "3.5": "reg_garena.py",

        "4.1": "check_proxy_v1.py",
        "4.2": "check_proxy_v2.py",
        "4.3": "check_proxy_v3.py",
        "4.4": "dao_proxy_v1.py",
        "4.5": "dao_proxy_v2.py",
        "4.6": "dao_proxy_v3.py",
        "4.7": "dao_proxy_v4.py",
        "4.8": "dao_proxy_v5.py",

        "5.2": "kramer_deobf.py",
        "5.3": "dump_marshal.py",
        "5.4": "convert_marshal_pyc.py",

        "8": "reg_facebook.py"
    }

    if choice in tools:
        try:
            url = base_url + tools[choice]
            console.print(f"[blue]→ Đang tải:[/blue] {url}")
            code = requests.get(url).text
            exec(code, {})
        except Exception as e:
            console.print(f"[red]Lỗi khi chạy tool:[/red] {e}")
    else:
        console.print("[bold red]❌ Mã không hợp lệ. Vui lòng chọn lại.[/bold red]")

def main():
    while True:
        show_banner()
        show_menu()
        choice = console.input("[bold green]Nhập mã tool muốn chạy:[/bold green] ").strip()
        run_tool(choice)
        input("\n[bold yellow]Nhấn Enter để quay lại menu...[/bold yellow]")
        console.clear()

if __name__ == "__main__":
    main()
    
