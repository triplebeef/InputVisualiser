   

import tkinter as tk
from pynput import keyboard, mouse
import threading
import time
import sys
import os
import ctypes

               

languages = {
    "EN": {
        "key": "Key", "combo": "Combo", "click": "Click", "scroll": "Scroll",
        "left": "Left", "right": "Right", "middle": "Middle",
        "up": "Up", "down": "Down",
        "special": {
            "space": "Space", "enter": "Enter", "backspace": "Bksp",
            "tab": "Tab", "esc": "Esc", "shift": "Shift", "ctrl": "Ctrl",
            "alt": "Alt", "cmd": "Win", "up_arrow": "Up", "down_arrow": "Down",
            "left_arrow": "Left", "right_arrow": "Right", "delete": "Del",
            "home": "Home", "end": "End", "page_up": "PgUp", "page_down": "PgDn",
            "caps_lock": "Caps",
            **{f"f{i}": f"F{i}" for i in range(1, 13)},
        },
    },
    "ES": {
        "key": "Tecla", "combo": "Combo", "click": "Clic", "scroll": "Despl",
        "left": "Izq", "right": "Der", "middle": "Centro",
        "up": "Arriba", "down": "Abajo",
        "special": {
            "space": "Espacio", "enter": "Intro", "backspace": "Borrar",
            "tab": "Tab", "esc": "Esc", "shift": "Shift", "ctrl": "Ctrl",
            "alt": "Alt", "cmd": "Win", "up_arrow": "Arriba", "down_arrow": "Abajo",
            "left_arrow": "Izq", "right_arrow": "Der", "delete": "Supr",
            "home": "Inicio", "end": "Fin", "page_up": "RePag", "page_down": "AvPag",
            "caps_lock": "Bloq",
            **{f"f{i}": f"F{i}" for i in range(1, 13)},
        },
    },
    "FR": {
        "key": "Touche", "combo": "Combo", "click": "Clic", "scroll": "Déf",
        "left": "Gauche", "right": "Droite", "middle": "Milieu",
        "up": "Haut", "down": "Bas",
        "special": {
            "space": "Espace", "enter": "Entrée", "backspace": "Effacer",
            "tab": "Tab", "esc": "Échap", "shift": "Maj", "ctrl": "Ctrl",
            "alt": "Alt", "cmd": "Win", "up_arrow": "Haut", "down_arrow": "Bas",
            "left_arrow": "Gauche", "right_arrow": "Droite", "delete": "Suppr",
            "home": "Début", "end": "Fin", "page_up": "PgPréc", "page_down": "PgSuiv",
            "caps_lock": "Verr",
            **{f"f{i}": f"F{i}" for i in range(1, 13)},
        },
    },
    "DE": {
        "key": "Taste", "combo": "Kombo", "click": "Klick", "scroll": "Scroll",
        "left": "Links", "right": "Rechts", "middle": "Mitte",
        "up": "Hoch", "down": "Runter",
        "special": {
            "space": "Leertaste", "enter": "Eingabe", "backspace": "Löschen",
            "tab": "Tab", "esc": "Esc", "shift": "Umschalt", "ctrl": "Strg",
            "alt": "Alt", "cmd": "Win", "up_arrow": "Hoch", "down_arrow": "Runter",
            "left_arrow": "Links", "right_arrow": "Rechts", "delete": "Entf",
            "home": "Pos1", "end": "Ende", "page_up": "BildHoch", "page_down": "BildRunter",
            "caps_lock": "Feststell",
            **{f"f{i}": f"F{i}" for i in range(1, 13)},
        },
    },
    "JA": {
        "key": "キー", "combo": "コンボ", "click": "クリック", "scroll": "スクロール",
        "left": "左", "right": "右", "middle": "中",
        "up": "上", "down": "下",
        "special": {
            "space": "スペース", "enter": "エンター", "backspace": "削除",
            "tab": "タブ", "esc": "ESC", "shift": "シフト", "ctrl": "CTRL",
            "alt": "ALT", "cmd": "Win", "up_arrow": "上", "down_arrow": "下",
            "left_arrow": "左", "right_arrow": "右", "delete": "デリート",
            "home": "ホーム", "end": "エンド", "page_up": "PgUp", "page_down": "PgDn",
            "caps_lock": "CAPS",
            **{f"f{i}": f"F{i}" for i in range(1, 13)},
        },
    },
    "ZH": {
        "key": "按键", "combo": "组合键", "click": "点击", "scroll": "滚动",
        "left": "左键", "right": "右键", "middle": "中键",
        "up": "上", "down": "下",
        "special": {
            "space": "空格", "enter": "回车", "backspace": "退格",
            "tab": "制表", "esc": "ESC", "shift": "SHIFT", "ctrl": "CTRL",
            "alt": "ALT", "cmd": "Win", "up_arrow": "上", "down_arrow": "下",
            "left_arrow": "左", "right_arrow": "右", "delete": "删除",
            "home": "开始", "end": "结束", "page_up": "上页", "page_down": "下页",
            "caps_lock": "大写",
            **{f"f{i}": f"F{i}" for i in range(1, 13)},
        },
    },
    "AR": {
        "key": "مفتاح", "combo": "تركيبة", "click": "نقر", "scroll": "تمرير",
        "left": "يسار", "right": "يمين", "middle": "وسط",
        "up": "أعلى", "down": "أسفل",
        "special": {
            "space": "مسافة", "enter": "إدخال", "backspace": "حذف",
            "tab": "تاب", "esc": "ESC", "shift": "شيفت", "ctrl": "CTRL",
            "alt": "ALT", "cmd": "Win", "up_arrow": "أعلى", "down_arrow": "أسفل",
            "left_arrow": "يسار", "right_arrow": "يمين", "delete": "مسح",
            "home": "بداية", "end": "نهاية", "page_up": "صفحة↑", "page_down": "صفحة↓",
            "caps_lock": "كابس",
            **{f"f{i}": f"F{i}" for i in range(1, 13)},
        },
    },
}

                      

