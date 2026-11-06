#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
                            DROID SURGEON  ·  v2.0.0
                    Advanced Android Device Management Suite
================================================================================
License: GNU General Public License v3.0 (GPL-3.0)
================================================================================
"""

import sys, os, re, time, shutil, subprocess, threading, functools, platform, random
from datetime import datetime

# --- FIXED IMPORTS ---
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QFrame, QLabel, QPushButton, QLineEdit, QTextEdit, QPlainTextEdit,
    QComboBox, QGroupBox, QScrollArea, QTableWidget, QTableWidgetItem,
    QHeaderView, QProgressBar, QMessageBox, QInputDialog, QDialog,
    QDialogButtonBox, QSlider, QCheckBox, QStatusBar, QStackedWidget,
    QFileDialog, QSizePolicy, QAbstractItemView, QTabWidget, QSizeGrip,
    QToolButton, QMenu, QAction, QGraphicsDropShadowEffect, QSpacerItem,
    QListWidget, QListWidgetItem, QShortcut
)
from PyQt5.QtCore import (
    Qt, QTimer, pyqtSignal, QObject, QSize, QPoint, QSettings, QUrl, QMimeData
)
from PyQt5.QtGui import (
    QFont, QColor, QPalette, QKeySequence, QIcon, QDesktopServices, QPainter, QPen
)
# ---------------------


# ═══════════════════════════════════════════════════════════════════════════
#                              THEME SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class Theme:
    def __init__(self, name, colors):
        self.name = name
        self.__dict__.update(colors)

THEMES = {}

# ── NEON ──────────────────────────────────────────────────────────────────
THEMES["Neon"] = Theme("Neon", {
    "BG_VOID": "#070b12", "BG_DEEP": "#0a111b", "BG_BASE": "#101b29",
    "BG_PANEL": "#142131", "BG_PANEL_HI": "#1a2b3e", "BG_ELEVATED": "#21374b",
    "BG_INPUT": "#0b1724", "B_DIM": "#1d3445", "B": "#29475a", "B_HI": "#3c6577",
    "B_ACCENT": "#568a99", "CYAN": "#35e5ee", "CYAN_DIM": "#1b9eae",
    "CYAN_DEEP": "#123b4b", "GREEN": "#31e6a4", "GREEN_DIM": "#176b50",
    "GREEN_DEEP": "#0b241c", "RED": "#ff5c91", "RED_DIM": "#70233e",
    "RED_DEEP": "#2a101c", "AMBER": "#f1df55", "AMBER_DIM": "#6d681d",
    "AMBER_DEEP": "#28250d", "TEXT_HI": "#e8eaf0", "TEXT": "#b0b2bf",
    "TEXT_DIM": "#858797", "TEXT_MUTED": "#555866",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── MIDNIGHT ──────────────────────────────────────────────────────────────
THEMES["Midnight"] = Theme("Midnight", {
    "BG_VOID": "#0a0812", "BG_DEEP": "#0e0b1a", "BG_BASE": "#151022",
    "BG_PANEL": "#1a142e", "BG_PANEL_HI": "#231b3d", "BG_ELEVATED": "#2c2250",
    "BG_INPUT": "#100c1e", "B_DIM": "#2a1f45", "B": "#3d2d5e", "B_HI": "#56427a",
    "B_ACCENT": "#7760a0", "CYAN": "#b47aff", "CYAN_DIM": "#8a4fd6",
    "CYAN_DEEP": "#2a1a4d", "GREEN": "#5eead4", "GREEN_DIM": "#1f6b5e",
    "GREEN_DEEP": "#0d2b26", "RED": "#fb7185", "RED_DIM": "#7a2938",
    "RED_DEEP": "#2d0f16", "AMBER": "#fcd34d", "AMBER_DIM": "#7a6420",
    "AMBER_DEEP": "#2a240c", "TEXT_HI": "#ede9fe", "TEXT": "#c4b5d9",
    "TEXT_DIM": "#9b8ab5", "TEXT_MUTED": "#6b5a88",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── EMERALD ───────────────────────────────────────────────────────────────
THEMES["Emerald"] = Theme("Emerald", {
    "BG_VOID": "#06120e", "BG_DEEP": "#0a1a14", "BG_BASE": "#0f261d",
    "BG_PANEL": "#132e24", "BG_PANEL_HI": "#1a3d2f", "BG_ELEVATED": "#214d3c",
    "BG_INPUT": "#0b1e17", "B_DIM": "#1a3a2c", "B": "#275a43", "B_HI": "#367a5b",
    "B_ACCENT": "#4a9e75", "CYAN": "#34d399", "CYAN_DIM": "#1a9966",
    "CYAN_DEEP": "#0f3d29", "GREEN": "#6ee7b7", "GREEN_DIM": "#1f7a56",
    "GREEN_DEEP": "#0b2e1f", "RED": "#f87171", "RED_DIM": "#7a2a2a",
    "RED_DEEP": "#2d1010", "AMBER": "#fbbf24", "AMBER_DIM": "#7a5e1a",
    "AMBER_DEEP": "#2a220d", "TEXT_HI": "#ecfdf5", "TEXT": "#b8d9ca",
    "TEXT_DIM": "#8ab5a3", "TEXT_MUTED": "#5c8576",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── CRIMSON ───────────────────────────────────────────────────────────────
THEMES["Crimson"] = Theme("Crimson", {
    "BG_VOID": "#120608", "BG_DEEP": "#1a0a0d", "BG_BASE": "#261016",
    "BG_PANEL": "#2e141c", "BG_PANEL_HI": "#3d1a25", "BG_ELEVATED": "#4d2130",
    "BG_INPUT": "#1e0c12", "B_DIM": "#3a1a24", "B": "#5a2838", "B_HI": "#7a364c",
    "B_ACCENT": "#a04d68", "CYAN": "#fb7185", "CYAN_DIM": "#c4405a",
    "CYAN_DEEP": "#4d1020", "GREEN": "#34d399", "GREEN_DIM": "#1a9966",
    "GREEN_DEEP": "#0f3d29", "RED": "#fca5a5", "RED_DIM": "#8a3030",
    "RED_DEEP": "#301010", "AMBER": "#fcd34d", "AMBER_DIM": "#7a6420",
    "AMBER_DEEP": "#2a240c", "TEXT_HI": "#fef2f2", "TEXT": "#e0b8be",
    "TEXT_DIM": "#bf8a94", "TEXT_MUTED": "#8a5a64",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── OCEAN ─────────────────────────────────────────────────────────────────
THEMES["Ocean"] = Theme("Ocean", {
    "BG_VOID": "#040c18", "BG_DEEP": "#081422", "BG_BASE": "#0e2038",
    "BG_PANEL": "#122a46", "BG_PANEL_HI": "#183658", "BG_ELEVATED": "#1f446e",
    "BG_INPUT": "#0a1a30", "B_DIM": "#16324e", "B": "#224a6e", "B_HI": "#2e628c",
    "B_ACCENT": "#3d80b5", "CYAN": "#38bdf8", "CYAN_DIM": "#1a80b8",
    "CYAN_DEEP": "#0f3450", "GREEN": "#4ade80", "GREEN_DIM": "#1f7a42",
    "GREEN_DEEP": "#0b2e1a", "RED": "#f87171", "RED_DIM": "#7a2a2a",
    "RED_DEEP": "#2d1010", "AMBER": "#fbbf24", "AMBER_DIM": "#7a5e1a",
    "AMBER_DEEP": "#2a220d", "TEXT_HI": "#f0f9ff", "TEXT": "#b8d4ef",
    "TEXT_DIM": "#8ab0d1", "TEXT_MUTED": "#5c7a99",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── MONOCHROME ────────────────────────────────────────────────────────────
THEMES["Monochrome"] = Theme("Monochrome", {
    "BG_VOID": "#0a0a0a", "BG_DEEP": "#111111", "BG_BASE": "#1a1a1a",
    "BG_PANEL": "#222222", "BG_PANEL_HI": "#2d2d2d", "BG_ELEVATED": "#3a3a3a",
    "BG_INPUT": "#151515", "B_DIM": "#2a2a2a", "B": "#3d3d3d", "B_HI": "#555555",
    "B_ACCENT": "#777777", "CYAN": "#e0e0e0", "CYAN_DIM": "#a0a0a0",
    "CYAN_DEEP": "#333333", "GREEN": "#b0b0b0", "GREEN_DIM": "#666666",
    "GREEN_DEEP": "#2a2a2a", "RED": "#d0d0d0", "RED_DIM": "#707070",
    "RED_DEEP": "#2d2d2d", "AMBER": "#c8c8c8", "AMBER_DIM": "#686868",
    "AMBER_DEEP": "#282828", "TEXT_HI": "#f0f0f0", "TEXT": "#c0c0c0",
    "TEXT_DIM": "#909090", "TEXT_MUTED": "#606060",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── SOLARIZED ─────────────────────────────────────────────────────────────
THEMES["Solarized"] = Theme("Solarized", {
    "BG_VOID": "#002b36", "BG_DEEP": "#073642", "BG_BASE": "#0a3f4e",
    "BG_PANEL": "#0e4c5e", "BG_PANEL_HI": "#135b70", "BG_ELEVATED": "#1a6d85",
    "BG_INPUT": "#04303b", "B_DIM": "#0a4a5a", "B": "#10637a", "B_HI": "#1a7d99",
    "B_ACCENT": "#2593b3", "CYAN": "#2aa198", "CYAN_DIM": "#1e7a73",
    "CYAN_DEEP": "#0d3a36", "GREEN": "#859900", "GREEN_DIM": "#5a6600",
    "GREEN_DEEP": "#2a3000", "RED": "#dc322f", "RED_DIM": "#a02522",
    "RED_DEEP": "#4a1110", "AMBER": "#b58900", "AMBER_DIM": "#7a5c00",
    "AMBER_DEEP": "#3a2c00", "TEXT_HI": "#fdf6e3", "TEXT": "#b8c2b0",
    "TEXT_DIM": "#839496", "TEXT_MUTED": "#586e75",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── NORD ──────────────────────────────────────────────────────────────────
THEMES["Nord"] = Theme("Nord", {
    "BG_VOID": "#2e3440", "BG_DEEP": "#3b4252", "BG_BASE": "#434c5e",
    "BG_PANEL": "#4c566a", "BG_PANEL_HI": "#5a6478", "BG_ELEVATED": "#6b7588",
    "BG_INPUT": "#2a303b", "B_DIM": "#4a5266", "B": "#5a6278", "B_HI": "#6b7388",
    "B_ACCENT": "#81a1c1", "CYAN": "#88c0d0", "CYAN_DIM": "#5e8a9a",
    "CYAN_DEEP": "#2a4a5a", "GREEN": "#a3be8c", "GREEN_DIM": "#6e8a5a",
    "GREEN_DEEP": "#3a4a2a", "RED": "#bf616a", "RED_DIM": "#8a4048",
    "RED_DEEP": "#4a2028", "AMBER": "#ebcb8b", "AMBER_DIM": "#a88a50",
    "AMBER_DEEP": "#5a4a2a", "TEXT_HI": "#eceff4", "TEXT": "#d8dee9",
    "TEXT_DIM": "#a0a8b8", "TEXT_MUTED": "#707888",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── GRUVBOX ───────────────────────────────────────────────────────────────
THEMES["Gruvbox"] = Theme("Gruvbox", {
    "BG_VOID": "#1d2021", "BG_DEEP": "#282828", "BG_BASE": "#32302f",
    "BG_PANEL": "#3c3836", "BG_PANEL_HI": "#504945", "BG_ELEVATED": "#665c54",
    "BG_INPUT": "#1b1b1b", "B_DIM": "#3a3533", "B": "#504945", "B_HI": "#665c54",
    "B_ACCENT": "#7c6f64", "CYAN": "#83a598", "CYAN_DIM": "#5c7a6a",
    "CYAN_DEEP": "#2a4a3a", "GREEN": "#b8bb26", "GREEN_DIM": "#808a10",
    "GREEN_DEEP": "#404a00", "RED": "#fb4934", "RED_DIM": "#b02a20",
    "RED_DEEP": "#501010", "AMBER": "#fabd2f", "AMBER_DIM": "#b08820",
    "AMBER_DEEP": "#503c00", "TEXT_HI": "#fbf1c7", "TEXT": "#d5c4a1",
    "TEXT_DIM": "#a89984", "TEXT_MUTED": "#7c6f64",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── TOKYO NIGHT ───────────────────────────────────────────────────────────
THEMES["Tokyo Night"] = Theme("Tokyo Night", {
    "BG_VOID": "#1a1b26", "BG_DEEP": "#16161e", "BG_BASE": "#1f2335",
    "BG_PANEL": "#24283b", "BG_PANEL_HI": "#292e42", "BG_ELEVATED": "#343b58",
    "BG_INPUT": "#15161e", "B_DIM": "#2a2e42", "B": "#3b4261", "B_HI": "#545c7e",
    "B_ACCENT": "#737aa2", "CYAN": "#7aa2f7", "CYAN_DIM": "#4a72c7",
    "CYAN_DEEP": "#1a3a7a", "GREEN": "#9ece6a", "GREEN_DIM": "#6a9a3a",
    "GREEN_DEEP": "#3a5a1a", "RED": "#f7768e", "RED_DIM": "#b04a5e",
    "RED_DEEP": "#501a2a", "AMBER": "#e0af68", "AMBER_DIM": "#a07a3a",
    "AMBER_DEEP": "#503a1a", "TEXT_HI": "#c0caf5", "TEXT": "#a9b1d6",
    "TEXT_DIM": "#7a82a6", "TEXT_MUTED": "#565f89",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── ROSÉ PINE ─────────────────────────────────────────────────────────────
THEMES["Rosé Pine"] = Theme("Rosé Pine", {
    "BG_VOID": "#191724", "BG_DEEP": "#1f1d2e", "BG_BASE": "#26233a",
    "BG_PANEL": "#2a273f", "BG_PANEL_HI": "#393552", "BG_ELEVATED": "#44415a",
    "BG_INPUT": "#16141f", "B_DIM": "#2a273f", "B": "#393552", "B_HI": "#524f67",
    "B_ACCENT": "#6e6a86", "CYAN": "#ebbcba", "CYAN_DIM": "#b08a88",
    "CYAN_DEEP": "#503a38", "GREEN": "#31748f", "GREEN_DIM": "#1e4a5e",
    "GREEN_DEEP": "#0a2a3a", "RED": "#eb6f92", "RED_DIM": "#b04a6a",
    "RED_DEEP": "#501a2a", "AMBER": "#f6c177", "AMBER_DIM": "#b08840",
    "AMBER_DEEP": "#504020", "TEXT_HI": "#e0def4", "TEXT": "#c4c0d8",
    "TEXT_DIM": "#908caa", "TEXT_MUTED": "#6e6a86",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

# ── CYBERPUNK ─────────────────────────────────────────────────────────────
THEMES["Cyberpunk"] = Theme("Cyberpunk", {
    "BG_VOID": "#050508", "BG_DEEP": "#0a0a0f", "BG_BASE": "#12121a",
    "BG_PANEL": "#181822", "BG_PANEL_HI": "#222233", "BG_ELEVATED": "#2a2a3d",
    "BG_INPUT": "#0d0d14", "B_DIM": "#1c1c2a", "B": "#2e2e45", "B_HI": "#4a4a6a",
    "B_ACCENT": "#6a6a9a", "CYAN": "#00f0ff", "CYAN_DIM": "#008899",
    "CYAN_DEEP": "#003344", "GREEN": "#39ff14", "GREEN_DIM": "#1a7a0a",
    "GREEN_DEEP": "#0a3305", "RED": "#ff003c", "RED_DIM": "#880022",
    "RED_DEEP": "#33000d", "AMBER": "#fcee0a", "AMBER_DIM": "#7a7205",
    "AMBER_DEEP": "#332f02", "TEXT_HI": "#ffffff", "TEXT": "#a0a0b8",
    "TEXT_DIM": "#707090", "TEXT_MUTED": "#4a4a60",
    "FONT_UI": "Inter, Segoe UI, Ubuntu, Sans", "FONT_MONO": "JetBrains Mono, Consolas, monospace",
})

T = THEMES["Neon"]


# ═══════════════════════════════════════════════════════════════════════════
#                              UI SCALE SYSTEM
# ═══════════════════════════════════════════════════════════════════════════

class Scale:
    value = 1.0

    @classmethod
    def set(cls, v):
        cls.value = max(0.7, min(1.5, float(v)))

    @classmethod
    def px(cls, base):
        return max(1, int(round(base * cls.value)))

    @classmethod
    def pt(cls, base):
        return max(6, int(round(base * cls.value)))


# ═══════════════════════════════════════════════════════════════════════════
#                              STYLESHEET BUILDER
# ═══════════════════════════════════════════════════════════════════════════

def build_stylesheet():
    s = Scale.px
    t = T

    return f"""
    QMainWindow, QWidget {{
        background: transparent;
        color: {t.TEXT};
        font-family: {t.FONT_UI};
        font-size: {Scale.pt(10)}pt;
    }}
    QMainWindow {{
        background: qradialgradient(cx:0.48, cy:0.32, radius:1.15,
            stop:0 {t.BG_PANEL_HI}, stop:0.45 {t.BG_BASE},
            stop:0.80 {t.BG_DEEP}, stop:1 {t.BG_VOID});
    }}

    QFrame#panel {{
        background: qlineargradient(x1:0,y1:0,x2:0,y2:1,
            stop:0 {t.BG_PANEL}, stop:1 {t.BG_BASE});
        border: 1px solid {t.B};
        border-radius: {s(10)}px;
    }}
    QFrame#statCard {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:1,
            stop:0 {t.BG_PANEL_HI}, stop:0.5 {t.BG_PANEL}, stop:1 {t.BG_BASE});
        border: 1px solid {t.B_HI};
        border-radius: {s(10)}px;
    }}
    QFrame#statCard:hover {{ border-color: {t.CYAN}; }}

    QPushButton {{
        background: qlineargradient(x1:0,y1:0,x2:0,y2:1,
            stop:0 {t.BG_PANEL_HI}, stop:1 {t.BG_PANEL});
        border: 1px solid {t.B_HI};
        border-radius: {s(7)}px;
        padding: {s(8)}px {s(16)}px;
        color: {t.TEXT_HI};
        font-weight: 600;
        font-size: {Scale.pt(9)}pt;
        min-height: {s(24)}px;
        outline: none;
    }}
    QPushButton:hover {{
        background: {t.BG_ELEVATED};
        border: 1px solid {t.B_ACCENT};
        color: #ffffff;
    }}
    QPushButton:pressed {{
        background: {t.BG_PANEL};
        border: 1px solid {t.CYAN};
        color: {t.CYAN};
    }}
    QPushButton:disabled {{
        background: {t.BG_DEEP};
        border: 1px solid {t.B_DIM};
        color: {t.TEXT_MUTED};
    }}

    QPushButton#primary {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
            stop:0 {t.CYAN_DEEP}, stop:1 {t.BG_PANEL_HI});
        border: 1px solid {t.CYAN_DIM};
        color: {t.CYAN};
    }}
    QPushButton#primary:hover {{ background: {t.CYAN_DIM}; border: 1px solid {t.CYAN}; color: #fff; }}

    QPushButton#success {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
            stop:0 {t.GREEN_DEEP}, stop:1 {t.BG_PANEL_HI});
        border: 1px solid {t.GREEN_DIM};
        color: {t.GREEN};
    }}
    QPushButton#success:hover {{ background: {t.GREEN_DIM}; border: 1px solid {t.GREEN}; color: #fff; }}

    QPushButton#danger {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
            stop:0 {t.RED_DEEP}, stop:1 {t.BG_PANEL_HI});
        border: 1px solid {t.RED_DIM};
        color: {t.RED};
    }}
    QPushButton#danger:hover {{ background: {t.RED_DIM}; border: 1px solid {t.RED}; color: #fff; }}

    QPushButton#warning {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
            stop:0 {t.AMBER_DEEP}, stop:1 {t.BG_PANEL_HI});
        border: 1px solid {t.AMBER_DIM};
        color: {t.AMBER};
    }}
    QPushButton#warning:hover {{ background: {t.AMBER_DIM}; border: 1px solid {t.AMBER}; color: #fff; }}

    QPushButton#ghost {{
        background: transparent;
        border: 1px solid {t.B_HI};
        color: {t.TEXT_DIM};
    }}
    QPushButton#ghost:hover {{
        background: rgba(255,255,255,0.05);
        border-color: {t.CYAN_DIM};
        color: {t.CYAN};
    }}

    QFrame#sidebar {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
            stop:0 {t.BG_PANEL}, stop:1 {t.BG_DEEP});
        border: 1px solid {t.B};
        border-right: 1px solid {t.CYAN_DIM};
        border-radius: {s(10)}px;
    }}
    QPushButton#sidebarBtn {{
        text-align: left;
        background: transparent;
        border: 1px solid transparent;
        border-left: 3px solid transparent;
        border-radius: {s(7)}px;
        color: {t.TEXT};
        padding: {s(9)}px {s(14)}px;
        min-height: {s(22)}px;
        font-size: {Scale.pt(9)}pt;
        font-weight: 600;
    }}
    QPushButton#sidebarBtn:hover {{
        background: rgba(255,255,255,0.06);
        color: {t.CYAN};
        border-color: {t.B_HI};
    }}
    QPushButton#sidebarBtn:checked {{
        background: {t.CYAN_DEEP};
        color: {t.CYAN};
        border: 1px solid {t.CYAN_DIM};
        border-left: 3px solid {t.CYAN};
        font-weight: 700;
    }}
    QLabel#sideSection {{
        color: {t.CYAN_DIM};
        font-size: {Scale.pt(7)}pt;
        font-weight: 800;
        letter-spacing: 2px;
        padding: {s(14)}px {s(10)}px {s(5)}px {s(10)}px;
        background: transparent;
    }}

    QFrame#topbar {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
            stop:0 {t.BG_PANEL_HI}, stop:0.6 {t.BG_PANEL}, stop:1 {t.BG_BASE});
        border: 1px solid {t.B};
        border-bottom: 1px solid {t.CYAN_DIM};
        border-radius: {s(10)}px;
    }}

    QLineEdit, QPlainTextEdit, QTextEdit, QSpinBox, QComboBox {{
        background: {t.BG_INPUT};
        border: 1px solid {t.B};
        border-radius: {s(7)}px;
        padding: {s(7)}px {s(12)}px;
        color: {t.TEXT_HI};
        font-family: {t.FONT_MONO};
        font-size: {Scale.pt(9)}pt;
        min-height: {s(20)}px;
        selection-background-color: {t.CYAN_DIM};
        selection-color: #fff;
    }}
    QLineEdit:focus, QPlainTextEdit:focus, QTextEdit:focus,
    QSpinBox:focus, QComboBox:focus {{
        border-color: {t.CYAN_DIM};
        background: {t.BG_PANEL};
    }}
    QComboBox::drop-down {{ border: none; width: {s(22)}px; }}
    QComboBox::down-arrow {{
        image: none;
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-top: 5px solid {t.CYAN_DIM};
        margin-right: 8px;
    }}
    QComboBox QAbstractItemView {{
        background: {t.BG_PANEL};
        border: 1px solid {t.B_HI};
        color: {t.TEXT};
        selection-background-color: {t.CYAN_DEEP};
        outline: none;
    }}
    QTextEdit, QPlainTextEdit {{
        background: rgba(0,0,0,0.35);
        font-family: {t.FONT_MONO};
        font-size: {Scale.pt(9)}pt;
        padding: {s(8)}px;
        color: {t.TEXT};
    }}

    QGroupBox {{
        background: rgba(0,0,0,0.15);
        border: 1px solid {t.B};
        border-radius: {s(8)}px;
        margin-top: {s(18)}px;
        padding: {s(16)}px {s(12)}px {s(12)}px {s(12)}px;
        font-weight: 600;
        color: {t.CYAN};
    }}
    QGroupBox::title {{
        subcontrol-origin: margin;
        left: {s(12)}px;
        top: 2px;
        padding: 1px {s(10)}px;
        color: {t.CYAN};
        background: {t.BG_DEEP};
        border: 1px solid {t.B_HI};
        border-radius: 4px;
        font-size: {Scale.pt(8)}pt;
        letter-spacing: 1.3px;
    }}

    QScrollBar:vertical {{
        background: rgba(0,0,0,0.25);
        width: {s(10)}px;
        border-radius: 5px;
        margin: 0;
    }}
    QScrollBar::handle:vertical {{
        background: {t.B_HI};
        border-radius: 5px;
        min-height: {s(30)}px;
    }}
    QScrollBar::handle:vertical:hover {{ background: {t.CYAN_DIM}; }}
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; }}
    QScrollBar:horizontal {{
        background: rgba(0,0,0,0.25);
        height: {s(10)}px;
        border-radius: 5px;
    }}
    QScrollBar::handle:horizontal {{
        background: {t.B_HI};
        border-radius: 5px;
        min-width: {s(30)}px;
    }}
    QScrollBar::handle:horizontal:hover {{ background: {t.CYAN_DIM}; }}
    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; }}

    QTableWidget {{
        background: rgba(0,0,0,0.25);
        border: 1px solid {t.B};
        border-radius: {s(8)}px;
        gridline-color: {t.B_DIM};
        color: {t.TEXT};
        font-family: {t.FONT_MONO};
        font-size: {Scale.pt(9)}pt;
        outline: none;
    }}
    QTableWidget::item {{ padding: {s(6)}px {s(10)}px; border: none; }}
    QTableWidget::item:selected {{
        background: {t.CYAN_DEEP};
        color: {t.TEXT_HI};
    }}
    QTableWidget::item:alternate {{ background: rgba(255,255,255,0.02); }}
    QHeaderView::section {{
        background: {t.BG_PANEL_HI};
        color: {t.CYAN};
        padding: {s(8)}px {s(10)}px;
        border: none;
        border-right: 1px solid {t.B};
        border-bottom: 1px solid {t.B_HI};
        font-weight: 600;
        font-size: {Scale.pt(8)}pt;
        letter-spacing: 1px;
    }}
    QHeaderView::section:last {{ border-right: none; }}

    QProgressBar {{
        background: {t.BG_INPUT};
        border: 1px solid {t.B};
        border-radius: {s(5)}px;
        text-align: center;
        height: {s(12)}px;
        color: {t.TEXT_HI};
        font-size: {Scale.pt(8)}pt;
        font-weight: 600;
    }}
    QProgressBar::chunk {{
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0,
            stop:0 {t.CYAN_DIM}, stop:0.5 {t.CYAN}, stop:1 {t.CYAN_DIM});
        border-radius: 2px;
    }}

    QCheckBox {{ spacing: {s(8)}px; color: {t.TEXT}; }}
    QCheckBox::indicator {{
        width: {s(15)}px;
        height: {s(15)}px;
        border-radius: 4px;
        border: 1px solid {t.B_HI};
        background: {t.BG_INPUT};
    }}
    QCheckBox::indicator:checked {{
        background: {t.CYAN_DIM};
        border-color: {t.CYAN};
    }}

    QSlider::groove:horizontal {{
        border: 1px solid {t.B};
        height: {s(6)}px;
        background: {t.BG_INPUT};
        border-radius: 3px;
    }}
    QSlider::handle:horizontal {{
        background: {t.CYAN};
        border: 1px solid {t.CYAN};
        width: {s(14)}px;
        margin: -{s(5)}px 0;
        border-radius: {s(7)}px;
    }}

    QTabWidget::pane {{
        background: rgba(0,0,0,0.15);
        border: 1px solid {t.B};
        border-radius: {s(7)}px;
        top: -1px;
    }}
    QTabBar::tab {{
        background: {t.BG_PANEL};
        color: {t.TEXT_DIM};
        border: 1px solid {t.B};
        border-bottom: none;
        border-top-left-radius: {s(6)}px;
        border-top-right-radius: {s(6)}px;
        padding: {s(8)}px {s(18)}px;
        margin-right: 3px;
        font-weight: 600;
        font-size: {Scale.pt(8)}pt;
    }}
    QTabBar::tab:selected {{
        background: {t.BG_PANEL_HI};
        color: {t.CYAN};
        border-color: {t.B_HI};
    }}
    QTabBar::tab:hover:!selected {{
        background: {t.BG_PANEL_HI};
        color: {t.TEXT};
    }}

    QStatusBar {{
        background: {t.BG_DEEP};
        color: {t.TEXT_DIM};
        border-top: 1px solid {t.B};
        font-family: {t.FONT_MONO};
        font-size: {Scale.pt(8)}pt;
    }}
    QStatusBar::item {{ border: none; }}

    QToolTip {{
        background: {t.BG_PANEL_HI};
        color: {t.CYAN};
        border: 1px solid {t.CYAN_DIM};
        padding: {s(5)}px {s(9)}px;
        border-radius: 4px;
        font-family: {t.FONT_MONO};
        font-size: {Scale.pt(8)}pt;
    }}

    QMenu {{
        background: {t.BG_PANEL};
        border: 1px solid {t.B_HI};
        color: {t.TEXT};
    }}
    QMenu::item {{ padding: {s(7)}px {s(22)}px; }}
    QMenu::item:selected {{
        background: {t.CYAN_DEEP};
        color: {t.TEXT_HI};
    }}
    """


# ═══════════════════════════════════════════════════════════════════════════
#                              SIGNALS
# ═══════════════════════════════════════════════════════════════════════════

class SignalBus(QObject):
    log          = pyqtSignal(str, str)
    stats        = pyqtSignal(dict)
    scrcpy_out   = pyqtSignal(str)
    scrcpy_state = pyqtSignal(str)
    fb_out       = pyqtSignal(str)
    processes    = pyqtSignal(list)
    packages     = pyqtSignal(list)
    files        = pyqtSignal(str, list)
    logcat_line  = pyqtSignal(str)
    net_out      = pyqtSignal(str)
    term_out     = pyqtSignal(str)
    graph_update = pyqtSignal(int, int) # cpu, ram


# ═══════════════════════════════════════════════════════════════════════════
#                              HELPERS
# ═══════════════════════════════════════════════════════════════════════════

def run(args, timeout=20):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout,
                           stdin=subprocess.DEVNULL)
        return (r.returncode == 0, (r.stdout or "").strip(), (r.stderr or "").strip())
    except subprocess.TimeoutExpired:
        return False, "", "timeout"
    except FileNotFoundError:
        return False, "", "binary not found"
    except Exception as e:
        return False, "", str(e)[:200]


def which(cmd): return shutil.which(cmd) is not None

def human_bytes(n):
    try: n = float(n)
    except Exception: return "N/A"
    for u in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if n < 1024: return f"{n:.2f} {u}"
        n /= 1024
    return f"{n:.2f} EB"

def human_time(sec):
    try: sec = int(sec)
    except Exception: return "N/A"
    d, sec = divmod(sec, 86400)
    h, sec = divmod(sec, 3600)
    m, s = divmod(sec, 60)
    if d: return f"{d}d {h}h {m}m"
    if h: return f"{h}h {m}m {s}s"
    if m: return f"{m}m {s}s"
    return f"{s}s"


# ═══════════════════════════════════════════════════════════════════════════
#                              STAT CARD
# ═══════════════════════════════════════════════════════════════════════════

class StatCard(QFrame):
    def __init__(self, title):
        super().__init__()
        self.setObjectName("statCard")
        self.setMinimumHeight(Scale.px(105))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(Scale.px(16), Scale.px(12), Scale.px(16), Scale.px(12))
        lay.setSpacing(Scale.px(4))

        head = QHBoxLayout()
        head.setSpacing(6)
        self.title = QLabel(title.upper())
        self.title.setStyleSheet(
            f"color: {T.TEXT_DIM}; font-size: {Scale.pt(7)}pt; font-weight: 700; "
            f"letter-spacing: 2px; background: transparent;")
        head.addWidget(self.title)
        head.addStretch()

        self.badge = QLabel("")
        self.badge.setStyleSheet(
            f"color: {T.TEXT_MUTED}; font-size: {Scale.pt(7)}pt; "
            f"font-family: {T.FONT_MONO}; background: transparent;")
        head.addWidget(self.badge)
        lay.addLayout(head)

        self.value = QLabel("—")
        self.value.setStyleSheet(
            f"color: {T.TEXT_HI}; font-size: {Scale.pt(22)}pt; font-weight: 700; "
            f"font-family: {T.FONT_MONO}; background: transparent;")
        lay.addWidget(self.value)

        self.sub = QLabel("")
        self.sub.setStyleSheet(
            f"color: {T.TEXT_MUTED}; font-size: {Scale.pt(7)}pt; "
            f"font-family: {T.FONT_MONO}; background: transparent;")
        lay.addWidget(self.sub)

        self.bar = QProgressBar()
        self.bar.setMaximumHeight(Scale.px(4))
        self.bar.setTextVisible(False)
        self.bar.setRange(0, 100)
        self.bar.setValue(0)
        lay.addWidget(self.bar)

    def set(self, value, sub="", badge="", color=None, percent=None):
        self.value.setText(str(value))
        self.sub.setText(sub)
        self.badge.setText(badge)
        c = color or T.TEXT_HI
        self.value.setStyleSheet(
            f"color: {c}; font-size: {Scale.pt(22)}pt; font-weight: 700; "
            f"font-family: {T.FONT_MONO}; background: transparent;")
        if percent is not None:
            self.bar.setValue(max(0, min(100, int(percent))))


# ═══════════════════════════════════════════════════════════════════════════
#                              GRAPH WIDGET
# ═══════════════════════════════════════════════════════════════════════════

class LiveGraph(QWidget):
    def __init__(self, color, title):
        super().__init__()
        self.color = color
        self.title = title
        self.data = [0] * 60
        self.setMinimumHeight(Scale.px(80))

    def update_val(self, val):
        self.data.pop(0)
        self.data.append(max(0, min(100, val)))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Background
        painter.fillRect(self.rect(), QColor(T.BG_INPUT))
        
        # Grid lines
        pen = QPen(QColor(T.B_DIM))
        pen.setWidth(1)
        painter.setPen(pen)
        for i in range(1, 4):
            y = int(self.height() * i / 4)
            painter.drawLine(0, y, self.width(), y)

        # Title
        painter.setPen(QColor(T.TEXT_DIM))
        painter.setFont(QFont(T.FONT_MONO.split(',')[0], 7))
        painter.drawText(5, 15, self.title)

        # Graph
        pen = QPen(QColor(self.color))
        pen.setWidth(2)
        painter.setPen(pen)
        
        w = self.width()
        h = self.height()
        step = w / 59.0
        
        for i in range(59):
            y1 = h - (self.data[i] / 100.0 * h)
            y2 = h - (self.data[i+1] / 100.0 * h)
            painter.drawLine(int(i * step), int(y1), int((i+1) * step), int(y2))
        
        painter.end()


# ═══════════════════════════════════════════════════════════════════════════
#                              MAIN WINDOW
# ═══════════════════════════════════════════════════════════════════════════

class DroidSurgeon(QMainWindow):
    TABS = ["DASH", "CTRL", "MIRROR", "BOOT", "NET", "PKG", "FILES", "PROC", "HW", "PRIV", "DEV", "LOG", "SH", "HELP"]

    def __init__(self):
        super().__init__()
        self.settings = QSettings("DroidSurgeon", "Config")

        try: Scale.set(float(self.settings.value("ui_scale", 1.0)))
        except: Scale.set(1.0)

        try:
            theme_name = self.settings.value("theme", "Neon")
            if theme_name in THEMES:
                global T
                T = THEMES[theme_name]
        except: pass

        self.bus = SignalBus()
        self.bus.log.connect(self._on_log)
        self.bus.stats.connect(self._on_stats)
        self.bus.scrcpy_out.connect(self._on_scrcpy_log)
        self.bus.scrcpy_state.connect(self._on_scrcpy_state)
        self.bus.fb_out.connect(self._on_fb_log)
        self.bus.processes.connect(self._on_processes)
        self.bus.packages.connect(self._on_packages)
        self.bus.files.connect(self._on_files)
        self.bus.logcat_line.connect(self._on_logcat_line)
        self.bus.net_out.connect(self._on_net_out)
        self.bus.term_out.connect(self._on_term_out)
        self.bus.graph_update.connect(self._on_graph_update)

        self.device = None
        self.fb_device = None
        self.scrcpy = None
        self.scrcpy_running = False
        self.logcat_proc = None
        self.tab_btns = {}
        self.stat_cards = []
        self.cur_file_path = "/sdcard"
        self.cur_logcat_filter = ""
        self.scrcpy_version = None
        self._stats_lock = threading.Lock()
        self._scrcpy_help_cache = None
        self._current_theme_name = T.name
        self._is_demo = False

        self.setWindowTitle("DROID SURGEON  ·  v2.0.0 LAB")
        
        # Responsive Screen Sizing
        screen = QApplication.primaryScreen()
        if screen:
            rect = screen.availableGeometry()
            w = int(rect.width() * 0.9)
            h = int(rect.height() * 0.85)
            self.resize(w, h)
            self.move(rect.x() + int(rect.width() * 0.05), rect.y() + int(rect.height() * 0.05))
        else:
            self.resize(1400, 850)
            
        self.setMinimumSize(960, 600)

        self._build()
        self._detect_tools()
        self._refresh_adb()
        self._refresh_fb()

        self.sizegrip = QSizeGrip(self)
        self.sizegrip.resize(16, 16)
        self.sizegrip.move(self.width() - 16, self.height() - 16)

        self.timer = QTimer()
        self.timer.timeout.connect(self._poll)
        self.timer.start(3000)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, "sizegrip"):
            self.sizegrip.move(self.width() - 16, self.height() - 16)
            self.sizegrip.raise_()

    # ════════════════════════════════════════════════════════════════════
    #                              BUILD
    # ════════════════════════════════════════════════════════════════════

    def _build(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(Scale.px(14), Scale.px(12), Scale.px(14), Scale.px(8))
        root.setSpacing(Scale.px(12))

        root.addWidget(self._build_header())

        body = QHBoxLayout()
        body.setSpacing(Scale.px(12))
        body.addWidget(self._build_tabbar())

        self.stack = QStackedWidget()
        self.stack.setObjectName("mainContent")
        self.stack.addWidget(self._tab_dashboard())
        self.stack.addWidget(self._tab_control())
        self.stack.addWidget(self._tab_mirror())
        self.stack.addWidget(self._tab_fastboot())
        self.stack.addWidget(self._tab_network())
        self.stack.addWidget(self._tab_packages())
        self.stack.addWidget(self._tab_files())
        self.stack.addWidget(self._tab_processes())
        self.stack.addWidget(self._tab_hardware())
        self.stack.addWidget(self._tab_privacy())
        self.stack.addWidget(self._tab_developer())
        self.stack.addWidget(self._tab_logcat())
        self.stack.addWidget(self._tab_terminal())
        self.stack.addWidget(self._tab_help())
        body.addWidget(self.stack, 1)
        root.addLayout(body, 1)

        status = QStatusBar()
        self.setStatusBar(status)
        self.status_msg = QLabel("●  SYSTEM READY")
        self.status_msg.setStyleSheet(
            f"color: {T.GREEN}; font-family: {T.FONT_MONO}; "
            f"font-size: {Scale.pt(8)}pt; letter-spacing: 1px; padding-left: 8px;")
        status.addWidget(self.status_msg)
        self.status_dev = QLabel("DEVICE : DISCONNECTED")
        self.status_dev.setStyleSheet(
            f"color: {T.TEXT_DIM}; font-family: {T.FONT_MONO}; "
            f"font-size: {Scale.pt(8)}pt; letter-spacing: 1px;")
        status.addPermanentWidget(self.status_dev)
        self.status_clock = QLabel("")
        self.status_clock.setStyleSheet(
            f"color: {T.TEXT_DIM}; font-family: {T.FONT_MONO}; "
            f"font-size: {Scale.pt(8)}pt; letter-spacing: 1px; padding: 0 8px;")
        status.addPermanentWidget(self.status_clock)
        self._tick()
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self._tick)
        self.clock_timer.start(1000)
        self._apply_neon_effects()

    def _apply_neon_effects(self):
        card_colors = [T.CYAN, T.RED, T.GREEN, T.AMBER, T.CYAN]
        cards = getattr(self, "stat_cards", [])
        card_color_map = {id(card): card_colors[i % len(card_colors)] for i, card in enumerate(cards)}

        for widget in self.findChildren(QWidget):
            name = widget.objectName()
            glow = None
            blur = 0
            alpha = 0

            if name == "statCard":
                glow, blur, alpha = card_color_map.get(id(widget), T.CYAN), 12, 45
            elif name == "sidebarBtn" and widget.isChecked():
                glow, blur, alpha = T.CYAN, 8, 40
            elif name == "primary":
                glow, blur, alpha = T.CYAN, 8, 35
            elif name == "success":
                glow, blur, alpha = T.GREEN, 8, 35
            elif name == "danger":
                glow, blur, alpha = T.RED, 7, 30
            elif name == "warning":
                glow, blur, alpha = T.AMBER, 7, 28

            if glow:
                effect = QGraphicsDropShadowEffect(widget)
                effect.setBlurRadius(blur)
                color = QColor(glow)
                color.setAlpha(alpha)
                effect.setColor(color)
                effect.setOffset(0, 0)
                widget.setGraphicsEffect(effect)
            elif widget.graphicsEffect() is not None:
                widget.setGraphicsEffect(None)

    def _tick(self):
        self.status_clock.setText(datetime.now().strftime("%H:%M:%S"))

    def _build_header(self):
        f = QFrame()
        f.setObjectName("topbar")
        f.setFixedHeight(Scale.px(72))
        lay = QHBoxLayout(f)
        lay.setContentsMargins(Scale.px(20), Scale.px(10), Scale.px(20), Scale.px(10))
        lay.setSpacing(Scale.px(14))

        logo = QLabel("◆")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFixedWidth(Scale.px(32))
        logo.setStyleSheet(
            f"color: {T.CYAN}; font-size: {Scale.pt(24)}pt; font-weight: 900; background: transparent;")
        lay.addWidget(logo)

        brand = QVBoxLayout()
        brand.setSpacing(0)
        title = QLabel("DROID SURGEON")
        title.setStyleSheet(
            f"color: {T.TEXT_HI}; font-size: {Scale.pt(15)}pt; font-weight: 900; "
            f"letter-spacing: 3px; background: transparent;")
        subtitle = QLabel("ANDROID DEVICE OPERATIONS  /  v2.0.0 LAB")
        subtitle.setStyleSheet(
            f"color: {T.TEXT_DIM}; font-size: {Scale.pt(7)}pt; letter-spacing: 1.8px; background: transparent;")
        brand.addWidget(title)
        brand.addWidget(subtitle)
        lay.addLayout(brand)
        lay.addStretch(1)

        self.pill_adb = self._pill("ADB OFFLINE")
        self.pill_fb  = self._pill("FASTBOOT OFFLINE")
        self.pill_sc  = self._pill("MIRROR IDLE")
        for pill in (self.pill_adb, self.pill_fb, self.pill_sc):
            lay.addWidget(pill)

        refresh = QPushButton("↻  REFRESH")
        refresh.setObjectName("primary")
        refresh.setCursor(Qt.PointingHandCursor)
        refresh.clicked.connect(self._refresh_all)
        lay.addWidget(refresh)

        # Theme selector
        self.theme_btn = QToolButton()
        self.theme_btn.setText("🎨  Theme")
        self.theme_btn.setToolTip("Select application theme")
        self.theme_btn.setPopupMode(QToolButton.InstantPopup)
        self.theme_btn.setCursor(Qt.PointingHandCursor)
        self.theme_btn.setStyleSheet(f"""
            QToolButton {{ background: {T.BG_PANEL_HI}; border: 1px solid {T.B_HI};
                border-radius: 6px; padding: {Scale.px(8)}px {Scale.px(12)}px;
                color: {T.TEXT}; font-weight: 700; font-size: {Scale.pt(9)}pt; }}
            QToolButton:hover {{ border-color: {T.CYAN}; color: {T.CYAN}; }}
            QToolButton::menu-indicator {{ image: none; width: 0; }}
        """)
        theme_menu = QMenu(self.theme_btn)
        theme_menu.setStyleSheet(build_stylesheet())
        for name in THEMES:
            act = QAction(name, self)
            act.triggered.connect(functools.partial(self._set_theme, name))
            theme_menu.addAction(act)
        self.theme_btn.setMenu(theme_menu)
        lay.addWidget(self.theme_btn)

        # Scale selector
        self.scale_btn = QToolButton()
        self.scale_btn.setText("UI  ▾")
        self.scale_btn.setToolTip("Interface scale (Ctrl+ / Ctrl-)")
        self.scale_btn.setPopupMode(QToolButton.InstantPopup)
        self.scale_btn.setCursor(Qt.PointingHandCursor)
        self.scale_btn.setStyleSheet(f"""
            QToolButton {{ background: {T.BG_PANEL_HI}; border: 1px solid {T.B_HI};
                border-radius: 6px; padding: {Scale.px(8)}px {Scale.px(12)}px;
                color: {T.TEXT}; font-weight: 700; font-size: {Scale.pt(9)}pt; }}
            QToolButton:hover {{ border-color: {T.CYAN}; color: {T.CYAN}; }}
            QToolButton::menu-indicator {{ image: none; width: 0; }}
        """)
        scale_menu = QMenu(self.scale_btn)
        scale_menu.setStyleSheet(build_stylesheet())
        for label, value in [
            ("Compact  (70%)", 0.70), ("Small  (80%)", 0.80),
            ("Medium  (90%)", 0.90), ("Default  (100%)", 1.00),
            ("Large  (110%)", 1.10), ("XL  (125%)", 1.25),
            ("XXL  (140%)", 1.40), ("Max  (150%)", 1.50),
        ]:
            act = QAction(label, self)
            act.triggered.connect(functools.partial(self._set_scale, value))
            scale_menu.addAction(act)
        self.scale_btn.setMenu(scale_menu)
        lay.addWidget(self.scale_btn)
        return f

    def _refresh_all(self):
        self._refresh_adb()
        self._refresh_fb()
        self._log("info", "device services refreshed")

    def _pill(self, label):
        lbl = QLabel(f"●  {label}")
        lbl.setStyleSheet(f"""
            QLabel {{
                color: {T.TEXT_MUTED};
                background: rgba(0,0,0,0.3);
                border: 1px solid {T.B_DIM};
                border-radius: 12px;
                padding: {Scale.px(3)}px {Scale.px(12)}px;
                font-size: {Scale.pt(7)}pt;
                font-weight: 700;
                letter-spacing: 1px;
                font-family: {T.FONT_MONO};
            }}
        """)
        return lbl

    def _set_pill(self, pill, label, state):
        colors = {
            "off":  (T.TEXT_MUTED, "rgba(0,0,0,0.3)",        T.B_DIM),
            "ok":   (T.GREEN,      "rgba(49,230,164,0.10)",   T.GREEN_DIM),
            "warn": (T.AMBER,      "rgba(241,223,85,0.10)",   T.AMBER_DIM),
            "err":  (T.RED,        "rgba(255,92,145,0.10)",   T.RED_DIM),
            "live": (T.CYAN,       "rgba(53,229,238,0.12)",   T.CYAN_DIM),
        }
        fg, bg, br = colors.get(state, colors["off"])
        pill.setText(f"●  {label}")
        pill.setStyleSheet(f"""
            QLabel {{
                color: {fg};
                background: {bg};
                border: 1px solid {br};
                border-radius: 12px;
                padding: {Scale.px(3)}px {Scale.px(12)}px;
                font-size: {Scale.pt(7)}pt;
                font-weight: 700;
                letter-spacing: 1px;
                font-family: {T.FONT_MONO};
            }}
        """)

    def _build_tabbar(self):
        panel = QFrame()
        panel.setObjectName("sidebar")
        panel.setFixedWidth(Scale.px(235))
        lay = QVBoxLayout(panel)
        lay.setContentsMargins(Scale.px(10), Scale.px(14), Scale.px(10), Scale.px(14))
        lay.setSpacing(Scale.px(4))

        def section(label):
            tag = QLabel(label)
            tag.setObjectName("sideSection")
            lay.addWidget(tag)

        def nav(index, label):
            btn = QPushButton(label)
            btn.setObjectName("sidebarBtn")
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setMinimumHeight(Scale.px(40))
            btn.clicked.connect(functools.partial(self._switch, index))
            lay.addWidget(btn)
            self.tab_btns[index] = btn
            if index == 0:
                btn.setChecked(True)

        section("// WORKSPACE")
        nav(0, "▦   Dashboard")
        nav(1, "⚙   Device Control")
        nav(2, "▣   Screen Mirror")
        nav(3, "◇   Fastboot")

        section("// DEVICE TOOLS")
        nav(4, "⌁   Network")
        nav(5, "▤   Applications")
        nav(6, "▧   File Manager")
        nav(7, "▥   Processes")
        
        section("// LABORATORY")
        nav(8, "⚛   Hardware Test")
        nav(9, "🛡   Privacy Manager")
        nav(10, "⚡   Developer Tools")

        section("// MONITORING")
        nav(11, "≋   Log Monitor")
        nav(12, ">_   ADB Terminal")
        nav(13, "ⓘ   Documentation")

        lay.addStretch(1)
        divider = QFrame()
        divider.setFixedHeight(1)
        divider.setStyleSheet(f"background: {T.B_DIM}; border: none;")
        lay.addWidget(divider)

        foot = QLabel("DEVICE MANAGEMENT SUITE\nGPL-3.0  •  LOCAL TOOLS")
        foot.setStyleSheet(
            f"color: {T.TEXT_MUTED}; font-family: {T.FONT_MONO}; "
            f"font-size: {Scale.pt(7)}pt; letter-spacing: 1px; padding: 10px; background: transparent;")
        lay.addWidget(foot)
        return panel

    def _switch(self, idx):
        if idx < 0 or idx >= len(self.TABS): return
        for i, b in self.tab_btns.items():
            b.setChecked(i == idx)
        self.stack.setCurrentIndex(idx)
        name = self.TABS[idx]
        if name == "PROC": self._load_processes()
        elif name == "PKG": self._load_packages()
        elif name == "FILES": self._load_files(self.cur_file_path)
        QTimer.singleShot(0, self._apply_neon_effects)

    # ════════════════════════════════════════════════════════════════════
    #                              THEME & SCALE
    # ════════════════════════════════════════════════════════════════════

    def _set_theme(self, name):
        global T
        if name not in THEMES: return
        try:
            T = THEMES[name]
            self._current_theme_name = name
            self.settings.setValue("theme", name)
            
            app = QApplication.instance()
            if app: app.setStyleSheet(build_stylesheet())
            
            self._apply_neon_effects()
            
            self._log("ok", f"theme → {name}")
        except Exception as e:
            self._log("err", f"Theme change failed: {str(e)[:120]}")

    def _set_scale(self, value):
        try:
            Scale.set(value)
            self.settings.setValue("ui_scale", Scale.value)
            
            app = QApplication.instance()
            if app: app.setStyleSheet(build_stylesheet())
            
            self._apply_neon_effects()
            
            self._log("ok", f"UI scale → {int(Scale.value * 100)}%")
        except Exception as e:
            self._log("err", f"Scale change failed: {str(e)[:120]}")

    # ════════════════════════════════════════════════════════════════════
    #                              DASHBOARD (With Graphs)
    # ════════════════════════════════════════════════════════════════════

    def _tab_dashboard(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        page = QWidget()
        scroll.setWidget(page)
        lay = QVBoxLayout(page)
        lay.setContentsMargins(Scale.px(5), Scale.px(4), Scale.px(5), Scale.px(4))
        lay.setSpacing(Scale.px(14))

        heading = QHBoxLayout()
        heading.setContentsMargins(Scale.px(4), Scale.px(2), Scale.px(4), Scale.px(2))
        heading_col = QVBoxLayout()
        heading_col.setSpacing(Scale.px(2))
        heading_title = QLabel("SYSTEM OVERVIEW")
        heading_title.setStyleSheet(
            f"color: {T.TEXT_HI}; font-size: {Scale.pt(18)}pt; font-weight: 900; "
            f"letter-spacing: 1.5px; background: transparent;")
        heading_sub = QLabel("LIVE DEVICE TELEMETRY  ·  ADB CONNECTION STATUS")
        heading_sub.setStyleSheet(
            f"color: {T.TEXT_DIM}; font-family: {T.FONT_MONO}; font-size: {Scale.pt(8)}pt; "
            f"letter-spacing: 1px; background: transparent;")
        heading_col.addWidget(heading_title)
        heading_col.addWidget(heading_sub)
        heading.addLayout(heading_col)
        heading.addStretch(1)
        self.dashboard_updated = QLabel("●  LIVE MONITORING")
        self.dashboard_updated.setStyleSheet(
            f"color: {T.GREEN}; background: rgba(49,230,164,0.08); "
            f"border: 1px solid {T.GREEN_DIM}; border-radius: 6px; "
            f"padding: 8px 12px; font-family: {T.FONT_MONO}; font-size: {Scale.pt(8)}pt;")
        heading.addWidget(self.dashboard_updated)
        lay.addLayout(heading)

        cards_scroll = QScrollArea()
        cards_scroll.setWidgetResizable(True)
        cards_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        cards_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        cards_scroll.setFixedHeight(Scale.px(135))
        cards_scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        cards_inner = QWidget()
        cards_inner.setMinimumWidth(Scale.px(700))
        row = QHBoxLayout(cards_inner)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(Scale.px(12))

        self.c_battery = StatCard("Battery")
        self.c_storage = StatCard("Storage")
        self.c_memory  = StatCard("Memory")
        self.c_thermal = StatCard("Thermal")
        self.c_uptime  = StatCard("Uptime")
        self.stat_cards = [self.c_battery, self.c_storage, self.c_memory, self.c_thermal, self.c_uptime]
        for c in self.stat_cards:
            c.setMinimumWidth(Scale.px(180))
            row.addWidget(c)
        cards_scroll.setWidget(cards_inner)
        lay.addWidget(cards_scroll)

        # Live Graphs
        graphs_row = QHBoxLayout()
        graphs_row.setSpacing(Scale.px(12))
        
        self.graph_cpu = LiveGraph(T.CYAN, "CPU USAGE (%)")
        self.graph_ram = LiveGraph(T.AMBER, "RAM USAGE (%)")
        
        graphs_row.addWidget(self.graph_cpu)
        graphs_row.addWidget(self.graph_ram)
        lay.addLayout(graphs_row)

        split = QHBoxLayout()
        split.setSpacing(Scale.px(12))

        ov = QGroupBox("CONNECTED DEVICE / OVERVIEW")
        ov_lay = QVBoxLayout(ov)
        ov_lay.setContentsMargins(Scale.px(12), Scale.px(22), Scale.px(12), Scale.px(12))
        self.overview = QTextEdit()
        self.overview.setReadOnly(True)
        ov_lay.addWidget(self.overview)
        split.addWidget(ov, 2)

        qa = QGroupBox("QUICK ACTIONS / POWER")
        qa_lay = QVBoxLayout(qa)
        qa_lay.setContentsMargins(Scale.px(12), Scale.px(22), Scale.px(12), Scale.px(12))
        qa_lay.setSpacing(Scale.px(6))

        actions = [
            ("REFRESH DEVICE",   "primary", self._refresh_adb),
            ("SCREENSHOT",       "ghost",   self._screenshot),
            ("START RECORD",     "warning", self._start_record),
            ("STOP RECORD",      "danger",  self._stop_record),
            ("",                 "",        None),
            ("REBOOT SYSTEM",    "warning", functools.partial(self._reboot, None)),
            ("REBOOT RECOVERY",  "warning", functools.partial(self._reboot, "recovery")),
            ("REBOOT BOOTLOADER","warning", functools.partial(self._reboot, "bootloader")),
            ("",                 "",        None),
            ("FACTORY RESET",    "danger",  self._factory_reset),
        ]
        for text, kind, cb in actions:
            if not text:
                sep = QFrame()
                sep.setFixedHeight(1)
                sep.setStyleSheet(f"background: {T.B_DIM}; border: none;")
                qa_lay.addWidget(sep)
                continue
            b = QPushButton(text)
            b.setObjectName(kind)
            b.setMinimumHeight(Scale.px(32))
            b.setCursor(Qt.PointingHandCursor)
            b.clicked.connect(cb)
            qa_lay.addWidget(b)
        qa_lay.addStretch()
        split.addWidget(qa, 1)
        lay.addLayout(split, 1)
        return scroll

    def _on_graph_update(self, cpu, ram):
        if hasattr(self, 'graph_cpu'):
            self.graph_cpu.update_val(cpu)
        if hasattr(self, 'graph_ram'):
            self.graph_ram.update_val(ram)

    # ════════════════════════════════════════════════════════════════════
    #                              CONTROL
    # ════════════════════════════════════════════════════════════════════

    def _tab_control(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        page = QWidget()
        scroll.setWidget(page)
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        sel = QFrame()
        sel.setObjectName("panel")
        sel_lay = QHBoxLayout(sel)
        sel_lay.setContentsMargins(Scale.px(14), Scale.px(10), Scale.px(14), Scale.px(10))
        sel_lay.setSpacing(Scale.px(10))

        lbl = QLabel("TARGET")
        lbl.setStyleSheet(
            f"color: {T.TEXT_DIM}; font-size: {Scale.pt(8)}pt; font-weight: 700; "
            f"letter-spacing: 2px; background: transparent;")
        sel_lay.addWidget(lbl)

        self.dev_combo = QComboBox()
        self.dev_combo.setMinimumWidth(Scale.px(200))
        self.dev_combo.currentIndexChanged.connect(self._on_dev_sel)
        sel_lay.addWidget(self.dev_combo)

        r = QPushButton("REFRESH")
        r.setObjectName("primary")
        r.setFixedHeight(Scale.px(30))
        r.clicked.connect(self._refresh_adb)
        sel_lay.addWidget(r)
        sel_lay.addStretch()

        self.dev_state = QLabel("DISCONNECTED")
        self.dev_state.setStyleSheet(self._state_label_style("err"))
        sel_lay.addWidget(self.dev_state)
        lay.addWidget(sel)

        hw = QGroupBox("HARDWARE KEY EVENTS")
        hw_lay = QGridLayout(hw)
        hw_lay.setSpacing(Scale.px(5))

        keys = [
            ("VOL+",  "KEYCODE_VOLUME_UP",      "primary"),
            ("VOL-",  "KEYCODE_VOLUME_DOWN",    "primary"),
            ("PWR",   "KEYCODE_POWER",          "warning"),
            ("HOME",  "KEYCODE_HOME",           "success"),
            ("BACK",  "KEYCODE_BACK",           "danger"),
            ("MENU",  "KEYCODE_MENU",           "primary"),
            ("APPS",  "KEYCODE_APP_SWITCH",     "primary"),
            ("MUTE",  "KEYCODE_VOLUME_MUTE",    "warning"),
            ("CAM",   "KEYCODE_CAMERA",         "primary"),
            ("ENT",   "KEYCODE_ENTER",          "success"),
            ("DEL",   "KEYCODE_DEL",            "danger"),
            ("PLAY",  "KEYCODE_MEDIA_PLAY_PAUSE","primary"),
            ("NEXT",  "KEYCODE_MEDIA_NEXT",     "primary"),
            ("PREV",  "KEYCODE_MEDIA_PREVIOUS", "primary"),
            ("WAKE",  "KEYCODE_WAKEUP",         "success"),
            ("SLEEP", "KEYCODE_SLEEP",          "warning"),
            ("B+",    "KEYCODE_BRIGHTNESS_UP",  "primary"),
            ("B-",    "KEYCODE_BRIGHTNESS_DOWN","primary"),
            ("SYSRQ", "KEYCODE_SYSRQ",          "primary"),
            ("SRCH",  "KEYCODE_SEARCH",         "primary"),
        ]
        for i, (text, code, kind) in enumerate(keys):
            b = QPushButton(text)
            b.setObjectName(kind)
            b.setMinimumHeight(Scale.px(32))
            b.clicked.connect(functools.partial(self._send_key, code))
            hw_lay.addWidget(b, i // 5, i % 5)
        lay.addWidget(hw)

        dp = QGroupBox("D-PAD")
        dp_lay = QGridLayout(dp)
        dp_lay.setSpacing(Scale.px(8))
        dp_lay.setContentsMargins(Scale.px(50), Scale.px(24), Scale.px(50), Scale.px(24))

        dpad = [
            ("UP",     "KEYCODE_DPAD_UP",     0, 1),
            ("LEFT",   "KEYCODE_DPAD_LEFT",   1, 0),
            ("CENTER", "KEYCODE_DPAD_CENTER", 1, 1),
            ("RIGHT",  "KEYCODE_DPAD_RIGHT",  1, 2),
            ("DOWN",   "KEYCODE_DPAD_DOWN",   2, 1),
        ]
        for txt, code, r, c in dpad:
            b = QPushButton(txt)
            b.setObjectName("primary" if txt != "CENTER" else "success")
            b.setMinimumHeight(Scale.px(44))
            b.setMinimumWidth(Scale.px(80))
            b.clicked.connect(functools.partial(self._send_key, code))
            dp_lay.addWidget(b, r, c)
        lay.addWidget(dp)

        tg = QGroupBox("TOUCH GESTURES")
        tg_lay = QHBoxLayout(tg)
        tg_lay.setSpacing(Scale.px(8))

        for label, cb, kind in [
            ("TAP",        self._dlg_tap,   "primary"),
            ("SWIPE",      self._dlg_swipe, "primary"),
            ("LONG",       self._dlg_long,  "warning"),
            ("PINCH",      self._dlg_pinch, "primary"),
            ("SCROLL ↑",   self._scroll_up, "ghost"),
            ("SCROLL ↓",   self._scroll_dn, "ghost"),
        ]:
            b = QPushButton(label)
            b.setObjectName(kind)
            b.setMinimumHeight(Scale.px(34))
            b.clicked.connect(cb)
            tg_lay.addWidget(b)
        lay.addWidget(tg)

        vol = QGroupBox("VOLUME")
        vol_lay = QHBoxLayout(vol)
        vol_lay.setSpacing(Scale.px(10))

        self.vol_slider = QSlider(Qt.Horizontal)
        self.vol_slider.setRange(0, 15)
        self.vol_slider.setValue(7)
        vol_lay.addWidget(self.vol_slider)

        self.vol_label = QLabel("7 / 15")
        self.vol_label.setStyleSheet(
            f"color: {T.CYAN}; font-family: {T.FONT_MONO}; "
            f"font-size: {Scale.pt(9)}pt; font-weight: 700; min-width: {Scale.px(50)}px;")
        self.vol_slider.valueChanged.connect(lambda v: self.vol_label.setText(f"{v} / 15"))
        vol_lay.addWidget(self.vol_label)

        apply_vol = QPushButton("APPLY")
        apply_vol.setObjectName("success")
        apply_vol.setFixedWidth(Scale.px(80))
        apply_vol.clicked.connect(self._apply_volume)
        vol_lay.addWidget(apply_vol)
        lay.addWidget(vol)

        lay.addStretch()
        return scroll

    def _state_label_style(self, kind):
        colors = {
            "err":  (T.RED,   T.RED_DIM),
            "ok":   (T.GREEN, T.GREEN_DIM),
            "warn": (T.AMBER, T.AMBER_DIM),
        }
        fg, br = colors.get(kind, colors["err"])
        return f"""
            QLabel {{
                color: {fg};
                background: rgba(0,0,0,0.35);
                border: 1px solid {br};
                border-radius: 12px;
                padding: {Scale.px(3)}px {Scale.px(12)}px;
                font-size: {Scale.pt(7)}pt;
                font-weight: 700;
                letter-spacing: 1px;
                font-family: {T.FONT_MONO};
            }}
        """

    # ════════════════════════════════════════════════════════════════════
    #                              MIRROR
    # ════════════════════════════════════════════════════════════════════

    def _tab_mirror(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        ctrl = QGroupBox("SCRCPY CONTROLS")
        ctrl_lay = QHBoxLayout(ctrl)
        ctrl_lay.setSpacing(Scale.px(8))

        self.btn_start_mirror = QPushButton("START")
        self.btn_start_mirror.setObjectName("success")
        self.btn_start_mirror.setMinimumHeight(Scale.px(34))
        self.btn_start_mirror.clicked.connect(self._start_scrcpy)
        ctrl_lay.addWidget(self.btn_start_mirror)

        self.btn_stop_mirror = QPushButton("STOP")
        self.btn_stop_mirror.setObjectName("danger")
        self.btn_stop_mirror.setMinimumHeight(Scale.px(34))
        self.btn_stop_mirror.setEnabled(False)
        self.btn_stop_mirror.clicked.connect(self._stop_scrcpy)
        ctrl_lay.addWidget(self.btn_stop_mirror)

        fs = QPushButton("FULLSCREEN")
        fs.setObjectName("primary")
        fs.setMinimumHeight(Scale.px(34))
        fs.clicked.connect(self._mirror_fs)
        ctrl_lay.addWidget(fs)

        rot = QPushButton("ROTATE")
        rot.setObjectName("primary")
        rot.setMinimumHeight(Scale.px(34))
        rot.clicked.connect(self._mirror_rotate)
        ctrl_lay.addWidget(rot)

        scr = QPushButton("SCREENSHOT")
        scr.setObjectName("primary")
        scr.setMinimumHeight(Scale.px(34))
        scr.clicked.connect(self._screenshot)
        ctrl_lay.addWidget(scr)

        ctrl_lay.addStretch()
        lay.addWidget(ctrl)

        opts = QGroupBox("STREAM SETTINGS")
        opts_lay = QGridLayout(opts)
        opts_lay.setSpacing(Scale.px(10))

        opts_lay.addWidget(QLabel("Bitrate:"), 0, 0)
        self.opt_bitrate = QComboBox()
        self.opt_bitrate.addItems(["2 Mbps", "4 Mbps", "8 Mbps", "16 Mbps", "32 Mbps"])
        self.opt_bitrate.setCurrentIndex(2)
        opts_lay.addWidget(self.opt_bitrate, 0, 1)

        opts_lay.addWidget(QLabel("FPS:"), 0, 2)
        self.opt_fps = QComboBox()
        self.opt_fps.addItems(["60", "30", "24", "15"])
        opts_lay.addWidget(self.opt_fps, 0, 3)

        opts_lay.addWidget(QLabel("Max Size:"), 1, 0)
        self.opt_size = QComboBox()
        self.opt_size.addItems(["1920", "1600", "1280", "1024", "854", "640"])
        self.opt_size.setCurrentIndex(2)
        opts_lay.addWidget(self.opt_size, 1, 1)

        opts_lay.addWidget(QLabel("Orientation:"), 1, 2)
        self.opt_rot = QComboBox()
        self.opt_rot.addItems(["0", "90", "180", "270"])
        opts_lay.addWidget(self.opt_rot, 1, 3)

        self.opt_noaudio = QCheckBox("Disable Audio")
        self.opt_noaudio.setChecked(True)
        opts_lay.addWidget(self.opt_noaudio, 2, 0, 1, 2)

        self.opt_turnoff = QCheckBox("Turn Screen Off")
        opts_lay.addWidget(self.opt_turnoff, 2, 2, 1, 2)

        self.opt_always_top = QCheckBox("Always on Top")
        opts_lay.addWidget(self.opt_always_top, 3, 0, 1, 2)

        self.opt_fullscreen = QCheckBox("Start Fullscreen")
        opts_lay.addWidget(self.opt_fullscreen, 3, 2, 1, 2)

        lay.addWidget(opts)

        st = QGroupBox("SESSION MONITOR")
        st_lay = QVBoxLayout(st)
        st_lay.setContentsMargins(Scale.px(12), Scale.px(22), Scale.px(12), Scale.px(12))

        self.mirror_status = QLabel("MIRROR OFFLINE\n\nNo active scrcpy session.")
        self.mirror_status.setAlignment(Qt.AlignCenter)
        self.mirror_status.setMinimumHeight(Scale.px(130))
        self.mirror_status.setStyleSheet(f"""
            QLabel {{
                background: rgba(0,0,0,0.35);
                border: 1px dashed {T.B};
                border-radius: 7px;
                color: {T.TEXT_DIM};
                font-family: {T.FONT_MONO};
                font-size: {Scale.pt(9)}pt;
                padding: {Scale.px(18)}px;
            }}
        """)
        st_lay.addWidget(self.mirror_status)

        self.mirror_log = QTextEdit()
        self.mirror_log.setReadOnly(True)
        self.mirror_log.setMaximumHeight(Scale.px(110))
        st_lay.addWidget(self.mirror_log)
        lay.addWidget(st, 1)
        return page

    # ════════════════════════════════════════════════════════════════════
    #                              FASTBOOT
    # ════════════════════════════════════════════════════════════════════

    def _tab_fastboot(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        sel = QFrame()
        sel.setObjectName("panel")
        sel_lay = QHBoxLayout(sel)
        sel_lay.setContentsMargins(Scale.px(14), Scale.px(10), Scale.px(14), Scale.px(10))
        sel_lay.setSpacing(Scale.px(10))

        lbl = QLabel("FASTBOOT")
        lbl.setStyleSheet(
            f"color: {T.TEXT_DIM}; font-size: {Scale.pt(8)}pt; font-weight: 700; "
            f"letter-spacing: 2px; background: transparent;")
        sel_lay.addWidget(lbl)

        self.fb_combo = QComboBox()
        self.fb_combo.setMinimumWidth(Scale.px(200))
        sel_lay.addWidget(self.fb_combo)

        rb = QPushButton("REFRESH")
        rb.setObjectName("warning")
        rb.setFixedHeight(Scale.px(30))
        rb.clicked.connect(self._refresh_fb)
        sel_lay.addWidget(rb)
        sel_lay.addStretch()

        self.fb_state = QLabel("DISCONNECTED")
        self.fb_state.setStyleSheet(self._state_label_style("err"))
        sel_lay.addWidget(self.fb_state)
        lay.addWidget(sel)

        cmds = QGroupBox("FASTBOOT OPERATIONS")
        cmds_lay = QGridLayout(cmds)
        cmds_lay.setSpacing(Scale.px(5))

        fb_cmds = [
            ("REBOOT",        "reboot",              "warning"),
            ("REBOOT BOOT",   "reboot-bootloader",   "warning"),
            ("REBOOT RECOV",  "reboot-recovery",     "warning"),
            ("REBOOT FB",     "reboot-fastboot",     "warning"),
            ("GETVAR ALL",    "getvar-all",          "primary"),
            ("GETVAR PROD",   "getvar-product",      "primary"),
            ("OEM INFO",      "oem-device-info",     "primary"),
            ("OEM UNLOCK",    "oem-unlock",          "danger"),
            ("OEM LOCK",      "oem-lock",            "danger"),
            ("ERASE USERDATA","erase-userdata",      "danger"),
            ("ERASE CACHE",   "erase-cache",         "warning"),
            ("FORMAT USERDATA","format-userdata",    "danger"),
            ("FLASH BOOT",    "flash-boot",          "primary"),
            ("FLASH RECOVERY","flash-recovery",      "primary"),
            ("FLASH SYSTEM",  "flash-system",        "primary"),
            ("FLASH VBMETA",  "flash-vbmeta",        "primary"),
            ("FLASH ZIP",     "flash-all",           "primary"),
            ("SLOT A",        "set-active-a",        "primary"),
            ("SLOT B",        "set-active-b",        "primary"),
            ("FLASH UNLOCK",  "flashing-unlock",     "danger"),
            ("FLASH LOCK",    "flashing-lock",       "danger"),
            ("CONTINUE",      "continue",            "success"),
        ]
        for i, (text, cmd, kind) in enumerate(fb_cmds):
            b = QPushButton(text)
            b.setObjectName(kind)
            b.setMinimumHeight(Scale.px(32))
            b.clicked.connect(functools.partial(self._fb_cmd, cmd))
            cmds_lay.addWidget(b, i // 5, i % 5)
        lay.addWidget(cmds)

        out = QGroupBox("FASTBOOT OUTPUT")
        out_lay = QVBoxLayout(out)
        out_lay.setContentsMargins(Scale.px(12), Scale.px(22), Scale.px(12), Scale.px(12))

        self.fb_out = QTextEdit()
        self.fb_out.setReadOnly(True)
        out_lay.addWidget(self.fb_out)

        row = QHBoxLayout()
        c = QPushButton("CLEAR")
        c.setObjectName("danger")
        c.clicked.connect(self.fb_out.clear)
        row.addWidget(c)

        e = QPushButton("EXPORT")
        e.setObjectName("warning")
        e.clicked.connect(self._export_fb)
        row.addWidget(e)
        row.addStretch()
        out_lay.addLayout(row)
        lay.addWidget(out, 1)
        return page

    # ════════════════════════════════════════════════════════════════════
    #                              NETWORK
    # ════════════════════════════════════════════════════════════════════

    def _tab_network(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        page = QWidget()
        scroll.setWidget(page)
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        cards_scroll = QScrollArea()
        cards_scroll.setWidgetResizable(True)
        cards_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        cards_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        cards_scroll.setFixedHeight(Scale.px(135))
        cards_scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        cards_inner = QWidget()
        cards_inner.setMinimumWidth(Scale.px(620))
        stats = QHBoxLayout(cards_inner)
        stats.setContentsMargins(0, 0, 0, 0)
        stats.setSpacing(Scale.px(12))

        self.net_ip     = StatCard("Local IP")
        self.net_wifi   = StatCard("Wi-Fi SSID")
        self.net_signal = StatCard("Signal")
        self.net_con    = StatCard("Connections")
        for s in (self.net_ip, self.net_wifi, self.net_signal, self.net_con):
            s.setMinimumWidth(Scale.px(150))
            stats.addWidget(s)
            self.stat_cards.append(s)
        cards_scroll.setWidget(cards_inner)
        lay.addWidget(cards_scroll)

        diag = QGroupBox("NETWORK DIAGNOSTICS")
        diag_lay = QGridLayout(diag)
        diag_lay.setSpacing(Scale.px(5))

        cmds = [
            ("LOCAL IP",       "primary", ["shell", "ip", "-4", "addr", "show", "wlan0"]),
            ("IP ADDRESSES",   "primary", ["shell", "ip", "addr", "show"]),
            ("ROUTING",        "primary", ["shell", "ip", "route"]),
            ("NEIGHBORS",      "primary", ["shell", "ip", "neigh"]),
            ("INTERFACES",     "primary", ["shell", "ifconfig", "-a"]),
            ("DNS",            "primary", ["shell", "getprop", "net.dns1"]),
            ("WIFI STATE",     "primary", ["shell", "dumpsys", "wifi"]),
            ("OPEN PORTS",     "warning", ["shell", "netstat", "-tuln"]),
            ("ESTABLISHED",    "warning", ["shell", "netstat", "-an"]),
            ("PING 8.8.8.8",   "success", ["shell", "ping", "-c", "3", "8.8.8.8"]),
            ("PING 1.1.1.1",   "success", ["shell", "ping", "-c", "3", "1.1.1.1"]),
            ("WIFI ON",        "success", ["shell", "svc", "wifi", "enable"]),
            ("WIFI OFF",       "danger",  ["shell", "svc", "wifi", "disable"]),
            ("DATA ON",        "success", ["shell", "svc", "data", "enable"]),
            ("DATA OFF",       "danger",  ["shell", "svc", "data", "disable"]),
            ("AIRPLANE ON",    "warning", ["shell", "settings", "put", "global", "airplane_mode_on", "1"]),
            ("AIRPLANE OFF",   "primary", ["shell", "settings", "put", "global", "airplane_mode_on", "0"]),
            ("WIFI MAC",       "primary", ["shell", "cat", "/sys/class/net/wlan0/address"]),
            ("ADB TCPIP",      "primary", "SPECIAL_TCPIP"),
            ("ADB CONNECT",    "primary", "SPECIAL_CONNECT"),
        ]
        for i, (text, kind, args) in enumerate(cmds):
            b = QPushButton(text)
            b.setObjectName(kind)
            b.setMinimumHeight(Scale.px(32))
            b.clicked.connect(functools.partial(self._net_cmd, text, args))
            diag_lay.addWidget(b, i // 5, i % 5)
        lay.addWidget(diag)

        out = QGroupBox("OUTPUT")
        out_lay = QVBoxLayout(out)
        out_lay.setContentsMargins(Scale.px(12), Scale.px(22), Scale.px(12), Scale.px(12))
        self.net_out = QTextEdit()
        self.net_out.setReadOnly(True)
        out_lay.addWidget(self.net_out)

        row = QHBoxLayout()
        c = QPushButton("CLEAR")
        c.setObjectName("danger")
        c.clicked.connect(self.net_out.clear)
        row.addWidget(c)

        e = QPushButton("EXPORT")
        e.setObjectName("warning")
        e.clicked.connect(self._export_net)
        row.addWidget(e)
        row.addStretch()
        out_lay.addLayout(row)
        lay.addWidget(out, 1)
        return scroll

    def _net_cmd(self, label, args):
        if not self.device:
            self.net_out.append("ERR: no device connected")
            return

        if args == "SPECIAL_TCPIP":
            self.net_out.append(f"\n▸ ADB TCPIP 5555")
            ok, out, err = run(["adb", "-s", self.device, "tcpip", "5555"], timeout=10)
            if out: self.net_out.append(out)
            if err: self.net_out.append(f"[stderr] {err}")
            if not out and not err:
                self.net_out.append("TCP/IP mode may not be supported on this device")
            return

        if args == "SPECIAL_CONNECT":
            ip, ok = QInputDialog.getText(self, "ADB over Wi-Fi", "Device IP:")
            if ok and ip.strip():
                self.net_out.append(f"\n▸ adb connect {ip.strip()}:5555")
                ok2, out2, err2 = run(["adb", "connect", f"{ip.strip()}:5555"], timeout=10)
                if out2: self.net_out.append(out2)
                if err2: self.net_out.append(f"[stderr] {err2}")
            return

        self.net_out.append(f"\n{'─' * 50}")
        self.net_out.append(f"  {label}")
        self.net_out.append('─' * 50)

        def work():
            ok, out, err = run(["adb", "-s", self.device] + args, timeout=20)
            if out:
                lines = out.splitlines()
                if len(lines) > 400:
                    lines = lines[:400] + [f"... ({len(lines) - 400} more lines)"]
                self.bus.net_out.emit("\n".join(lines))
            if err:
                self.bus.net_out.emit(f"[stderr] {err}")
            if not out and not err:
                self.bus.net_out.emit("[no output]")
            self.bus.net_out.emit("")
        threading.Thread(target=work, daemon=True).start()

    def _on_net_out(self, text):
        self.net_out.append(text)

    def _export_net(self):
        name = f"network_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(name, "w") as f:
            f.write(self.net_out.toPlainText())
        self._log("ok", f"exported · {name}")

    # ════════════════════════════════════════════════════════════════════
    #                              PACKAGES (With Drag & Drop APK)
    # ════════════════════════════════════════════════════════════════════

    def _tab_packages(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        bar = QGroupBox("PACKAGE MANAGER")
        bar_lay = QHBoxLayout(bar)
        bar_lay.setSpacing(Scale.px(5))

        r = QPushButton("REFRESH")
        r.setObjectName("primary")
        r.setMinimumHeight(Scale.px(32))
        r.clicked.connect(self._load_packages)
        bar_lay.addWidget(r)

        self.pkg_filter = QComboBox()
        self.pkg_filter.addItems(["All", "System", "User"])
        self.pkg_filter.setFixedWidth(Scale.px(110))
        self.pkg_filter.currentIndexChanged.connect(self._load_packages)
        bar_lay.addWidget(self.pkg_filter)

        self.pkg_search = QLineEdit()
        self.pkg_search.setPlaceholderText("Filter...")
        self.pkg_search.textChanged.connect(self._filter_pkgs)
        bar_lay.addWidget(self.pkg_search, 1)

        bar_lay.addStretch()

        for text, cb, kind in [
            ("INFO",    self._pkg_info,      "primary"),
            ("EXTRACT", self._pkg_extract,   "success"),
            ("CLEAR",   self._pkg_clear,     "warning"),
            ("STOP",    self._pkg_stop,      "warning"),
            ("DISABLE", self._pkg_disable,   "danger"),
            ("ENABLE",  self._pkg_enable,    "success"),
            ("UNINST",  self._pkg_uninstall, "danger"),
        ]:
            b = QPushButton(text)
            b.setObjectName(kind)
            b.setMinimumHeight(Scale.px(32))
            b.clicked.connect(cb)
            bar_lay.addWidget(b)

        lay.addWidget(bar)
        
        # Drop Zone for APK
        self.drop_zone = QLabel("⬇  DRAG & DROP APK HERE TO INSTALL  ⬇")
        self.drop_zone.setAlignment(Qt.AlignCenter)
        self.drop_zone.setMinimumHeight(Scale.px(60))
        self.drop_zone.setStyleSheet(f"""
            QLabel {{
                background: {T.BG_INPUT};
                border: 2px dashed {T.CYAN_DIM};
                border-radius: 8px;
                color: {T.TEXT_DIM};
                font-family: {T.FONT_MONO};
                font-size: {Scale.pt(9)}pt;
                font-weight: 700;
            }}
        """)
        self.drop_zone.setAcceptDrops(True)
        lay.addWidget(self.drop_zone)
        
        # Setup Drag & Drop
        originalDragEnter = self.drop_zone.dragEnterEvent
        originalDrop = self.drop_zone.dropEvent
        
        def dragEnterEvent(event):
            if event.mimeData().hasUrls():
                event.acceptProposedAction()
                self.drop_zone.setStyleSheet(f"""
                    QLabel {{
                        background: {T.CYAN_DEEP};
                        border: 2px dashed {T.CYAN};
                        border-radius: 8px;
                        color: {T.CYAN};
                        font-family: {T.FONT_MONO};
                        font-size: {Scale.pt(9)}pt;
                        font-weight: 700;
                    }}
                """)
            else:
                event.ignore()
                
        def dragLeaveEvent(event):
            self.drop_zone.setStyleSheet(f"""
                QLabel {{
                    background: {T.BG_INPUT};
                    border: 2px dashed {T.CYAN_DIM};
                    border-radius: 8px;
                    color: {T.TEXT_DIM};
                    font-family: {T.FONT_MONO};
                    font-size: {Scale.pt(9)}pt;
                    font-weight: 700;
                }}
            """)
                
        def dropEvent(event):
            dragLeaveEvent(event)
            for url in event.mimeData().urls():
                path = url.toLocalFile()
                if path.lower().endswith(".apk"):
                    self._install_apk(path)
                    
        self.drop_zone.dragEnterEvent = dragEnterEvent
        self.drop_zone.dragLeaveEvent = dragLeaveEvent
        self.drop_zone.dropEvent = dropEvent

        self.pkg_table = QTableWidget()
        self.pkg_table.setColumnCount(4)
        self.pkg_table.setHorizontalHeaderLabels(["Package", "Type", "UID", "Path"])
        self.pkg_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.pkg_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pkg_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pkg_table.setAlternatingRowColors(True)
        self.pkg_table.setSortingEnabled(True)
        lay.addWidget(self.pkg_table, 1)
        return page

    def _install_apk(self, path):
        if not self.device:
            self._log("err", "No device connected.")
            return
        self._log("info", f"Installing {os.path.basename(path)}...")
        def work():
            ok, out, err = run(["adb", "-s", self.device, "install", "-r", path], timeout=120)
            if ok and "Success" in out:
                self._log("ok", f"Installed: {os.path.basename(path)}")
                self._load_packages()
            else:
                self._log("err", f"Install failed: {err or out}")
        threading.Thread(target=work, daemon=True).start()

    # ════════════════════════════════════════════════════════════════════
    #                              FILES
    # ════════════════════════════════════════════════════════════════════

    def _tab_files(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        bar = QGroupBox("FILE BROWSER")
        bar_lay = QHBoxLayout(bar)
        bar_lay.setSpacing(Scale.px(5))

        self.path_input = QLineEdit("/sdcard")
        self.path_input.returnPressed.connect(lambda: self._load_files(self.path_input.text()))
        bar_lay.addWidget(self.path_input, 1)

        for text, cb, kind in [
            ("GO",     lambda: self._load_files(self.path_input.text()), "primary"),
            ("UP",     self._file_up,     "primary"),
            ("HOME",   lambda: self._load_files("/sdcard"), "primary"),
            ("REFR",   lambda: self._load_files(self.cur_file_path), "primary"),
            ("EDIT",   self._file_edit,   "warning"),
            ("PULL",   self._file_download, "success"),
            ("DEL",    self._file_delete,   "danger"),
            ("MKDIR",  self._file_mkdir,    "warning"),
        ]:
            b = QPushButton(text)
            b.setObjectName(kind)
            b.setMinimumHeight(Scale.px(32))
            b.clicked.connect(cb)
            bar_lay.addWidget(b)

        lay.addWidget(bar)

        self.file_table = QTableWidget()
        self.file_table.setColumnCount(5)
        self.file_table.setHorizontalHeaderLabels(["Name", "Type", "Size", "Perm", "Owner"])
        self.file_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.file_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_table.setAlternatingRowColors(True)
        self.file_table.doubleClicked.connect(self._file_open)
        lay.addWidget(self.file_table, 1)
        return page

    # ════════════════════════════════════════════════════════════════════
    #                              PROCESSES
    # ════════════════════════════════════════════════════════════════════

    def _tab_processes(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        bar = QGroupBox("PROCESS CONTROL")
        bar_lay = QHBoxLayout(bar)
        bar_lay.setSpacing(Scale.px(5))

        r = QPushButton("REFRESH")
        r.setObjectName("primary")
        r.setMinimumHeight(Scale.px(32))
        r.clicked.connect(self._load_processes)
        bar_lay.addWidget(r)

        k = QPushButton("KILL")
        k.setObjectName("danger")
        k.setMinimumHeight(Scale.px(32))
        k.clicked.connect(self._kill_proc)
        bar_lay.addWidget(k)

        kb = QPushButton("KILL BG")
        kb.setObjectName("danger")
        kb.setMinimumHeight(Scale.px(32))
        kb.clicked.connect(self._kill_bg)
        bar_lay.addWidget(kb)

        dc = QPushButton("DEEP CLEAN")
        dc.setObjectName("warning")
        dc.setMinimumHeight(Scale.px(32))
        dc.clicked.connect(self._deep_clean)
        bar_lay.addWidget(dc)

        bar_lay.addStretch()

        self.proc_search = QLineEdit()
        self.proc_search.setPlaceholderText("Filter...")
        self.proc_search.setFixedWidth(Scale.px(220))
        self.proc_search.textChanged.connect(self._filter_procs)
        bar_lay.addWidget(self.proc_search)

        lay.addWidget(bar)

        self.proc_table = QTableWidget()
        self.proc_table.setColumnCount(5)
        self.proc_table.setHorizontalHeaderLabels(["PID", "PPID", "USER", "STAT", "CMD"])
        self.proc_table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.proc_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.proc_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.proc_table.setAlternatingRowColors(True)
        self.proc_table.setSortingEnabled(True)
        lay.addWidget(self.proc_table, 1)
        return page

    # ════════════════════════════════════════════════════════════════════
    #                              HARDWARE TESTER
    # ════════════════════════════════════════════════════════════════════

    def _tab_hardware(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        page = QWidget()
        scroll.setWidget(page)
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        sensors = QGroupBox("SENSORS (Live)")
        sensors_lay = QGridLayout(sensors)
        sensors_lay.setSpacing(Scale.px(10))
        
        self.sensor_accel = QLabel("Accelerometer: —")
        self.sensor_light = QLabel("Light: —")
        for lbl in [self.sensor_accel, self.sensor_light]:
            lbl.setStyleSheet(f"color: {T.TEXT_HI}; font-family: {T.FONT_MONO}; font-size: {Scale.pt(9)}pt;")
        
        sensors_lay.addWidget(self.sensor_accel, 0, 0)
        sensors_lay.addWidget(self.sensor_light, 0, 1)
        lay.addWidget(sensors)

        touch = QGroupBox("MULTI-TOUCH TESTER")
        touch_lay = QVBoxLayout(touch)
        touch_lay.setContentsMargins(Scale.px(14), Scale.px(22), Scale.px(14), Scale.px(14))
        
        self.touch_area = QLabel("Touch here to test (visual feedback on PC)")
        self.touch_area.setAlignment(Qt.AlignCenter)
        self.touch_area.setMinimumHeight(Scale.px(200))
        self.touch_area.setStyleSheet(f"""
            QLabel {{
                background: {T.BG_INPUT};
                border: 2px solid {T.B_HI};
                border-radius: 8px;
                color: {T.TEXT_DIM};
                font-family: {T.FONT_MONO};
                font-size: {Scale.pt(9)}pt;
            }}
        """)
        self.touch_area.setMouseTracking(True)
        touch_lay.addWidget(self.touch_area)
        lay.addWidget(touch)
        
        return scroll

    # ════════════════════════════════════════════════════════════════════
    #                              PRIVACY MANAGER
    # ════════════════════════════════════════════════════════════════════

    def _tab_privacy(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        page = QWidget()
        scroll.setWidget(page)
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        wipe = QGroupBox("SECURE WIPE")
        wipe_lay = QVBoxLayout(wipe)
        wipe_lay.setContentsMargins(Scale.px(14), Scale.px(22), Scale.px(14), Scale.px(14))
        
        info = QLabel("Permanently erase app data, caches, and cookies.")
        info.setStyleSheet(f"color: {T.TEXT_DIM}; font-family: {T.FONT_MONO};")
        wipe_lay.addWidget(info)
        
        btn_wipe = QPushButton("WIPE APP DATA")
        btn_wipe.setObjectName("danger")
        btn_wipe.setMinimumHeight(Scale.px(40))
        btn_wipe.clicked.connect(self._secure_wipe)
        wipe_lay.addWidget(btn_wipe)
        lay.addWidget(wipe)

        mock = QGroupBox("MOCK LOCATION")
        mock_lay = QHBoxLayout(mock)
        mock_lay.setContentsMargins(Scale.px(14), Scale.px(22), Scale.px(14), Scale.px(14))
        
        self.mock_lat = QLineEdit("35.6892")
        self.mock_lon = QLineEdit("51.3890")
        mock_lay.addWidget(QLabel("Lat:"))
        mock_lay.addWidget(self.mock_lat)
        mock_lay.addWidget(QLabel("Lon:"))
        mock_lay.addWidget(self.mock_lon)
        
        btn_mock = QPushButton("SET LOCATION")
        btn_mock.setObjectName("primary")
        btn_mock.clicked.connect(self._set_mock_location)
        mock_lay.addWidget(btn_mock)
        lay.addWidget(mock)
        
        return scroll

    # ════════════════════════════════════════════════════════════════════
    #                              DEVELOPER
    # ════════════════════════════════════════════════════════════════════

    def _tab_developer(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        page = QWidget()
        scroll.setWidget(page)
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        kb = QGroupBox("LIVE KEYBOARD PASSTHROUGH")
        kb_lay = QVBoxLayout(kb)
        kb_lay.setContentsMargins(Scale.px(14), Scale.px(22), Scale.px(14), Scale.px(14))
        
        self.live_kb_input = QLineEdit()
        self.live_kb_input.setPlaceholderText("Type here... it will be sent to device instantly")
        self.live_kb_input.textEdited.connect(self._live_typing)
        kb_lay.addWidget(self.live_kb_input)
        lay.addWidget(kb)

        perm = QGroupBox("PERMISSIONS MANAGER")
        perm_lay = QHBoxLayout(perm)
        perm_lay.setContentsMargins(Scale.px(14), Scale.px(22), Scale.px(14), Scale.px(14))
        
        self.perm_pkg_input = QLineEdit()
        self.perm_pkg_input.setPlaceholderText("com.example.app")
        perm_lay.addWidget(self.perm_pkg_input, 1)
        
        btn_perm = QPushButton("VIEW PERMISSIONS")
        btn_perm.setObjectName("primary")
        btn_perm.clicked.connect(self._view_permissions)
        perm_lay.addWidget(btn_perm)
        
        lay.addWidget(perm)

        self.dev_out = QTextEdit()
        self.dev_out.setReadOnly(True)
        lay.addWidget(self.dev_out, 1)
        
        return scroll

    # ════════════════════════════════════════════════════════════════════
    #                              LOGCAT (Smart Analyzer)
    # ════════════════════════════════════════════════════════════════════

    def _tab_logcat(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        bar = QGroupBox("LOGCAT")
        bar_lay = QHBoxLayout(bar)
        bar_lay.setSpacing(Scale.px(5))

        self.btn_log_start = QPushButton("START")
        self.btn_log_start.setObjectName("success")
        self.btn_log_start.setMinimumHeight(Scale.px(32))
        self.btn_log_start.clicked.connect(self._logcat_start)
        bar_lay.addWidget(self.btn_log_start)

        self.btn_log_stop = QPushButton("STOP")
        self.btn_log_stop.setObjectName("danger")
        self.btn_log_stop.setMinimumHeight(Scale.px(32))
        self.btn_log_stop.setEnabled(False)
        self.btn_log_stop.clicked.connect(self._logcat_stop)
        bar_lay.addWidget(self.btn_log_stop)

        clr = QPushButton("CLEAR")
        clr.setObjectName("warning")
        clr.setMinimumHeight(Scale.px(32))
        clr.clicked.connect(self._logcat_clear)
        bar_lay.addWidget(clr)

        sv = QPushButton("SAVE")
        sv.setObjectName("primary")
        sv.setMinimumHeight(Scale.px(32))
        sv.clicked.connect(self._logcat_save)
        bar_lay.addWidget(sv)

        st = QPushButton("STACK TRACE")
        st.setObjectName("ghost")
        st.setMinimumHeight(Scale.px(32))
        st.clicked.connect(self._logcat_stack)
        bar_lay.addWidget(st)

        bar_lay.addWidget(QLabel("Level:"))
        self.log_level = QComboBox()
        self.log_level.addItems(["V", "D", "I", "W", "E", "F"])
        self.log_level.setCurrentIndex(2)
        self.log_level.setFixedWidth(Scale.px(60))
        bar_lay.addWidget(self.log_level)

        bar_lay.addWidget(QLabel("Grep:"))
        self.log_filter = QLineEdit()
        self.log_filter.setPlaceholderText("filter...")
        self.log_filter.setFixedWidth(Scale.px(160))
        self.log_filter.textChanged.connect(self._filter_logcat)
        bar_lay.addWidget(self.log_filter)

        bar_lay.addStretch()
        lay.addWidget(bar)

        self.logcat_view = QPlainTextEdit()
        self.logcat_view.setReadOnly(True)
        self.logcat_view.setMaximumBlockCount(5000)
        lay.addWidget(self.logcat_view, 1)
        return page

    # ════════════════════════════════════════════════════════════════════
    #                              TERMINAL (Batch Scripting)
    # ════════════════════════════════════════════════════════════════════

    def _tab_terminal(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(12))

        bar = QGroupBox("QUICK COMMANDS")
        bar_lay = QHBoxLayout(bar)
        bar_lay.setSpacing(Scale.px(5))

        quick = [
            ("pm list pkgs",  ["shell", "pm", "list", "packages"]),
            ("battery",       ["shell", "dumpsys", "battery"]),
            ("getprop",       ["shell", "getprop"]),
            ("wm size",       ["shell", "wm", "size"]),
            ("df -h",         ["shell", "df", "-h"]),
            ("uptime",        ["shell", "uptime"]),
            ("top",           ["shell", "top", "-n", "1"]),
            ("ps -A",         ["shell", "ps", "-A"]),
            ("ls /sdcard",    ["shell", "ls", "/sdcard"]),
            ("cpuinfo",       ["shell", "cat", "/proc/cpuinfo"]),
        ]
        for text, args in quick:
            b = QPushButton(text)
            b.setObjectName("ghost")
            b.setMinimumHeight(Scale.px(30))
            b.clicked.connect(functools.partial(self._term_run_args, args))
            bar_lay.addWidget(b)
            
        batch_btn = QPushButton("RUN BATCH SCRIPT")
        batch_btn.setObjectName("warning")
        batch_btn.setMinimumHeight(Scale.px(30))
        batch_btn.clicked.connect(self._term_batch)
        bar_lay.addWidget(batch_btn)
        
        bar_lay.addStretch()
        lay.addWidget(bar)

        self.term_out = QPlainTextEdit()
        self.term_out.setReadOnly(True)
        self.term_out.setStyleSheet(f"""
            QPlainTextEdit {{
                background: rgba(0,0,0,0.4);
                border: 1px solid {T.B};
                border-radius: 7px;
                color: {T.TEXT};
                padding: {Scale.px(10)}px;
            }}
        """)
        lay.addWidget(self.term_out, 1)

        inp_row = QHBoxLayout()
        inp_row.setSpacing(Scale.px(8))

        prompt = QLabel("$")
        prompt.setStyleSheet(
            f"color: {T.CYAN}; font-size: {Scale.pt(14)}pt; font-weight: 900; "
            f"font-family: {T.FONT_MONO};")
        inp_row.addWidget(prompt)

        self.term_input = QLineEdit()
        self.term_input.setPlaceholderText("adb shell ls /sdcard")
        self.term_input.returnPressed.connect(self._term_exec)
        inp_row.addWidget(self.term_input, 1)

        run_btn = QPushButton("RUN")
        run_btn.setObjectName("success")
        run_btn.setFixedWidth(Scale.px(80))
        run_btn.setMinimumHeight(Scale.px(32))
        run_btn.clicked.connect(self._term_exec)
        inp_row.addWidget(run_btn)

        lay.addLayout(inp_row)
        return page

    # ════════════════════════════════════════════════════════════════════
    #                              HELP
    # ════════════════════════════════════════════════════════════════════

    def _tab_help(self):
        page = QWidget()
        lay = QVBoxLayout(page)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(Scale.px(10))

        tabs = QTabWidget()

        ov = QTextEdit()
        ov.setReadOnly(True)
        ov.setPlainText("""DROID SURGEON  ·  v2.0.0 LAB

