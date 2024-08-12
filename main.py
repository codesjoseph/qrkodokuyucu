import tkinter as tk
from tkinter import colorchooser, messagebox, filedialog
import qrcode
import qrcode.constants
from PIL import ImageTk, Image

def choose_fill_color():
    color_code = colorchooser.askcolor(title="QR Kod Doldurma Rengi Seçin")
    if color_code[1]: 
        global fill_color
        fill_color = color_code[1]
        fill_color_label.config(bg=fill_color)

def choose_back_color():
    color_code = colorchooser.askcolor(title="QR Kod Arka Plan Rengi Seçin")
    if color_code[1]:  
        global back_color
        back_color = color_code[1]
        back_color_label.config(bg=back_color)

def generate_qr_code():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Hata", "URL boş olamaz!")
        return

    # QR kod oluşturma
    code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    code.add_data(url)
    code.make(fit=True)

    img = code.make_image(fill_color=fill_color, back_color=back_color)

    # QR kodunu kaydetme
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Başarılı", f"QR kod başarıyla '{file_path}' konumuna kaydedildi!")

        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)

        panel.config(image=img)
        panel.image = img 

# Varsayılan renkler
fill_color = "red"
back_color = "black"

# Pencereyi oluştur
window = tk.Tk()
window.title("QR Kod Oluşturucu")
window.geometry("600x700")
window.resizable(False, False)

# URL girişi
tk.Label(window, text="URL:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
url_entry = tk.Entry(window, width=40, font=("Arial", 10))
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Renk seçme butonları ve gösterim alanları
fill_color_button = tk.Button(window, text="Doldurma Rengini Seç", command=choose_fill_color, font=("Arial", 10))
fill_color_button.grid(row=1, column=0, padx=10, pady=10)

fill_color_label = tk.Label(window, bg=fill_color, width=3, height=1)
fill_color_label.grid(row=1, column=1, sticky="w")

back_color_button = tk.Button(window, text="Arka Plan Rengini Seç", command=choose_back_color,  font=("Arial", 10))
back_color_button.grid(row=2, column=0, padx=10, pady=10)

back_color_label = tk.Label(window, bg=back_color, width=3, height=1)
back_color_label.grid(row=2, column=1, sticky="w")

# QR kod oluşturma butonu
generate_button = tk.Button(window, text="QR Kod Oluştur", command=generate_qr_code, bg="green", fg="white", font=("Arial", 12))
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

# QR kod görüntüleme alanı
panel = tk.Label(window)
panel.grid(row=4, column=0, columnspan=2)

window.mainloop()