def _collect_modifier_keys():
                                                                        
    keys = set()
    for name in ("ctrl", "ctrl_l", "ctrl_r",
                 "shift", "shift_l", "shift_r",
                 "alt", "alt_l", "alt_r", "alt_gr",
                 "cmd", "cmd_l", "cmd_r"):
        k = getattr(keyboard.Key, name, None)
        if k is not None:
            keys.add(k)
    return keys

MODIFIER_KEYS = _collect_modifier_keys()

def _build_modifier_labels():
    m = {}
    for name, label in [("ctrl","Ctrl"),("ctrl_l","Ctrl"),("ctrl_r","Ctrl"),
                         ("shift","Shift"),("shift_l","Shift"),("shift_r","Shift"),
                         ("alt","Alt"),("alt_l","Alt"),("alt_r","Alt"),("alt_gr","AltGr"),
                         ("cmd","Win"),("cmd_l","Win"),("cmd_r","Win")]:
        k = getattr(keyboard.Key, name, None)
        if k is not None:
            m[k] = label
    return m

MODIFIER_LABELS = _build_modifier_labels()

def _build_key_map():
    m = {}
    pairs = [
        ("space","space"), ("enter","enter"), ("backspace","backspace"),
        ("tab","tab"), ("esc","esc"),
        ("shift","shift"),   ("shift_l","shift"),  ("shift_r","shift_r"),
        ("ctrl","ctrl"),     ("ctrl_l","ctrl"),     ("ctrl_r","ctrl_r"),
        ("alt","alt"),       ("alt_l","alt"),       ("alt_r","alt_r"),
        ("alt_gr","alt_r"),
        ("cmd","cmd"),       ("cmd_l","cmd"),       ("cmd_r","cmd_r"),
        ("up","up_arrow"), ("down","down_arrow"), ("left","left_arrow"), ("right","right_arrow"),
        ("delete","delete"), ("home","home"), ("end","end"),
        ("page_up","page_up"), ("page_down","page_down"), ("caps_lock","caps_lock"),
    ]
    for name, internal in pairs:
        k = getattr(keyboard.Key, name, None)
        if k is not None:
            m[k] = internal
    for i in range(1, 13):
        k = getattr(keyboard.Key, f"f{i}", None)
        if k is not None:
            m[k] = f"f{i}"
    return m

PYNPUT_KEY_MAP = _build_key_map()

       

BG_COLOR     = "#0d0d0d"
ACCENT_COLOR = "#1a1a1a"
BORDER_COLOR = "#161616"
TEXT_MUTED   = "#3a3a3a"

