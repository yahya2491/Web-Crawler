import requests
from bs4 import BeautifulSoup
import whois
import tkinter as tk
from tkinter import scrolledtext


def scan_website():
    url = url_entry.get()
    output_text.delete(1.0, tk.END)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "N/A"

        output_text.insert(tk.END, f"Website Title: {title}\n\n")
        output_text.insert(tk.END, "Website Headers:\n")
        for header, value in response.headers.items():
            output_text.insert(tk.END, f"{header}: {value}\n")

        whois_info = whois.whois(url)
        output_text.insert(tk.END, "\nWebsite WHOIS Information:\n")
        output_text.insert(tk.END, f"Registrar: {whois_info.registrar}\n")
        output_text.insert(tk.END, f"Creation Date: {whois_info.creation_date}\n")
        output_text.insert(tk.END, f"Expiration Date: {whois_info.expiration_date}\n")
        output_text.insert(tk.END, f"Name Servers: {whois_info.name_servers}\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")


# Create GUI window
root = tk.Tk()
root.title("Website Scanner")

# Input field
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Scan button
scan_button = tk.Button(root, text="Scan", command=scan_website)
scan_button.pack()

# Output text area
output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack()

root.mainloop()