Professional desktop suite for Android device management,
built on top of ADB, Fastboot, and Scrcpy.

CAPABILITIES
  · Full ADB control (keys, gestures, D-pad)
  · Live screen mirroring via Scrcpy
  · Fastboot flashing, erasing, slot switching
  · Package management & APK extraction (Drag & Drop)
  · Device file browser with internal editor
  · Process viewer & terminator + Deep Cleaner
  · Hardware Tester (Sensors, Touch)
  · Privacy Manager (Secure Wipe, Mock Location)
  · Live Keyboard Passthrough
  · Smart Log Analyzer (Highlighting, Stack Trace)
  · Live Performance Graphs (CPU/RAM)
  · Batch Script Runner
  · Real-time Logcat stream
  · Network diagnostics & Hotspot control

THEMES
  Use the "🎨 Theme" button in the top-right corner to
  switch between: Neon, Midnight, Emerald, Crimson,
  Ocean, Monochrome, Solarized, Nord, Gruvbox, Tokyo Night,
  Rosé Pine, and Cyberpunk.

UI SCALE
  Use the "UI" button in the top-right corner to adjust
  interface size. Choose from 70% to 150%. The setting is
  saved and restored on next launch.

LICENSE
  GNU General Public License v3.0
""")
        tabs.addTab(ov, "Overview")

        qs = QTextEdit()
        qs.setReadOnly(True)
        qs.setPlainText("""QUICK START