KEY_BG       = "#181818"
KEY_FG       = "#6a6a6a"
KEY_BORDER   = "#252525"
KEY_ACTIVE   = "#60b4f5"                     
KEY_ACTIVE_M = "#4ecfa0"                     
KEY_ACTIVE_CLICK = "#4ecfa0"               

REFRESH_MS   = 16                                                        

                   
                                                     
                                                                        
                                                                 

U = 34                            
GAP = 3                    

ROWS = [
                  
    [("esc","Esc",1), None,
     ("f1","F1",1),("f2","F2",1),("f3","F3",1),("f4","F4",1), None,
     ("f5","F5",1),("f6","F6",1),("f7","F7",1),("f8","F8",1), None,
     ("f9","F9",1),("f10","F10",1),("f11","F11",1),("f12","F12",1)],
                
    [("~","~",1),("1","1",1),("2","2",1),("3","3",1),("4","4",1),
     ("5","5",1),("6","6",1),("7","7",1),("8","8",1),("9","9",1),
     ("0","0",1),("-","-",1),("=","=",1),("backspace","⌫",2)],
            
    [("tab","Tab",1.5),("q","Q",1),("w","W",1),("e","E",1),("r","R",1),
     ("t","T",1),("y","Y",1),("u","U",1),("i","I",1),("o","O",1),
     ("p","P",1),("[","[",1),("]","]",1),("\\","\\",1.5)],
          
    [("caps_lock","Caps",1.75),("a","A",1),("s","S",1),("d","D",1),
     ("f","F",1),("g","G",1),("h","H",1),("j","J",1),("k","K",1),
     ("l","L",1),(";",";",1),("'","'",1),("enter","Enter",2.25)],
               
    [("shift","Shift",2.25),("z","Z",1),("x","X",1),("c","C",1),
     ("v","V",1),("b","B",1),("n","N",1),("m","M",1),(",",",",1),
     (".",  ".",1),("/","/",1),("shift_r","Shift",2.75)],
                
    [("ctrl","Ctrl",1.25),("cmd","Win",1.25),("alt","Alt",1.25),
     ("space","Space",6.25),
     ("alt_r","Alt",1.25),("cmd_r","Win",1.25),("ctrl_r","Ctrl",1.25)],
]

ARROW_KEYS = [
                                           
    [("up_arrow","▲",1)],
    [("left_arrow","◀",1),("down_arrow","▼",1),("right_arrow","▶",1)],
]

         

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return os.getuid() == 0

def rerun_as_admin():
    try:
        script = os.path.abspath(sys.argv[0])
        params = " ".join(f'"{a}"' for a in sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}" {params}', None, 1)
    except Exception as exc:
        import tkinter.messagebox as mb
        mb.showerror("Admin re-launch failed", str(exc))
    finally:
        os._exit(0)



          

