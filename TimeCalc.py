import customtkinter as ctk
from tkinter import messagebox
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class TimeCalcApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TimeCalc Pro")
        self.geometry("620x450")
        
        self.total_seconds = 0
        # List to store history of total_seconds for Undo
        self.history_stack = []

        # Layout Configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- LEFT PANEL: Calculator ---
        self.control_frame = ctk.CTkFrame(self, corner_radius=0)
        self.control_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.label_title = ctk.CTkLabel(self.control_frame, text="RUNNING TOTAL", font=ctk.CTkFont(size=12, weight="bold"))
        self.label_title.pack(pady=(20, 5))

        self.display = ctk.CTkLabel(self.control_frame, text="0:00", font=ctk.CTkFont(size=48, weight="bold"))
        self.display.pack(pady=(0, 20))

        self.entry = ctk.CTkEntry(self.control_frame, placeholder_text="M.SS (+/- or Enter)", width=180, justify="center")
        self.entry.pack(pady=10)
        
        # BINDINGS
        self.entry.bind("<KeyRelease>", self.check_for_operator)
        self.entry.bind("<Return>", lambda e: self.add_time())
        self.entry.bind("<KP_Enter>", lambda e: self.add_time())
        # Command+Z for macOS, Control+Z for others
        self.bind("<Command-z>", lambda e: self.undo())
        self.bind("<Control-z>", lambda e: self.undo())

        self.add_btn = ctk.CTkButton(self.control_frame, text="Add (+)", command=self.add_time)
        self.add_btn.pack(pady=5)

        self.sub_btn = ctk.CTkButton(self.control_frame, text="Subtract (-)", command=self.sub_time, fg_color="transparent", border_width=2)
        self.sub_btn.pack(pady=5)

        self.undo_btn = ctk.CTkButton(self.control_frame, text="Undo (⌘Z)", command=self.undo, fg_color="#555555")
        self.undo_btn.pack(pady=5)

        self.reset_btn = ctk.CTkButton(self.control_frame, text="Reset", command=self.reset, fg_color="#ae3c33", hover_color="#8a2f29")
        self.reset_btn.pack(side="bottom", pady=20)

        # --- RIGHT PANEL: Session Log ---
        self.log_frame = ctk.CTkFrame(self)
        self.log_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 20), pady=20)
        
        self.log_label = ctk.CTkLabel(self.log_frame, text="SESSION LOG", font=ctk.CTkFont(size=12, weight="bold"))
        self.log_label.pack(pady=10)

        self.history_box = ctk.CTkScrollableFrame(self.log_frame, label_text="History")
        self.history_box.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.entry.focus_set()

    def format_time(self, seconds):
        is_neg = seconds < 0
        abs_secs = abs(seconds)
        return f"{'-' if is_neg else ''}{abs_secs // 60}:{abs_secs % 60:02d}"

    def check_for_operator(self, event):
        text = self.entry.get()
        if not text: return
        if text.endswith('+'): self.add_time()
        elif text.endswith('-'): self.sub_time()

    def parse_input(self, text=None):
        raw_val = text if text is not None else self.entry.get().strip()
        if not raw_val: return None
        clean_val = raw_val.rstrip('+-')
        try:
            if "." in clean_val:
                parts = clean_val.split('.')
                mins = int(parts[0]) if parts[0] else 0
                secs = int(parts[1]) if len(parts) > 1 and parts[1] else 0
            else:
                mins, secs = int(clean_val), 0
            return (mins * 60) + secs
        except ValueError:
            return None

    def add_to_log(self, op, val_secs):
        time_str = self.format_time(val_secs)
        total_str = self.format_time(self.total_seconds)
        log_entry = ctk.CTkLabel(self.history_box, text=f"{op} {time_str}  ➔  Total: {total_str}", font=ctk.CTkFont(size=11))
        log_entry.pack(anchor="w", padx=5)
        self.history_box._parent_canvas.yview_moveto(1.0)

    def add_time(self):
        val = self.parse_input()
        if val is not None:
            # Store current state for undo before modifying
            self.history_stack.append(self.total_seconds)
            self.total_seconds += val
            self.display.configure(text=self.format_time(self.total_seconds))
            self.add_to_log("+", val)
            self.entry.delete(0, 'end')

    def sub_time(self):
        val = self.parse_input()
        if val is not None:
            self.history_stack.append(self.total_seconds)
            self.total_seconds -= val
            self.display.configure(text=self.format_time(self.total_seconds))
            self.add_to_log("-", val)
            self.entry.delete(0, 'end')

    def undo(self):
        """Reverts to the last state in the history stack."""
        if self.history_stack:
            self.total_seconds = self.history_stack.pop()
            self.display.configure(text=self.format_time(self.total_seconds))
            
            # Remove the last log entry from the scrollable frame
            log_widgets = self.history_box.winfo_children()
            if log_widgets:
                log_widgets[-1].destroy()
        else:
            messagebox.showinfo("Undo", "No more actions to undo.")

    def reset(self):
        if messagebox.askyesno("Reset", "Clear current total and history?"):
            self.total_seconds = 0
            self.history_stack = []
            self.display.configure(text="0:00")
            for widget in self.history_box.winfo_children():
                widget.destroy()
            self.entry.focus_set()

if __name__ == "__main__":
    app = TimeCalcApp()
    app.mainloop()