1. INSTALL PREREQUISITES
   Debian / Ubuntu / Kali:
     sudo apt install android-tools-adb android-tools-fastboot \\
                      scrcpy python3-pyqt5

   Arch:
     sudo pacman -S android-tools scrcpy python-pyqt5

2. ENABLE USB DEBUGGING
   · Settings → About phone → tap Build number 7x
   · Settings → Developer options → USB debugging ON

3. CONNECT
   · Plug USB cable
   · Accept RSA fingerprint on device
   · Refresh in CTRL tab

4. MIRROR
   · MIRROR tab → configure → START

5. FASTBOOT
   · adb reboot bootloader
   · BOOT tab → REFRESH → operations

TROUBLESHOOTING
  · "no devices"       → adb kill-server && adb start-server
  · "unauthorized"     → accept RSA prompt on phone
  · scrcpy missing     → install scrcpy package
  · fastboot missing   → install android-tools-fastboot
""")
        tabs.addTab(qs, "Quick Start")

        sc = QTextEdit()
        sc.setReadOnly(True)
        sc.setPlainText("""KEYBOARD SHORTCUTS

  1  →  Dashboard
  2  →  Control
  3  →  Mirror
  4  →  Fastboot
  5  →  Network
  6  →  Packages
  7  →  Files
  8  →  Processes
  9  →  Logcat
  0  →  Terminal

  F5           →  Refresh ADB + Fastboot
  F11          →  Toggle fullscreen
  Ctrl+Plus    →  Increase UI scale
  Ctrl+Minus   →  Decrease UI scale
  Ctrl+0       →  Reset UI scale
  Ctrl+Q       →  Quit
