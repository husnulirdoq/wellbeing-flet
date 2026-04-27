import flet as ft
import requests

# Sesuaikan BASE_URL dengan IP laptop lo kalo mau ditest di HP beneran
BASE_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "Wellbeing Mobile"
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- PENGATURAN ALIGNMENT AGAR CENTER ---
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Padding biar gak nempel banget ke pinggir layar HP
    page.padding = 20

    # HALAMAN LOGIN
    def login_screen():
        user_in = ft.TextField(
            label="Username",
            border_radius=10,
            width=320 # Lebar standar biar pas di layar HP
        )
        pass_in = ft.TextField(
            label="Password",
            password=True,
            border_radius=10,
            width=320
        )

        def masuk_klik(e):
            if user_in.value.lower() == "aqib" and pass_in.value == "123":
                home_screen()
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Username/Password Salah!"))
                page.snack_bar.open = True
                page.update()

        page.controls.clear()
        page.add(
            ft.Column([
                ft.Icon(ft.Icons.LOCK_PERSON_ROUNDED, size=50, color="blue"),
                ft.Text("Login Account", size=24, weight="bold"),
                ft.Text("Silakan masuk, Qib", color="grey"),
                ft.Divider(height=20, color="transparent"),
                user_in,
                pass_in,
                ft.Divider(height=10, color="transparent"),
                ft.Button(
                    "MASUK",
                    on_click=masuk_klik,
                    width=320,
                    height=50,
                    bgcolor=ft.Colors.BLUE_600,
                    color=ft.Colors.WHITE
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        page.update()

    # HALAMAN UTAMA
    def home_screen():
        page.controls.clear()

        # Biar konten gak menjorok ke atas banget, kita pake Column center
        tugas_in = ft.TextField(
            hint_text="Fokus apa hari ini?",
            expand=True,
            border_radius=10
        )
        list_v = ft.ListView(expand=True, spacing=10)

        def load_data():
            try:
                res = requests.get(f"{BASE_URL}/tasks", timeout=2).json()
                list_v.controls.clear()
                for i, text in enumerate(res):
                    def hapus(e, idx=i):
                        requests.delete(f"{BASE_URL}/tasks/{idx}")
                        load_data()

                    list_v.controls.append(
                        ft.Container(
                            content=ft.ListTile(
                                title=ft.Text(text),
                                trailing=ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    icon_color="red",
                                    on_click=hapus
                                )
                            ),
                            bgcolor="#f0f2f5",
                            border_radius=10
                        )
                    )
                page.update()
            except:
                pass

        def tambah(e):
            if tugas_in.value:
                requests.post(f"{BASE_URL}/tasks", json={"content": tugas_in.value})
                tugas_in.value = ""
                load_data()

        # UI UTAMA dibungkus Container dengan maxWidth biar rapi
        main_container = ft.Container(
            width=350, # Ukuran HP standar
            height=650, # Tinggi HP standar
            content=ft.Column([
                ft.Row([
                    ft.Text("Wellbeing", size=22, weight="bold"),
                    ft.IconButton(
                        icon=ft.Icons.LOGOUT_ROUNDED,
                        on_click=lambda _: login_screen()
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                ft.Row([
                    tugas_in,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=tambah,
                        mini=True # Ukuran kecil biar pas di Row
                    )
                ]),
                ft.Divider(),
                list_v
            ], expand=True)
        )

        page.add(main_container)
        load_data()

    login_screen()

if __name__ == "__main__":
    # Karena lo running lewat Android Studio, ft.run atau ft.app bakal otomatis detect
    ft.run(main)