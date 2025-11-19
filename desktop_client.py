import json
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from urllib import request, error

API_URL = "http://127.0.0.1:5000/api/ai-assistant"


def append_message(text_widget, prefix, message):
    text_widget.configure(state="normal")
    text_widget.insert(tk.END, f"{prefix}: {message}\n")
    text_widget.see(tk.END)
    text_widget.configure(state="disabled")


def send_message(entry, text_widget):
    msg = entry.get().strip()
    if not msg:
        return

    append_message(text_widget, "You", msg)
    entry.delete(0, tk.END)

    payload = json.dumps({"message": msg}).encode("utf-8")
    req = request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode("utf-8")
            data = json.loads(body)
            reply = data.get("reply") or "(no reply)"
    except Exception as exc:  # noqa: BLE001
        reply = (
            "Could not reach the VPN AI server. "
            "Make sure app.py is running on http://127.0.0.1:5000.\n"
            f"Details: {exc}"
        )

    append_message(text_widget, "AI", reply)


def main():
    root = tk.Tk()
    root.title("VPN FOR SERVER FREE CLOUD ACCESS - Desktop AI Assistant")
    root.geometry("640x420")

    chat_box = ScrolledText(root, wrap=tk.WORD)
    chat_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
    chat_box.configure(state="disabled")

    entry_frame = tk.Frame(root)
    entry_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

    entry = tk.Entry(entry_frame)
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))

    send_btn = tk.Button(
        entry_frame,
        text="Send",
        command=lambda: send_message(entry, chat_box),
    )
    send_btn.pack(side=tk.RIGHT)

    append_message(
        chat_box,
        "AI",
        "Hi! I am the VPNCLOUD desktop assistant. Ask me anything about secure, free cloud VPN access.",
    )

    def on_enter(event):  # noqa: D401, ARG001
        """Handle Enter key press to send the message."""

        send_message(entry, chat_box)

    entry.bind("<Return>", on_enter)

    root.mainloop()


if __name__ == "__main__":
    main()