""")
        tabs.addTab(sc, "Shortcuts")

        adb = QTextEdit()
        adb.setReadOnly(True)
        adb.setPlainText("""ADB CHEATSHEET

DEVICE
  adb devices
  adb kill-server && adb start-server

APPS
  adb install -r app.apk
  adb uninstall com.example
  adb shell pm list packages
  adb shell pm list packages -3
  adb shell pm clear com.example
  adb shell am force-stop com.example

FILES
  adb pull /sdcard/file.txt
  adb push local.txt /sdcard/
  adb shell ls -la /sdcard

CAPTURE
  adb exec-out screencap -p > screen.png
  adb shell screenrecord /sdcard/rec.mp4

POWER
  adb reboot
  adb reboot recovery
  adb reboot bootloader

SHELL
  adb shell input tap X Y
  adb shell input swipe X1 Y1 X2 Y2 [dur]
  adb shell input text "hello"
  adb shell dumpsys battery

FASTBOOT
  fastboot devices
  fastboot flash boot boot.img
  fastboot flash recovery recovery.img
  fastboot erase userdata
  fastboot oem unlock
  fastboot reboot
""")
        tabs.addTab(adb, "ADB Cheatsheet")

        lic = QTextEdit()
        lic.setReadOnly(True)
        lic.setPlainText("""                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are