class InputVisualiser:

    def __init__(self):
        self.lang  = "EN"
        self.lock  = threading.Lock()
        self.stats = {"keys": 0, "clicks": 0, "scrolls": 0}

                                                                          
        self._active      = set()
        self._active_lock = threading.Lock()

                           
        self._held_mods       = set()
        self._mod_lock        = threading.Lock()
        self._WIN_KEYS = {k for name in ("cmd","cmd_l","cmd_r")
                          for k in [getattr(keyboard.Key, name, None)] if k}
        self._win_combo_fired = set()

                                         
        self._mouse_active = set()

        self._build_window()
        self._start_listeners()
        self._schedule_refresh()

            

    def _build_window(self):
        self.root = tk.Tk()
        self.root.title("Input Visualiser")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.95)
        self.root.configure(bg=BG_COLOR)
        self.root.geometry(f"+12+12")
                                                                        
                                                                          
                                                                        

        self._build_header()
        self._build_keyboard()
        self._build_mouse_row()
        self._build_footer()

                                                                             
        self.root.after(50, self._set_click_through)

    def _set_click_through(self):
                   
        try:
            user32     = ctypes.windll.user32
            GWL_EXSTYLE       = -20
            WS_EX_LAYERED     = 0x00080000
            WS_EX_TRANSPARENT = 0x00000020
            WS_EX_TOPMOST     = 0x00000008                           

                                                                                
                                                                              
            hwnd = user32.FindWindowExW(None, None, None, "Input Visualiser")
            if not hwnd:
                                               
                hwnd = self.root.winfo_id()

            style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            user32.SetWindowLongW(
                hwnd, GWL_EXSTYLE,
                style | WS_EX_LAYERED | WS_EX_TRANSPARENT)

                                                                                        
            HWND_TOPMOST   = -1
            SWP_NOMOVE     = 0x0002
            SWP_NOSIZE     = 0x0001
            SWP_NOACTIVATE = 0x0010
            user32.SetWindowPos(
                hwnd, HWND_TOPMOST, 0, 0, 0, 0,
                SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE)

        except Exception:
            pass                               

    def _build_header(self):
        hdr = tk.Frame(self.root, bg=ACCENT_COLOR, padx=8, pady=4)
        hdr.pack(fill="x")

        self.live_dot = tk.Label(hdr, text="●", font=("Segoe UI", 8),
                                 fg="#4ecfa0", bg=ACCENT_COLOR)
        self.live_dot.pack(side="left")

        tk.Label(hdr, text=" Input Visualiser", font=("Consolas", 9, "bold"),
                 fg="#555555", bg=ACCENT_COLOR).pack(side="left")



    def _build_keyboard(self):
                                                
                             
        max_row_w = 0
        for row in ROWS:
            w = sum((item[2] if item else 0.5) for item in row if item is not None)
                  
            n = sum(1 for item in row if item is not None)
            w = w * U + (n - 1) * GAP
            max_row_w = max(max_row_w, w)

                                                      
        arrow_w = 3 * U + 2 * GAP + 8                       
        canvas_w = int(max_row_w) + int(arrow_w) + 12
        row_count = len(ROWS)
        canvas_h  = row_count * (U + GAP) + GAP + 6                          

        self.canvas = tk.Canvas(self.root, width=canvas_w, height=canvas_h,
                                bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(padx=6, pady=(4, 2))

        self._key_rects  = {}                                
        self._key_ids    = {}                                             

        pad_x = 6
        pad_y = 6

        for row_idx, row in enumerate(ROWS):
            x = pad_x
            y = pad_y + row_idx * (U + GAP)
            for item in row:
                if item is None:
                    x += U // 2                            
                    continue
                kid, label, w_units = item
                w = int(w_units * U + (w_units - 1) * GAP)
                h = U
                self._draw_key(kid, label, x, y, w, h)
                x += w + GAP

                                                                      
        arrow_x = pad_x + int(max_row_w) + 10
                                                                  
        up_y = pad_y + 4 * (U + GAP)
        self._draw_key("up_arrow", "▲", arrow_x + U + GAP, up_y, U, U)
        nav_y = up_y + U + GAP
        self._draw_key("left_arrow",  "◀", arrow_x,             nav_y, U, U)
        self._draw_key("down_arrow",  "▼", arrow_x + U + GAP,   nav_y, U, U)
        self._draw_key("right_arrow", "▶", arrow_x + 2*(U+GAP), nav_y, U, U)

    def _draw_key(self, kid, label, x, y, w, h):
        r = 4                  
        rid = self._rounded_rect(x, y, x + w, y + h, r, fill=KEY_BG, outline=KEY_BORDER)
        font_size = 7 if len(label) > 4 else (8 if len(label) > 2 else 9)
        tid = self.canvas.create_text(
            x + w // 2, y + h // 2,
            text=label, fill=KEY_FG,
            font=("Consolas", font_size, "bold"))
        self._key_rects[kid] = (rid, tid)

    def _rounded_rect(self, x1, y1, x2, y2, r, **kw):
        pts = [
            x1+r, y1,   x2-r, y1,
            x2, y1,     x2, y1+r,
            x2, y2-r,   x2, y2,
            x2-r, y2,   x1+r, y2,
            x1, y2,     x1, y2-r,
            x1, y1+r,   x1, y1,
        ]
        return self.canvas.create_polygon(pts, smooth=True, **kw)

    def _build_mouse_row(self):
                                                               
        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(pady=(0, 4))

        self._mouse_btns = {}
        btn_defs = [("left", "LMB"), ("middle", "MMB"), ("right", "RMB")]
        for kid, label in btn_defs:
            f = tk.Frame(frame, bg=KEY_BG,
                         highlightbackground=KEY_BORDER, highlightthickness=1,
                         width=48, height=22)
            f.pack_propagate(False)
            f.pack(side="left", padx=3)
            lbl = tk.Label(f, text=label, font=("Consolas", 8, "bold"),
                           fg=KEY_FG, bg=KEY_BG)
            lbl.pack(expand=True)
            self._mouse_btns[kid] = (f, lbl)

                          
        self._scroll_lbl = tk.Label(frame, text="▲▼", font=("Consolas", 8),
                                    fg=TEXT_MUTED, bg=BG_COLOR, padx=6)
        self._scroll_lbl.pack(side="left")

    def _build_footer(self):
        ftr = tk.Frame(self.root, bg=BORDER_COLOR, padx=8, pady=3)
        ftr.pack(fill="x")
        self.stat_lbl = tk.Label(
            ftr, text="keys: 0   clicks: 0   scrolls: 0",
            font=("Consolas", 8), fg="#3a3a3a", bg=BORDER_COLOR)
        self.stat_lbl.pack(side="left")
        tk.Label(ftr, text="Ctrl+Q to quit", font=("Consolas", 7),
                 fg="#fff", bg=BORDER_COLOR).pack(side="right")

        tk.Label(ftr, text="Ctrl+D toggle display", font=("Consolas", 7),
                 fg="#12e537", bg=BORDER_COLOR).pack(side="right")
                                
        if not is_admin():
            tk.Label(ftr, text="Ctrl+Shift+A to rerun as admin", font=("Consolas", 7),
                     fg="#1f80d0", bg=BORDER_COLOR).pack(side="right")

                    

    def _activate_key(self, kid):
        with self._active_lock:
            self._active.add(kid)

    def _deactivate_key(self, kid):
        with self._active_lock:
            self._active.discard(kid)

    def _activate_mouse(self, btn):
        self._mouse_active.add(btn)

                            

    def _key_id(self, key):
                                                    
        mapped = PYNPUT_KEY_MAP.get(key)
        if mapped:
            return mapped
        if hasattr(key, "char") and key.char and key.char.isprintable():
            return key.char.lower()
        if hasattr(key, "vk") and key.vk:
            vk = key.vk
            if 65 <= vk <= 90:
                return chr(vk + 32)             
            if 48 <= vk <= 57:
                return chr(vk)
        return None

    def _key_display(self, key, L):
        special = PYNPUT_KEY_MAP.get(key)
        if special:
            return L["special"].get(special, special.upper())
        if hasattr(key, "char") and key.char and key.char.isprintable():
            return key.char.upper()
        if hasattr(key, "vk") and key.vk:
            vk = key.vk
            if 65 <= vk <= 90:
                return chr(vk)
            if 48 <= vk <= 57:
                return chr(vk)
            if 96 <= vk <= 105:
                return f"Num{vk - 96}"
        return str(key).replace("Key.", "").upper()

    def _mod_display(self, mod_key, L):
        internal = PYNPUT_KEY_MAP.get(mod_key, "")
        return L["special"].get(internal, MODIFIER_LABELS.get(mod_key, "Mod"))

               

    def _start_listeners(self):

        def on_key_press(key):
            kid = self._key_id(key)
            if kid:
                self._activate_key(kid)

            if key in MODIFIER_KEYS:
                with self._mod_lock:
                    self._held_mods.add(key)
                if key in self._WIN_KEYS:
                    self._win_combo_fired.discard(key)
                return

            with self._mod_lock:
                mods = set(self._held_mods)

                           
                                              
                                            
                                                                                 
            q_pressed = (hasattr(key, "char") and key.char in ("q", "Q")) or                        (hasattr(key, "vk") and key.vk == 81)
            a_pressed = (hasattr(key, "char") and key.char in ("a", "A")) or                        (hasattr(key, "vk") and key.vk == 65)
            d_pressed = (hasattr(key, "char") and key.char in ("d", "D")) or                        (hasattr(key, "vk") and key.vk == 68)
            ctrl_held  = any(k in mods for k in (
                getattr(keyboard.Key, "ctrl",   None),
                getattr(keyboard.Key, "ctrl_l", None),
                getattr(keyboard.Key, "ctrl_r", None),
            ) if k)
            shift_held = any(k in mods for k in (
                getattr(keyboard.Key, "shift",   None),
                getattr(keyboard.Key, "shift_l", None),
                getattr(keyboard.Key, "shift_r", None),
            ) if k)
            if ctrl_held and q_pressed:
                self.root.after(0, self.quit)
                return
            if ctrl_held and shift_held and a_pressed and not is_admin():
                self.root.after(0, rerun_as_admin)
                return
            if ctrl_held and d_pressed:
                self.root.after(0, self._toggle_display)
                return

            self.stats["keys"] += 1

            if mods:
                for wk in self._WIN_KEYS:
                    if wk in mods:
                        self._win_combo_fired.add(wk)

        def on_key_release(key):
            kid = self._key_id(key)
            if kid:
                self._deactivate_key(kid)

            with self._mod_lock:
                self._held_mods.discard(key)

            if key in self._WIN_KEYS:
                if key not in self._win_combo_fired:
                    self.stats["keys"] += 1
                self._win_combo_fired.discard(key)

        def on_click(x, y, button, pressed):
            btn_map = {
                mouse.Button.left:   "left",
                mouse.Button.right:  "right",
                mouse.Button.middle: "middle",
            }
            btn = btn_map.get(button, "left")
            if pressed:
                self.stats["clicks"] += 1
                self._activate_mouse(btn)
            else:
                self._mouse_active.discard(btn)

        def on_scroll(x, y, dx, dy):
            self.stats["scrolls"] += 1
            self._scroll_flash = time.time() + 0.25

        self._scroll_flash = 0.0

        self.kb_listener = keyboard.Listener(
            on_press=on_key_press, on_release=on_key_release)
        self.ms_listener = mouse.Listener(
            on_click=on_click, on_scroll=on_scroll)
        self.kb_listener.daemon = True
        self.ms_listener.daemon = True
        self.kb_listener.start()
        self.ms_listener.start()

             

    def _schedule_refresh(self):
        try:
            self._refresh()
        except Exception:
            pass
        self.root.after(REFRESH_MS, self._schedule_refresh)

    def _refresh(self):
        now = time.time()

        with self._active_lock:
            active_now = set(self._active)

        MODIFIER_IDS = {
            "ctrl","ctrl_r","shift","shift_r","alt","alt_r","cmd","cmd_r","caps_lock"
        }

        for kid, (rid, tid) in self._key_rects.items():
            if kid in active_now:
                color = KEY_ACTIVE_M if kid in MODIFIER_IDS else KEY_ACTIVE
                self.canvas.itemconfig(rid, fill=color, outline=color)
                self.canvas.itemconfig(tid, fill="#0d0d0d")
            else:
                self.canvas.itemconfig(rid, fill=KEY_BG,  outline=KEY_BORDER)
                self.canvas.itemconfig(tid, fill=KEY_FG)

        for btn, (frm, lbl) in self._mouse_btns.items():
            if btn in self._mouse_active:
                frm.config(highlightbackground=KEY_ACTIVE_CLICK, bg=KEY_ACTIVE_CLICK)
                lbl.config(bg=KEY_ACTIVE_CLICK, fg="#0d0d0d")
            else:
                frm.config(highlightbackground=KEY_BORDER, bg=KEY_BG)
                lbl.config(bg=KEY_BG, fg=KEY_FG)

        if now < self._scroll_flash:
            self._scroll_lbl.config(fg="#f5a623")
        else:
            self._scroll_lbl.config(fg=TEXT_MUTED)

        any_active = bool(active_now) or bool(self._mouse_active) or now < self._scroll_flash
        self.live_dot.config(fg="#ff4444" if any_active else "#4ecfa0")
        s = self.stats
        self.stat_lbl.config(
            text=f"keys: {s['keys']}   clicks: {s['clicks']}   scrolls: {s['scrolls']}")

                         

    def run(self):
        self.root.mainloop()

    def _toggle_display(self):
        if self.root.winfo_viewable():
            self.root.withdraw()
        else:
            self.root.deiconify()

    def quit(self):
        self.kb_listener.stop()
        self.ms_listener.stop()
        self.root.destroy()


if __name__ == "__main__":
    app = InputVisualiser()
    app.run()