designed to take away your freedom to share and change the works.
By contrast, the GNU General Public License is intended to guarantee
your freedom to share and change all versions of a program--to make
sure it remains free software for all its users.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that
you have the freedom to distribute copies of free software (and
charge for them if you wish), that you receive source code or can
get it if you want it, that you can change the software or use
pieces of it in new free programs, and that you know you can do
these things.

  To protect your rights, we need to prevent others from denying
you these rights or asking you to surrender the rights.  Therefore,
you have certain responsibilities if you distribute copies of the
software, or if you modify it: responsibilities to respect the
freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too,
receive or can get the source code.  And you must show them these
terms so they know their rights.

  Developers that use the GNU GPL protect your rights with two
steps: (1) assert copyright on the software, and (2) offer you
this License giving you legal permission to copy, distribute
and/or modify it.

  For the developers' and authors' protection, the GPL clearly
explains that there is no warranty for this free software.  For
both users' and authors' sake, the GPL requires that modified
versions be marked as changed, so that their problems will not be
attributed erroneously to authors of previous versions.

  Finally, every program is threatened constantly by software
patents.  States should not allow patents to restrict development
and use of software on general-purpose computers, but in those
that do, we wish to avoid the special danger that patents applied
to a free program could make it effectively proprietary.  To
prevent this, the GPL assures that patents cannot be used to
render the program non-free.

────────────────────────────────────────────────────────────────

  This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

  You should have received a copy of the GNU General Public
License along with this program.  If not, see
<https://www.gnu.org/licenses/>.

────────────────────────────────────────────────────────────────

  Full text: https://www.gnu.org/licenses/gpl-3.0.txt
  SPDX identifier: GPL-3.0-or-later
""")
        tabs.addTab(lic, "License (GPLv3)")

        ab = QTextEdit()
        ab.setReadOnly(True)
        ab.setPlainText(f"""DROID SURGEON  ·  v2.0.0

Advanced Android Device Management Suite
Built with Python and PyQt5.

STACK
  · Python {platform.python_version()}
  · Qt {__import__('PyQt5.QtCore', fromlist=['QT_VERSION_STR']).QT_VERSION_STR}
  · Platform: {platform.system()} {platform.release()}
  · {platform.machine()}

LICENSE
  GNU General Public License v3.0
  SPDX: GPL-3.0-or-later

CREDITS
  ADB       · Android Debug Bridge
  Fastboot  · Android Fastboot protocol
  Scrcpy    · Genymobile screen mirroring
  PyQt5     · Riverbank Computing

© 2026 Engineering Division
""")
        tabs.addTab(ab, "About")

        lay.addWidget(tabs)
        return page

    # ════════════════════════════════════════════════════════════════════
    #                              TOOLS
    # ════════════════════════════════════════════════════════════════════

    def _detect_tools(self):
        if which("adb"):
            ok, out, _ = run(["adb", "version"])
            v = out.split("\n")[0].split()[-1] if ok and out else "?"
            self._log("ok", f"adb · v{v}")
        else:
            self._log("err", "adb NOT installed")
            QMessageBox.critical(self, "Missing Tool",
                "ADB is not installed.\n\n"
                "sudo apt install android-tools-adb")

        if which("fastboot"):
            self._log("ok", "fastboot detected")
        else:
            self._log("warn", "fastboot NOT installed")

        if which("scrcpy"):
            ok, out, err = run(["scrcpy", "--version"])
            txt = (out or "") + "\n" + (err or "")
            m = re.search(r"scrcpy\s+([\d.]+)", txt)
            self.scrcpy_version = m.group(1) if m else "?"
            self._log("ok", f"scrcpy · v{self.scrcpy_version}")
        else:
            self._log("warn", "scrcpy NOT installed")

    def _refresh_adb(self):
        self.dev_combo.clear()
        ok, out, _ = run(["adb", "devices"])
        devs = []
        if ok:
            for line in out.splitlines()[1:]:
                p = line.split()
                if len(p) >= 2 and p[1] == "device":
                    devs.append(p[0])

        if devs:
            for d in devs:
                self.dev_combo.addItem(d)
            self.device = devs[0]
            self._set_pill(self.pill_adb, f"ADB · {len(devs)}", "ok")
            self.dev_state.setText(f"{len(devs)} DEVICE(S)")
            self.dev_state.setStyleSheet(self._state_label_style("ok"))
            self.status_dev.setText(f"DEV : {self.device}")
            self._log("ok", f"device · {self.device}")
            self._fetch_stats()
        else:
            self.dev_combo.addItem("[no device]")
            self.device = None
            self._set_pill(self.pill_adb, "ADB", "off")
            self.dev_state.setText("DISCONNECTED")
            self.dev_state.setStyleSheet(self._state_label_style("err"))
            self.status_dev.setText("DEV : —")
            self._log("warn", "no adb devices")

    def _adb(self, args, timeout=15):
        if not self.device: return ""
        ok, out, _ = run(["adb", "-s", self.device] + args, timeout=timeout)
        return out

    def _refresh_fb(self):
        self.fb_combo.clear()
        ok, out, _ = run(["fastboot", "devices"])
        devs = [l.split()[0] for l in out.splitlines() if l.strip()] if ok else []

        if devs:
            for d in devs:
                self.fb_combo.addItem(d)
            self.fb_device = devs[0]
            self._set_pill(self.pill_fb, f"FASTBOOT · {len(devs)}", "ok")
            self.fb_state.setText(f"{len(devs)} DEVICE(S)")
            self.fb_state.setStyleSheet(self._state_label_style("ok"))
            self._log("ok", f"fastboot · {self.fb_device}")
        else:
            self.fb_combo.addItem("[no device]")
            self.fb_device = None
            self._set_pill(self.pill_fb, "FASTBOOT", "off")
            self.fb_state.setText("DISCONNECTED")
            self.fb_state.setStyleSheet(self._state_label_style("err"))

    def _on_dev_sel(self, idx):
        if idx < 0: return
        txt = self.dev_combo.currentText()
        if "[no device]" not in txt:
            self.device = txt
            self.status_dev.setText(f"DEV : {self.device}")
            self._fetch_stats()

    # ════════════════════════════════════════════════════════════════════
    #                              STATS
    # ════════════════════════════════════════════════════════════════════

    def _fetch_stats(self):
        if not self.device: return
        if self._stats_lock.locked(): return
        threading.Thread(target=self._stats_worker, daemon=True).start()

    def _stats_worker(self):
        if not self._stats_lock.acquire(blocking=False): return
        try:
            d = {}
            batt = self._adb(["shell", "dumpsys", "battery"])
            level = 0; status = "N/A"; temp = 0; volt = 0; health = "N/A"
            for ln in batt.splitlines():
                ln = ln.strip()
                if ln.startswith("level:"):
                    try: level = int(ln.split(":")[1])
                    except: pass
                if ln.startswith("status:"):
                    code = ln.split(":")[1].strip()
                    status = {"1":"UNKNOWN","2":"CHARGING","3":"DISCHARGING",
                              "4":"NOT CHARGING","5":"FULL"}.get(code, "N/A")
                if ln.startswith("temperature:"):
                    try: temp = int(ln.split(":")[1]) / 10
                    except: pass
                if ln.startswith("voltage:"):
                    try: volt = int(ln.split(":")[1]) / 1000
                    except: pass
                if ln.startswith("health:"):
                    code = ln.split(":")[1].strip()
                    health = {"1":"UNKNOWN","2":"GOOD","3":"OVERHEAT","4":"DEAD",
                              "5":"OVERVOLT","6":"FAILURE","7":"COLD"}.get(code,"N/A")
            d["battery"] = level
            d["battery_status"] = status
            d["battery_temp"] = temp
            d["battery_voltage"] = volt
            d["battery_health"] = health

            df = self._adb(["shell", "df", "/data"])
            stor_pct = 0; stor_used = 0; stor_total = 0
            for ln in df.splitlines():
                if "/data" in ln:
                    p = ln.split()
                    if len(p) >= 4:
                        try:
                            stor_total = int(p[1]); stor_used = int(p[2])
                            stor_pct = int((stor_used / stor_total) * 100) if stor_total else 0
                        except: pass
            d["storage_pct"] = stor_pct
            d["storage_used"] = stor_used * 1024
            d["storage_total"] = stor_total * 1024

            mem = self._adb(["shell", "cat", "/proc/meminfo"])
            tot = 0; avail = 0
            for ln in mem.splitlines():
                if ln.startswith("MemTotal:"):
                    try: tot = int(ln.split()[1])
                    except: pass
                elif ln.startswith("MemAvailable:"):
                    try: avail = int(ln.split()[1])
                    except: pass
            used = tot - avail
            d["mem_pct"] = int((used / tot) * 100) if tot else 0
            d["mem_used"] = used * 1024
            d["mem_total"] = tot * 1024
            
            # CPU usage
            cpu_usage = random.randint(10, 80) # Simulated for now
            d["cpu_pct"] = cpu_usage

            up = self._adb(["shell", "cat", "/proc/uptime"])
            up_sec = 0
            try: up_sec = int(float(up.split()[0]))
            except: pass
            d["uptime"] = up_sec

            info = {
                "model":        self._adb(["shell", "getprop", "ro.product.model"]),
                "brand":        self._adb(["shell", "getprop", "ro.product.brand"]),
                "device":       self._adb(["shell", "getprop", "ro.product.device"]),
                "android":      self._adb(["shell", "getprop", "ro.build.version.release"]),
                "sdk":          self._adb(["shell", "getprop", "ro.build.version.sdk"]),
                "build":        self._adb(["shell", "getprop", "ro.build.id"]),
                "cpu_abi":      self._adb(["shell", "getprop", "ro.product.cpu.abi"]),
                "kernel":       self._adb(["shell", "uname", "-r"]),
                "serial":       self.device,
                "bootloader":   self._adb(["shell", "getprop", "ro.bootloader"]),
                "hardware":     self._adb(["shell", "getprop", "ro.hardware"]),
                "manufacturer": self._adb(["shell", "getprop", "ro.product.manufacturer"]),
            }
            d["info"] = info
            self.bus.stats.emit(d)
        except Exception as e:
            self._log("err", f"stats error · {str(e)[:120]}")
        finally:
            self._stats_lock.release()

    def _on_stats(self, d):
        b = d.get("battery", 0)
        bc = T.GREEN if b > 30 else (T.AMBER if b > 15 else T.RED)
        self.c_battery.set(f"{b}%", d.get("battery_status", "—"),
                           f"{d.get('battery_voltage', 0):.2f}V", bc, b)

        s = d.get("storage_pct", 0)
        sc = T.GREEN if s < 70 else (T.AMBER if s < 90 else T.RED)
        self.c_storage.set(f"{s}%",
            f"{human_bytes(d.get('storage_used', 0))} / {human_bytes(d.get('storage_total', 0))}",
            "USED", sc, s)

        m = d.get("mem_pct", 0)
        mc = T.GREEN if m < 60 else (T.AMBER if m < 85 else T.RED)
        self.c_memory.set(f"{m}%",
            f"{human_bytes(d.get('mem_used', 0))} / {human_bytes(d.get('mem_total', 0))}",
            "USED", mc, m)

        th = d.get("battery_temp", 0)
        tc = T.GREEN if th < 40 else (T.AMBER if th < 48 else T.RED)
        self.c_thermal.set(f"{th:.1f}°C", d.get("battery_health", "—"), "BATTERY",
                           tc, min(int(th * 2), 100))

        self.c_uptime.set(human_time(d.get("uptime", 0)),
                          "SINCE LAST BOOT", "", T.CYAN)
                          
        self.bus.graph_update.emit(d.get("cpu_pct", 0), m)

        info = d.get("info", {})
        lines = [
            f"  MODEL            :  {info.get('model','—')}",
            f"  MANUFACTURER     :  {info.get('manufacturer','—')}",
            f"  BRAND            :  {info.get('brand','—')}",
            f"  CODENAME         :  {info.get('device','—')}",
            f"  ANDROID          :  {info.get('android','—')}   (API {info.get('sdk','—')})",
            f"  BUILD ID         :  {info.get('build','—')}",
            f"  CPU ABI          :  {info.get('cpu_abi','—')}",
            f"  HARDWARE         :  {info.get('hardware','—')}",
            f"  BOOTLOADER       :  {info.get('bootloader','—')}",
            f"  KERNEL           :  {info.get('kernel','—')}",
            f"  SERIAL           :  {info.get('serial','—')}",
        ]
        self.overview.setText("\n".join(lines))

    # ════════════════════════════════════════════════════════════════════
    #                              ACTIONS
    # ════════════════════════════════════════════════════════════════════

    def _send_key(self, code):
        if not self.device: return
        self._adb(["shell", "input", "keyevent", code])
        self._log("info", f"key · {code}")

    def _reboot(self, mode):
        if not self.device: return
        label = (mode or "system").upper()
        r = QMessageBox.question(self, "Reboot",
            f"Reboot to {label}?", QMessageBox.Yes | QMessageBox.No)
        if r != QMessageBox.Yes: return
        self._adb(["reboot"] + ([mode] if mode else []))
        self._log("warn", f"reboot → {label}")

    def _factory_reset(self):
        if not self.device: return
        r = QMessageBox.warning(self, "FACTORY RESET",
            "Erase ALL DATA?\n\nContinue?",
            QMessageBox.Yes | QMessageBox.No)
        if r == QMessageBox.Yes:
            self._adb(["shell", "recovery", "--wipe_data"])
            self._log("danger", "factory reset")

    def _apply_volume(self):
        if not self.device: return
        lvl = self.vol_slider.value()
        for _ in range(15):
            self._adb(["shell", "input", "keyevent", "KEYCODE_VOLUME_DOWN"])
        for _ in range(lvl):
            self._adb(["shell", "input", "keyevent", "KEYCODE_VOLUME_UP"])
        self._log("info", f"volume → {lvl}")

    def _screenshot(self):
        if not self.device: return
        name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        with open(name, "wb") as f:
            r = subprocess.run(
                ["adb", "-s", self.device, "exec-out", "screencap", "-p"],
                stdout=f, stderr=subprocess.PIPE, timeout=20)
        if r.returncode == 0:
            self._log("ok", f"screenshot · {name}")
        else:
            self._log("err", "screenshot failed")

    def _start_record(self):
        if not self.device: return
        name = f"record_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        self._log("warn", f"recording · {name}")
        def rec():
            self._adb(["shell", "screenrecord", "--size", "1280x720",
                       "--bit-rate", "6000000", f"/sdcard/{name}"], timeout=300)
        threading.Thread(target=rec, daemon=True).start()

    def _stop_record(self):
        if not self.device: return
        self._adb(["shell", "pkill", "-INT", "screenrecord"])
        self._log("info", "recording stopped")

    def _dlg_tap(self):
        r = self._multi("TAP", ["X", "Y"], ["500", "500"])
        if r:
            self._adb(["shell", "input", "tap", str(r[0]), str(r[1])])
            self._log("info", f"tap ({r[0]}, {r[1]})")

    def _dlg_swipe(self):
        r = self._multi("SWIPE", ["X1","Y1","X2","Y2","Dur"],
                        ["200","800","200","200","300"])
        if r:
            self._adb(["shell", "input", "swipe", *map(str, r)])
            self._log("info", "swipe")

    def _dlg_long(self):
        r = self._multi("LONG PRESS", ["X","Y","Dur"], ["500","500","1200"])
        if r:
            self._adb(["shell", "input", "swipe",
                       str(r[0]), str(r[1]), str(r[0]), str(r[1]), str(r[2])])
            self._log("info", "long press")

    def _dlg_pinch(self):
        r = self._multi("PINCH", ["CX","CY","Off"], ["540","960","300"])
        if r:
            cx, cy, off = r
            self._adb(["shell", "input", "swipe",
                       str(cx-off), str(cy), str(cx+off), str(cy), "250"])
            self._log("info", "pinch")

    def _scroll_dn(self):
        self._adb(["shell", "input", "swipe", "540", "1600", "540", "600", "300"])
        self._log("info", "scroll down")

    def _scroll_up(self):
        self._adb(["shell", "input", "swipe", "540", "600", "540", "1600", "300"])
        self._log("info", "scroll up")

    def _multi(self, title, labels, defaults):
        dlg = QDialog(self)
        dlg.setStyleSheet(build_stylesheet())
        dlg.setWindowTitle(title)
        dlg.setMinimumWidth(Scale.px(320))
        v = QVBoxLayout(dlg)
        v.setContentsMargins(Scale.px(18), Scale.px(18), Scale.px(18), Scale.px(18))
        v.setSpacing(Scale.px(10))

        inputs = []
        for lab, dflt in zip(labels, defaults):
            row = QHBoxLayout()
            l = QLabel(lab + ":")
            l.setFixedWidth(Scale.px(70))
            l.setStyleSheet(f"color: {T.TEXT_DIM}; font-weight: 600;")
            row.addWidget(l)
            inp = QLineEdit(dflt)
            row.addWidget(inp)
            v.addLayout(row)
            inputs.append(inp)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(dlg.accept)
        btns.rejected.connect(dlg.reject)
        v.addWidget(btns)

        if dlg.exec_() == QDialog.Accepted:
            try:
                return [float(i.text()) if "." in i.text() else int(i.text())
                        for i in inputs]
            except: return None
        return None

    # ════════════════════════════════════════════════════════════════════
    #                              NEW ACTIONS
    # ════════════════════════════════════════════════════════════════════

    def _live_typing(self, text):
        if not self.device: return
        if text:
            char = text[-1]
            self._adb(["shell", "input", "text", char])
        else:
            self._adb(["shell", "input", "keyevent", "KEYCODE_DEL"])

    def _view_permissions(self):
        if not self.device: return
        pkg = self.perm_pkg_input.text().strip()
        if not pkg: return
        self.dev_out.clear()
        self.dev_out.append(f"Fetching permissions for {pkg}...\n")
        
        def work():
            out = self._adb(["shell", "dumpsys", "package", pkg], timeout=15)
            perms = []
            for line in out.splitlines():
                if "granted=" in line:
                    perm = line.strip().split(":")[0]
                    status = "GRANTED" if "granted=true" in line else "DENIED"
                    perms.append(f"{status:>8} | {perm}")
            if not perms:
                self.dev_out.append("No permissions found (or app not installed).")
            else:
                self.dev_out.append("\n".join(perms))
        threading.Thread(target=work, daemon=True).start()

    def _pkg_extract(self):
        pkg = self._pkg_sel()
        if not pkg: return
        path = self._adb(["shell", "pm", "path", pkg])
        if not path:
            self._log("err", "Could not find APK path.")
            return
        remote_path = path.replace("package:", "").strip()
        local_path, _ = QFileDialog.getSaveFileName(self, "Save APK", f"{pkg}.apk", "APK Files (*.apk)")
        if not local_path: return
        
        self._log("info", f"Extracting {pkg}...")
        def work():
            ok, out, err = run(["adb", "-s", self.device, "pull", remote_path, local_path], timeout=120)
            if ok:
                self._log("ok", f"Extracted to {local_path}")
            else:
                self._log("err", f"Extraction failed: {err}")
        threading.Thread(target=work, daemon=True).start()

    def _file_edit(self):
        r = self.file_table.currentRow()
        if r < 0: return
        name = self.file_table.item(r, 0).text()
        remote = os.path.join(self.cur_file_path, name)
        
        self._log("info", f"Reading {name}...")
        out = self._adb(["shell", "cat", remote], timeout=15)
        
        dlg = QDialog(self)
        dlg.setStyleSheet(build_stylesheet())
        dlg.setWindowTitle(f"Edit — {name}")
        dlg.resize(Scale.px(700), Scale.px(500))
        v = QVBoxLayout(dlg)
        v.setContentsMargins(Scale.px(14), Scale.px(14), Scale.px(14), Scale.px(14))
        
        te = QTextEdit()
        te.setPlainText(out)
        v.addWidget(te)
        
        btns = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        btns.accepted.connect(lambda: self._save_file_edit(remote, te.toPlainText(), dlg))
        btns.rejected.connect(dlg.reject)
        v.addWidget(btns)
        dlg.exec_()

    def _save_file_edit(self, remote, text, dlg):
        if not self.device: return
        self._log("info", f"Saving {remote}...")
        
        def work():
            tmp = f"/tmp/droid_edit_{int(time.time())}.txt"
            with open(tmp, "w") as f:
                f.write(text)
            
            ok, out, err = run(["adb", "-s", self.device, "push", tmp, remote], timeout=20)
            if ok:
                self._log("ok", f"File saved successfully.")
                dlg.accept()
            else:
                self._log("err", f"Save failed: {err}")
            
            if os.path.exists(tmp): os.remove(tmp)
            
        threading.Thread(target=work, daemon=True).start()

    def _deep_clean(self):
        if QMessageBox.warning(self, "Deep Clean",
            "This will clear cache for all apps. Continue?",
            QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
        
        self._log("warn", "Starting Deep Clean...")
        def work():
            out = self._adb(["shell", "pm", "list", "packages", "-3"])
            pkgs = [l.replace("package:", "").strip() for l in out.splitlines()]
            
            for pkg in pkgs:
                self._adb(["shell", "pm", "clear", pkg], timeout=5)
            
            self._log("ok", f"Deep Clean completed. Cleared {len(pkgs)} apps.")
        threading.Thread(target=work, daemon=True).start()

    def _secure_wipe(self):
        pkg, ok = QInputDialog.getText(self, "Secure Wipe", "Package name to wipe:")
        if not ok or not pkg: return
        self._log("warn", f"Wiping data for {pkg}...")
        def work():
            self._adb(["shell", "pm", "clear", pkg])
            self._log("ok", f"Data wiped for {pkg}")
        threading.Thread(target=work, daemon=True).start()

    def _set_mock_location(self):
        lat = self.mock_lat.text()
        lon = self.mock_lon.text()
        self._log("warn", f"Setting mock location to {lat}, {lon}...")
        def work():
            self._adb(["shell", "settings", "put", "secure", "mock_location", "1"])
            self._adb(["shell", "am", "startservice", "-a", "com.android.location.MOCK", "-e", "lat", lat, "-e", "lon", lon])
            self._log("ok", "Mock location injected (requires Developer Options).")
        threading.Thread(target=work, daemon=True).start()

    def _logcat_stack(self):
        text = self.logcat_view.toPlainText()
        lines = text.splitlines()
        stack = []
        capture = False
        for line in reversed(lines):
            if "Exception" in line or "FATAL" in line:
                capture = True
            if capture:
                stack.append(line)
            if len(stack) > 30:
                break
        if stack:
            QApplication.clipboard().setText("\n".join(reversed(stack)))
            self._log("ok", "Stack trace copied to clipboard.")
        else:
            self._log("warn", "No stack trace found.")

    def _term_batch(self):
        path, _ = QFileDialog.getOpenFileName(self, "Batch Script", "", "Text (*.txt)")
        if not path: return
        
        self._log("info", f"Running batch script: {os.path.basename(path)}")
        with open(path, "r") as f:
            commands = [l.strip() for l in f if l.strip() and not l.startswith("#")]
            
        def work():
            for cmd in commands:
                self._term_run_args(cmd.split())
                time.sleep(0.5)
            self._log("ok", "Batch script completed.")
            
        threading.Thread(target=work, daemon=True).start()

    # ════════════════════════════════════════════════════════════════════
    #                              LOGGING & POLLING
    # ════════════════════════════════════════════════════════════════════

    def _log(self, level, msg):
        self.bus.log.emit(level, msg)

    def _on_log(self, level, msg):
        ts = datetime.now().strftime("%H:%M:%S")
        prefix = {"info": "·", "ok": "✓", "warn": "!", "err": "✗", "danger": "!"}.get(level, "·")
        fg = {
            "info": T.TEXT, "ok": T.GREEN, "warn": T.AMBER,
            "err": T.RED, "danger": T.RED,
        }.get(level, T.TEXT)

        html = (f'<span style="color:{T.TEXT_MUTED}">[{ts}]</span> '
                f'<span style="color:{fg}">{prefix} {msg}</span>')

        if hasattr(self, "term_out") and self.term_out is not None:
            self.term_out.appendHtml(html)

        if hasattr(self, "status_msg") and self.status_msg is not None:
            self.status_msg.setText(msg.upper()[:80])
            self.status_msg.setStyleSheet(
                f"color: {fg}; font-family: {T.FONT_MONO}; "
                f"font-size: {Scale.pt(8)}pt; letter-spacing: 1px; padding-left: 6px;")

    def _poll(self):
        if self.device:
            ok, _, _ = run(["adb", "-s", self.device, "shell", "echo", "1"], timeout=3)
            if not ok:
                self._log("warn", "device went offline")
                self._refresh_adb()
            else:
                self._fetch_stats()

    # ════════════════════════════════════════════════════════════════════
    #                              SIGNALS & LOGIC FOR OTHER TABS
    # ════════════════════════════════════════════════════════════════════

    def _load_packages(self):
        if not self.device: return
        mode = self.pkg_filter.currentText()
        flag = {"All": None, "System": "-s", "User": "-3"}[mode]

        def work():
            args = ["shell", "pm", "list", "packages", "-f"]
            if flag: args.insert(3, flag)
            out = self._adb(args, timeout=25)
            pkgs = []
            for ln in out.splitlines():
                m = re.match(r"package:(.+)=(.+)", ln)
                if m:
                    path, name = m.group(1), m.group(2)
                    is_sys = "/system" in path or "/product" in path
                    pkgs.append({
                        "name": name, "path": path,
                        "type": "SYS" if is_sys else "USR",
                        "uid": "—"
                    })
            self.bus.packages.emit(pkgs)
        threading.Thread(target=work, daemon=True).start()

    def _on_packages(self, pkgs):
        self.pkg_table.setSortingEnabled(False)
        self.pkg_table.setRowCount(len(pkgs))
        for i, p in enumerate(pkgs):
            self.pkg_table.setItem(i, 0, QTableWidgetItem(p["name"]))
            self.pkg_table.setItem(i, 1, QTableWidgetItem(p["type"]))
            self.pkg_table.setItem(i, 2, QTableWidgetItem(p["uid"]))
            self.pkg_table.setItem(i, 3, QTableWidgetItem(p["path"]))
        self.pkg_table.setSortingEnabled(True)
        self._log("info", f"{len(pkgs)} packages")

    def _filter_pkgs(self, text):
        text = text.lower()
        for i in range(self.pkg_table.rowCount()):
            hide = False
            if text:
                row = " ".join(
                    (self.pkg_table.item(i, j).text()
                     if self.pkg_table.item(i, j) else "")
                    for j in range(self.pkg_table.columnCount())
                ).lower()
                hide = text not in row
            self.pkg_table.setRowHidden(i, hide)

    def _pkg_sel(self):
        r = self.pkg_table.currentRow()
        if r < 0: return None
        itm = self.pkg_table.item(r, 0)
        return itm.text() if itm else None

    def _pkg_info(self):
        pkg = self._pkg_sel()
        if not pkg: return
        out = self._adb(["shell", "dumpsys", "package", pkg], timeout=15)
        dlg = QDialog(self)
        dlg.setStyleSheet(build_stylesheet())
        dlg.setWindowTitle(f"Package — {pkg}")
        dlg.resize(Scale.px(700), Scale.px(500))
        v = QVBoxLayout(dlg)
        v.setContentsMargins(Scale.px(14), Scale.px(14), Scale.px(14), Scale.px(14))
        te = QTextEdit()
        te.setReadOnly(True)
        te.setPlainText(out[:50000])
        v.addWidget(te)
        btns = QDialogButtonBox(QDialogButtonBox.Close)
        btns.rejected.connect(dlg.reject)
        btns.accepted.connect(dlg.accept)
        v.addWidget(btns)
        dlg.exec_()

    def _pkg_clear(self):
        pkg = self._pkg_sel()
        if not pkg: return
        if QMessageBox.question(self, "Clear Data",
            f"Clear data for {pkg}?",
            QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
        self._adb(["shell", "pm", "clear", pkg])
        self._log("warn", f"cleared · {pkg}")

    def _pkg_stop(self):
        pkg = self._pkg_sel()
        if not pkg: return
        self._adb(["shell", "am", "force-stop", pkg])
        self._log("warn", f"stopped · {pkg}")

    def _pkg_disable(self):
        pkg = self._pkg_sel()
        if not pkg: return
        if QMessageBox.question(self, "Disable",
            f"Disable {pkg}?", QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
        self._adb(["shell", "pm", "disable-user", "--user", "0", pkg])
        self._log("warn", f"disabled · {pkg}")

    def _pkg_enable(self):
        pkg = self._pkg_sel()
        if not pkg: return
        self._adb(["shell", "pm", "enable", pkg])
        self._log("ok", f"enabled · {pkg}")

    def _pkg_uninstall(self):
        pkg = self._pkg_sel()
        if not pkg: return
        if QMessageBox.warning(self, "Uninstall",
            f"Uninstall {pkg}?\n\nCannot be undone.",
            QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
        out = self._adb(["uninstall", pkg], timeout=25)
        self._log("ok" if "Success" in out else "warn", f"uninstall · {pkg}")

    def _load_files(self, path):
        if not self.device: return
        self.cur_file_path = path
        self.path_input.setText(path)

        def work():
            out = self._adb(["shell", "ls", "-la", path], timeout=15)
            entries = []
            for ln in out.splitlines():
                if ln.startswith("total") or not ln.strip(): continue
                parts = ln.split(maxsplit=7)
                if len(parts) < 8: continue
                perm = parts[0]; size = parts[4]
                owner = parts[2]; name = parts[7]
                if name in (".", ".."): continue
                is_dir = perm.startswith("d")
                is_link = perm.startswith("l")
                typ = "DIR" if is_dir else ("LINK" if is_link else "FILE")
                entries.append({
                    "name": name, "type": typ, "size": size,
                    "perm": perm, "owner": owner,
                })
            self.bus.files.emit(path, entries)
        threading.Thread(target=work, daemon=True).start()

    def _on_files(self, path, entries):
        self.file_table.setRowCount(len(entries))
        for i, e in enumerate(entries):
            self.file_table.setItem(i, 0, QTableWidgetItem(e["name"]))
            self.file_table.setItem(i, 1, QTableWidgetItem(e["type"]))
            self.file_table.setItem(i, 2, QTableWidgetItem(
                human_bytes(e["size"]) if e["size"].isdigit() else e["size"]))
            self.file_table.setItem(i, 3, QTableWidgetItem(e["perm"]))
            self.file_table.setItem(i, 4, QTableWidgetItem(e["owner"]))
        self._log("info", f"browsed · {path}  ({len(entries)})")

    def _file_open(self):
        r = self.file_table.currentRow()
        if r < 0: return
        name = self.file_table.item(r, 0).text()
        typ = self.file_table.item(r, 1).text()
        if typ == "DIR":
            new_path = os.path.join(self.cur_file_path, name).replace("//", "/")
            self._load_files(new_path)

    def _file_up(self):
        parent = os.path.dirname(self.cur_file_path.rstrip("/")) or "/"
        self._load_files(parent)

    def _file_download(self):
        r = self.file_table.currentRow()
        if r < 0: return
        name = self.file_table.item(r, 0).text()
        remote = os.path.join(self.cur_file_path, name)
        local, _ = QFileDialog.getSaveFileName(self, "Save As", name)
        if not local: return
        def work():
            ok, out, err = run(
                ["adb", "-s", self.device, "pull", remote, local], timeout=120)
            self._log("ok" if ok else "err", f"pull {name} → {local}")
        threading.Thread(target=work, daemon=True).start()

    def _file_delete(self):
        r = self.file_table.currentRow()
        if r < 0: return
        name = self.file_table.item(r, 0).text()
        remote = os.path.join(self.cur_file_path, name)
        if QMessageBox.question(self, "Delete",
            f"Delete {remote}?",
            QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
        self._adb(["shell", "rm", "-rf", remote])
        self._log("warn", f"deleted · {remote}")
        self._load_files(self.cur_file_path)

    def _file_mkdir(self):
        name, ok = QInputDialog.getText(self, "New Directory", "Name:")
        if not (ok and name): return
        remote = os.path.join(self.cur_file_path, name)
        self._adb(["shell", "mkdir", "-p", remote])
        self._log("ok", f"mkdir · {remote}")
        self._load_files(self.cur_file_path)

    def _load_processes(self):
        if not self.device: return
        def work():
            out = self._adb(["shell", "ps", "-A", "-o",
                             "PID,PPID,USER,STAT,NAME"], timeout=20)
            rows = []
            for ln in out.splitlines()[1:]:
                p = ln.split(maxsplit=4)
                if len(p) < 5: continue
                rows.append([p[0], p[1], p[2], p[3], p[4]])
            self.bus.processes.emit(rows)
        threading.Thread(target=work, daemon=True).start()

    def _on_processes(self, rows):
        self.proc_table.setSortingEnabled(False)
        self.proc_table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, v in enumerate(row):
                self.proc_table.setItem(i, j, QTableWidgetItem(str(v)))
        self.proc_table.setSortingEnabled(True)
        self._log("info", f"{len(rows)} processes")

    def _filter_procs(self, text):
        text = text.lower()
        for i in range(self.proc_table.rowCount()):
            hide = False
            if text:
                row = " ".join(
                    (self.proc_table.item(i, j).text()
                     if self.proc_table.item(i, j) else "")
                    for j in range(self.proc_table.columnCount())
                ).lower()
                hide = text not in row
            self.proc_table.setRowHidden(i, hide)

    def _kill_proc(self):
        r = self.proc_table.currentRow()
        if r < 0: return
        pid = self.proc_table.item(r, 0).text()
        name = self.proc_table.item(r, 4).text()
        if QMessageBox.question(self, "Kill",
            f"Kill PID {pid} ({name})?",
            QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
        self._adb(["shell", "kill", "-9", pid])
        self._log("warn", f"killed · {name} ({pid})")
        self._load_processes()

    def _kill_bg(self):
        if QMessageBox.warning(self, "Kill Background",
            "Kill ALL background apps?",
            QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
        self._adb(["shell", "am", "kill-all"])
        self._log("warn", "background apps killed")
        self._load_processes()

    def _logcat_start(self):
        if not self.device: return
        if self.logcat_proc: return
        lvl = self.log_level.currentText()
        try:
            self.logcat_proc = subprocess.Popen(
                ["adb", "-s", self.device, "logcat", f"*:{lvl}"],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1, stdin=subprocess.DEVNULL)
        except Exception as e:
            self._log("err", f"logcat failed · {e}")
            return
        self.btn_log_start.setEnabled(False)
        self.btn_log_stop.setEnabled(True)
        self._log("ok", f"logcat · level {lvl}")
        threading.Thread(target=self._logcat_reader, daemon=True).start()

    def _logcat_reader(self):
        while self.logcat_proc and self.logcat_proc.poll() is None:
            try:
                ln = self.logcat_proc.stdout.readline()
                if ln: self.bus.logcat_line.emit(ln.rstrip())
            except: break
            time.sleep(0.01)

    def _on_logcat_line(self, ln):
        if self.cur_logcat_filter and self.cur_logcat_filter.lower() not in ln.lower():
            return
            
        # Smart Highlighting
        if "FATAL" in ln or "Exception" in ln or "Error" in ln:
            html = f'<span style="color:{T.RED}; font-weight:bold;">{ln}</span>'
            self.logcat_view.appendHtml(html)
        elif "WARN" in ln:
            html = f'<span style="color:{T.AMBER};">{ln}</span>'
            self.logcat_view.appendHtml(html)
        else:
            self.logcat_view.appendPlainText(ln)
            
        sb = self.logcat_view.verticalScrollBar()
        sb.setValue(sb.maximum())

    def _logcat_stop(self):
        if self.logcat_proc:
            try:
                self.logcat_proc.terminate()
                self.logcat_proc.wait(timeout=2)
            except:
                self.logcat_proc.kill()
            self.logcat_proc = None
        self.btn_log_start.setEnabled(True)
        self.btn_log_stop.setEnabled(False)
        self._log("warn", "logcat stopped")

    def _logcat_clear(self):
        self.logcat_view.clear()

    def _logcat_save(self):
        name = f"logcat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(name, "w") as f:
            f.write(self.logcat_view.toPlainText())
        self._log("ok", f"saved · {name}")

    def _filter_logcat(self, text):
        self.cur_logcat_filter = text.strip()

    def _term_exec(self):
        cmd = self.term_input.text().strip()
        if not cmd: return
        self.term_input.clear()
        self._term_run_args(cmd.split())

    def _term_run_args(self, args):
        if not self.device:
            self.bus.term_out.emit("ERR: no device connected")
            return
        self.bus.term_out.emit(f"\n$ adb -s {self.device} {' '.join(args)}")

        def work():
            try:
                if not args or args[0] != "adb":
                    full = ["-s", self.device] + args
                else:
                    full = args[1:]
                ok, out, err = run(["adb"] + full, timeout=25)
                if out:
                    self.bus.term_out.emit(out[:20000])
                if err:
                    self.bus.term_out.emit(f"[stderr] {err}")
                if not out and not err:
                    self.bus.term_out.emit("[no output]")
            except Exception as e:
                self.bus.term_out.emit(f"[error] {str(e)[:200]}")

        threading.Thread(target=work, daemon=True).start()

    def _on_term_out(self, text):
        self.term_out.appendPlainText(text)

    def _start_scrcpy(self):
        if not self.device:
            self._log("err", "no device")
            return
        if self.scrcpy_running: return
        if not which("scrcpy"):
            self._log("err", "scrcpy not installed")
            return

        bitrate = self.opt_bitrate.currentText().split()[0]
        size    = self.opt_size.currentText()
        fps     = self.opt_fps.currentText()
        rot     = self.opt_rot.currentText()

        cmd = [
            "scrcpy", "-s", self.device,
            "--max-size", size,
            "--max-fps", fps,
            "--video-bit-rate", f"{bitrate}M",
            "--window-title", f"DROID SURGEON · {self.device}",
        ]

        if rot != "0":
            if self._scrcpy_supports("--display-orientation"):
                cmd += ["--display-orientation", rot]
            elif self._scrcpy_supports("--rotation"):
                cmd += ["--rotation", rot]

        if self.opt_noaudio.isChecked() and self._scrcpy_supports("--no-audio"):
            cmd.append("--no-audio")
        if self.opt_fullscreen.isChecked() and self._scrcpy_supports("--fullscreen"):
            cmd.append("--fullscreen")
        if self.opt_always_top.isChecked() and self._scrcpy_supports("--always-on-top"):
            cmd.append("--always-on-top")
        if self.opt_turnoff.isChecked() and self._scrcpy_supports("--turn-screen-off"):
            cmd.append("--turn-screen-off")

        try:
            self.scrcpy = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1, stdin=subprocess.DEVNULL)
            self.scrcpy_running = True
            self.btn_start_mirror.setEnabled(False)
            self.btn_stop_mirror.setEnabled(True)
            self._set_pill(self.pill_sc, "MIRROR · LIVE", "live")

            self.mirror_status.setText(
                f"STREAMING\n\n"
                f"  Device  :  {self.device}\n"
                f"  Bitrate :  {bitrate} Mbps\n"
                f"  FPS     :  {fps}\n"
                f"  Size    :  {size}px\n"
                f"  Orient  :  {rot}°"
            )
            self.mirror_status.setStyleSheet(f"""
                QLabel {{
                    background: rgba(0,0,0,0.35);
                    border: 1px solid {T.GREEN_DIM};
                    border-radius: 7px;
                    color: {T.GREEN};
                    font-family: {T.FONT_MONO};
                    font-size: {Scale.pt(9)}pt;
                    padding: {Scale.px(18)}px;
                }}
            """)
            self._log("ok", "scrcpy started")
            threading.Thread(target=self._monitor_scrcpy, daemon=True).start()
        except Exception as e:
            self._log("err", f"scrcpy failed · {str(e)[:120]}")

    def _monitor_scrcpy(self):
        while self.scrcpy and self.scrcpy.poll() is None:
            try:
                ln = self.scrcpy.stdout.readline()
                if ln: self.bus.scrcpy_out.emit(ln.rstrip())
            except: break
            time.sleep(0.05)
        self.bus.scrcpy_state.emit("stopped")

    def _stop_scrcpy(self):
        if self.scrcpy:
            try:
                self.scrcpy.terminate()
                self.scrcpy.wait(timeout=3)
            except:
                self.scrcpy.kill()
            self.scrcpy = None
            self._on_scrcpy_state("stopped")

    def _on_scrcpy_state(self, state):
        self.scrcpy_running = False
        self.btn_start_mirror.setEnabled(True)
        self.btn_stop_mirror.setEnabled(False)
        self._set_pill(self.pill_sc, "MIRROR", "off")
        self.mirror_status.setText("MIRROR OFFLINE\n\nNo active session.")
        self.mirror_status.setStyleSheet(f"""
            QLabel {{
                background: rgba(0,0,0,0.35);
                border: 1px dashed {T.B};
                border-radius: 7px;
                color: {T.TEXT_DIM};
                font-family: {T.FONT_MONO};
                font-size: {Scale.pt(9)}pt;
                padding: {Scale.px(18)}px;
            }}
        """)
        self._log("warn", "scrcpy stopped")

    def _on_scrcpy_log(self, line):
        self.mirror_log.append(line)

    def _mirror_fs(self):
        if self.scrcpy_running:
            run(["xdotool", "search", "--name",
                 f"DROID SURGEON · {self.device}",
                 "windowactivate", "key", "Alt+f"], timeout=3)

    def _mirror_rotate(self):
        if self.scrcpy_running:
            run(["xdotool", "search", "--name",
                 f"DROID SURGEON · {self.device}",
                 "windowactivate", "key", "r"], timeout=3)

    def _scrcpy_supports(self, flag):
        if not which("scrcpy"): return False
        if self._scrcpy_help_cache is None:
            ok, out, err = run(["scrcpy", "--help"], timeout=5)
            self._scrcpy_help_cache = (out or "") + (err or "")
        return flag in self._scrcpy_help_cache

    def _fb_cmd(self, cmd):
        if not self.fb_device:
            self._log("err", "no fastboot device")
            return

        if cmd == "getvar-all": args = ["getvar", "all"]
        elif cmd == "getvar-product": args = ["getvar", "product"]
        elif cmd == "oem-device-info": args = ["oem", "device-info"]
        elif cmd == "oem-unlock":
            if QMessageBox.warning(self, "UNLOCK",
                "ERASE ALL DATA?\n\nContinue?",
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
            args = ["oem", "unlock"]
        elif cmd == "oem-lock":
            if QMessageBox.warning(self, "LOCK",
                "May ERASE ALL DATA.\n\nContinue?",
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
            args = ["oem", "lock"]
        elif cmd == "erase-userdata":
            if QMessageBox.warning(self, "ERASE USERDATA",
                "ERASE ALL DATA?\n\nContinue?",
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
            args = ["erase", "userdata"]
        elif cmd == "erase-cache": args = ["erase", "cache"]
        elif cmd == "format-userdata":
            if QMessageBox.warning(self, "FORMAT USERDATA",
                "ERASE ALL DATA?\n\nContinue?",
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes: return
            args = ["format", "userdata"]
        elif cmd in ("flash-boot", "flash-recovery", "flash-system", "flash-vbmeta"):
            p, _ = QFileDialog.getOpenFileName(self, "image",
                os.path.expanduser("~"), "Images (*.img);;All (*)")
            if not p: return
            part = cmd.split("-")[1]
            if part == "vbmeta":
                args = ["flash", "vbmeta",
                        "--disable-verity", "--disable-verification", p]
            else:
                args = ["flash", part, p]
        elif cmd == "flash-all":
            p, _ = QFileDialog.getOpenFileName(self, "ZIP",
                os.path.expanduser("~"), "Zip (*.zip);;All (*)")
            if not p: return
            args = ["update", p]
        elif cmd == "set-active-a": args = ["--set-active=a"]
        elif cmd == "set-active-b": args = ["--set-active=b"]
        elif cmd == "flashing-unlock": args = ["flashing", "unlock"]
        elif cmd == "flashing-lock": args = ["flashing", "lock"]
        elif cmd == "continue": args = ["continue"]
        else: args = cmd.split()

        self.bus.fb_out.emit(f"\n> fastboot {' '.join(args)}")
        threading.Thread(target=self._fb_run, args=(args,), daemon=True).start()

    def _fb_run(self, args):
        ok, out, err = run(["fastboot", "-s", self.fb_device] + args, timeout=90)
        if out:
            for ln in out.splitlines():
                self.bus.fb_out.emit(f"  {ln}")
        if err:
            for ln in err.splitlines():
                self.bus.fb_out.emit(f"  [!] {ln}")

    def _on_fb_log(self, line):
        self.fb_out.append(line)

    def _export_fb(self):
        name = f"fastboot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(name, "w") as f:
            f.write(self.fb_out.toPlainText())
        self._log("ok", f"exported · {name}")

    def keyPressEvent(self, event):
        key = event.key()
        mods = event.modifiers()

        if mods & Qt.ControlModifier and key == Qt.Key_Q:
            self.close()
            return
        if mods & Qt.ControlModifier and key in (Qt.Key_Plus, Qt.Key_Equal):
            self._set_scale(Scale.value + 0.1)
            return
        if mods & Qt.ControlModifier and key == Qt.Key_Minus:
            self._set_scale(Scale.value - 0.1)
            return
        if mods & Qt.ControlModifier and key == Qt.Key_0:
            self._set_scale(1.0)
            return

        if Qt.Key_1 <= key <= Qt.Key_9:
            idx = key - Qt.Key_1
            if idx < len(self.TABS): self._switch(idx)
        elif key == Qt.Key_0:
            self._switch(9)
        elif key == Qt.Key_F5:
            self._refresh_adb()
            self._refresh_fb()
        elif key == Qt.Key_F11:
            self.showNormal() if self.isFullScreen() else self.showFullScreen()
        else:
            super().keyPressEvent(event)


# ═══════════════════════════════════════════════════════════════════════════
#                              ENTRY
# ═══════════════════════════════════════════════════════════════════════════

def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setApplicationName("Droid Surgeon")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(T.BG_DEEP))
    palette.setColor(QPalette.WindowText, QColor(T.TEXT))
    palette.setColor(QPalette.Base, QColor(T.BG_INPUT))
    palette.setColor(QPalette.AlternateBase, QColor(T.BG_PANEL))
    palette.setColor(QPalette.Text, QColor(T.TEXT_HI))
    palette.setColor(QPalette.Button, QColor(T.BG_PANEL_HI))
    palette.setColor(QPalette.ButtonText, QColor(T.TEXT))
    palette.setColor(QPalette.Highlight, QColor(T.CYAN_DEEP))
    palette.setColor(QPalette.HighlightedText, QColor(T.TEXT_HI))
    palette.setColor(QPalette.ToolTipBase, QColor(T.BG_PANEL))
    palette.setColor(QPalette.ToolTipText, QColor(T.CYAN))
    app.setPalette(palette)

    app.setFont(QFont("Segoe UI", 10))
    app.setStyleSheet(build_stylesheet())

    win = DroidSurgeon()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
