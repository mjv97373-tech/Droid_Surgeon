<meta name="google-site-verification" content="dapULigPJXUkPzyM_jbfZHcGlZVnlRByXcxh1TlSsok" />


<div align="center">

# ⚕️ DROID SURGEON
# Last Edition : 2.0.0 Lab Version 
# Old version : 1.1.1
### Advanced Android Device Management Suite

**Control · Inspect · Mirror · Diagnose**

A desktop toolkit for Android device workflows, built with **Python**, **PyQt5**, **ADB**, **Fastboot**, and **scrcpy**.

[English](#english) · [فارسی](#فارسی) · [Русский](#русский)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-41CD52?logo=qt&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-informational)
![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)

**Version:** `2.0.0`

</div>

---

## Contents

- [English](#english)
- [فارسی](#فارسی)
- [Русский](#русский)
- [Safety Notice](#safety-notice)
- [License](#license)

<a id="english"></a>


##  Interface Preview

| Theme | Theme |
|:---:|:---:|
| ![Theme](screenshot/mdk.png) | ![Theme](screenshot/orc.png) |

| Theme | Theme |
|:---:|:---:|
| ![Theme](screenshot/rose.png) | ![Theme](screenshot/mcs.png) |


## 🇬🇧 English

### Overview

**DROID SURGEON** is a desktop graphical interface for managing and inspecting Android devices through established command-line tools. It brings common ADB, Fastboot, and scrcpy workflows together in a dark, resizable interface.

> [!NOTE]
> DROID SURGEON is a front-end for external Android tools, not a replacement for them. Available operations depend on the connected device, Android version, permissions, bootloader state, and installed tool versions.

### Features

- **Dashboard** — view available battery, storage, memory, thermal, and uptime information.
- **ADB control** — send hardware-key events and perform supported tap, swipe, long-press, pinch, and scroll gestures.
- **Screen mirroring** — launch scrcpy and configure supported bitrate, frame-rate, size, and orientation options.
- **Fastboot tools** — access supported bootloader operations.
- **Package management** — inspect installed packages and use available package actions.
- **Device file browser** — browse supported device paths and perform available file operations.
- **Process viewer** — inspect running processes and use supported process actions.
- **Live Logcat** — view Android system logs.
- **Network diagnostics** — access the network diagnostics provided by the application.
- **Terminal and quick reference** — access supported ADB/Fastboot workflows and built-in command notes.
- **Resizable interface** — scale the UI from 70% to 140%; the setting is saved.

### Requirements

**Host computer**
- Linux (Debian, Ubuntu, Kali Linux, and Arch Linux commands are provided below)
- Python 3
- PyQt5
- Android platform tools (`adb` and `fastboot`)
- `scrcpy` for screen mirroring

**Android device**
- USB debugging enabled for ADB operations
- A data-capable USB cable, or a correctly configured Android virtual device
- For Fastboot features: a device that supports Fastboot and is booted into its bootloader/Fastboot mode

### Install dependencies

#### Debian / Ubuntu / Kali Linux

```bash
sudo apt update
sudo apt install -y python3 python3-pyqt5 android-tools-adb android-tools-fastboot scrcpy git
```

#### Arch Linux

```bash
sudo pacman -Syu
sudo pacman -S python python-pyqt5 android-tools scrcpy git
```

> Package names and versions can vary between distributions. Use your distribution's official repositories if a package name differs.

### Get the project

Clone your repository (replace the URL with your actual GitHub repository URL):

```bash
git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
cd <YOUR-REPOSITORY>
```

Or download `Droid_Surgeon.py` from the repository and open a terminal in the directory where you saved it.

### Verify the tools

```bash
python3 --version
python3 -c "import PyQt5; print('PyQt5 OK')"
adb version
fastboot --version
scrcpy --version
```

### Launch

```bash
python3 Droid_Surgeon.py
```

If the GUI opens but a feature does not work, confirm that its external command-line tool is installed and available in your `PATH`.

### Connect an Android device

1. On the device, open **Settings → About phone**.
2. Tap **Build number** repeatedly until Developer options are enabled. The exact menu may vary by manufacturer.
3. Open **Developer options** and enable **USB debugging**.
4. Connect the device with a data-capable USB cable.
5. Unlock the device and accept the USB debugging authorization prompt.
6. Refresh the ADB device list in DROID SURGEON.

Check the connection in a terminal:

```bash
adb devices
```

If the device appears as `unauthorized`, accept the authorization prompt on the device. If it does not appear, check the cable, USB port, and host USB permissions.

### Screen mirroring

1. Confirm that ADB detects and authorizes the device.
2. Open the **MIRROR** tab.
3. Choose the desired supported settings.
4. Press **START**.

Screen mirroring relies on `scrcpy` installed on the host computer. Available options may depend on the installed scrcpy version.

### Fastboot workflow

Fastboot requires a compatible device and bootloader mode. A typical transition from Android is:

```bash
adb reboot bootloader
fastboot devices
```

Return to Android using the device's supported reboot option or the appropriate command for that device.

> [!CAUTION]
> Fastboot flashing, erasing, bootloader unlocking, and slot changes can cause data loss, make a device unbootable, or affect its warranty/security state. Read each command carefully, confirm the target device, and keep a backup. Do not run commands you do not understand.

### Keyboard shortcuts

| Shortcut | Action |
|---|---|
| `1`–`9` | Open the corresponding main section |
| `0` | Open Terminal |
| `F5` | Refresh ADB and Fastboot device information |
| `F11` | Toggle fullscreen |
| `Ctrl` + `+` | Increase UI scale |
| `Ctrl` + `-` | Decrease UI scale |
| `Ctrl` + `0` | Reset UI scale |
| `Ctrl` + `Q` | Quit the application |

### Troubleshooting

**ADB does not detect the device**

```bash
adb kill-server
adb start-server
adb devices
```

Unlock the phone and accept the USB debugging authorization prompt. Also check your cable and host USB permissions.

**The mirror feature does not start**

```bash
scrcpy --version
```

Install `scrcpy` using your distribution's package manager, then try again.

**Fastboot does not detect the device**

```bash
fastboot --version
fastboot devices
```

Confirm that the device supports Fastboot and is actually in bootloader/Fastboot mode.

**PyQt5 import error**

```bash
python3 -c "import PyQt5"
```

Install the `python3-pyqt5` package (Debian-based systems) or `python-pyqt5` (Arch Linux).

### Disclaimer

DROID SURGEON is provided for legitimate device administration, development, and testing. You are responsible for actions performed on connected devices. Always obtain authorization before accessing or modifying a device, and back up important data before performing operations that may change it.

---

<a id="فارسی"></a>

## 🇮🇷 فارسی

### معرفی

**DROID SURGEON** یک رابط گرافیکی دسکتاپ برای مدیریت و بررسی دستگاه‌های اندرویدی است. این برنامه ابزارهای رایج **ADB**، **Fastboot** و **scrcpy** را در یک محیط تیره و قابل تغییر اندازه کنار هم قرار می‌دهد.

> [!NOTE]
> این برنامه جایگزین ADB، Fastboot یا scrcpy نیست؛ بلکه رابطی برای استفاده از آن‌هاست. امکانات قابل استفاده به مدل دستگاه، نسخه اندروید، سطح دسترسی، وضعیت بوت‌لودر و نسخه ابزارهای نصب‌شده بستگی دارد.

### قابلیت‌ها

- **داشبورد:** نمایش اطلاعات در دسترس باتری، حافظه، فضای ذخیره‌سازی، دما و زمان روشن‌بودن دستگاه.
- **کنترل ADB:** ارسال رویدادهای کلیدهای سخت‌افزاری و اجرای ژست‌های پشتیبانی‌شده مانند لمس، کشیدن، نگه‌داشتن، pinch و پیمایش.
- **نمایش زنده صفحه:** اجرای scrcpy و تنظیم گزینه‌های پشتیبانی‌شده مانند نرخ فریم، بیت‌ریت، اندازه و جهت تصویر.
- **ابزارهای Fastboot:** دسترسی به عملیات پشتیبانی‌شده در حالت بوت‌لودر.
- **مدیریت بسته‌ها:** مشاهده برنامه‌های نصب‌شده و استفاده از عملیات موجود.
- **مرورگر فایل دستگاه:** مرور مسیرهای پشتیبانی‌شده و انجام عملیات فایل در دسترس.
- **نمایش فرایندها:** مشاهده فرایندهای در حال اجرا و استفاده از عملیات پشتیبانی‌شده.
- **Logcat زنده:** مشاهده گزارش‌های سیستم اندروید.
- **عیب‌یابی شبکه:** دسترسی به ابزارهای تشخیصی شبکه موجود در برنامه.
- **ترمینال و راهنمای دستورات:** دسترسی به گردش‌کارهای پشتیبانی‌شده ADB/Fastboot و راهنمای داخلی.
- **تنظیم اندازه رابط:** تغییر مقیاس رابط از ۷۰٪ تا ۱۴۰٪ و ذخیره تنظیم.

### پیش‌نیازها

**رایانه میزبان**
- لینوکس؛ دستورهای نصب برای Debian، Ubuntu، Kali Linux و Arch Linux در ادامه آمده‌اند.
- Python 3
- PyQt5
- ابزارهای Android Platform Tools شامل `adb` و `fastboot`
- ابزار `scrcpy` برای نمایش زنده صفحه

**دستگاه اندرویدی**
- فعال‌بودن USB debugging برای عملیات ADB
- کابل USB دارای قابلیت انتقال داده یا ماشین مجازی اندروید با پیکربندی مناسب
- برای Fastboot، دستگاه باید از این حالت پشتیبانی کند و در حالت بوت‌لودر/Fastboot قرار داشته باشد.

### نصب پیش‌نیازها

#### Debian / Ubuntu / Kali Linux

```bash
sudo apt update
sudo apt install -y python3 python3-pyqt5 android-tools-adb android-tools-fastboot scrcpy git
```

#### Arch Linux

```bash
sudo pacman -Syu
sudo pacman -S python python-pyqt5 android-tools scrcpy git
```

> نام و نسخه بسته‌ها ممکن است با توجه به توزیع فرق کند. در صورت تفاوت، مخازن رسمی توزیع خود را بررسی کنید.

### دریافت پروژه

نشانی زیر را با آدرس واقعی مخزن GitHub خود جایگزین کنید:

```bash
git clone https://github.com/<نام-کاربری>/<نام-مخزن>.git
cd <نام-مخزن>
```

یا فایل `Droid_Surgeon.py` را از مخزن دریافت کنید و ترمینال را در پوشه‌ای باز کنید که فایل در آن قرار دارد.

### بررسی نصب ابزارها

```bash
python3 --version
python3 -c "import PyQt5; print('PyQt5 OK')"
adb version
fastboot --version
scrcpy --version
```

### اجرای برنامه

```bash
python3 Droid_Surgeon.py
```

اگر رابط برنامه باز می‌شود اما بخشی کار نمی‌کند، بررسی کنید ابزار خط فرمان مربوطه نصب باشد و از طریق `PATH` قابل اجرا باشد.

### اتصال دستگاه اندرویدی

1. در دستگاه وارد **Settings → About phone** شوید.
2. چند بار روی **Build number** بزنید تا Developer options فعال شود. نام منوها ممکن است با توجه به سازنده متفاوت باشد.
3. در Developer options گزینه **USB debugging** را فعال کنید.
4. دستگاه را با کابل دارای قابلیت انتقال داده متصل کنید.
5. قفل دستگاه را باز کنید و درخواست مجوز USB debugging را تأیید کنید.
6. فهرست دستگاه‌های ADB را در DROID SURGEON به‌روزرسانی کنید.

برای بررسی اتصال:

```bash
adb devices
```

اگر وضعیت دستگاه `unauthorized` بود، درخواست مجوز را روی خود دستگاه تأیید کنید. اگر دستگاه نمایش داده نشد، کابل، درگاه USB و مجوزهای USB سیستم میزبان را بررسی کنید.

### نمایش زنده صفحه

1. مطمئن شوید ADB دستگاه را شناسایی کرده و مجوز آن تأیید شده است.
2. وارد بخش **MIRROR** شوید.
3. تنظیمات موردنظر را انتخاب کنید.
4. روی **START** بزنید.

این قابلیت به نصب `scrcpy` روی رایانه میزبان نیاز دارد. گزینه‌های موجود ممکن است به نسخه نصب‌شده scrcpy وابسته باشند.

### گردش‌کار Fastboot

برای استفاده از Fastboot، دستگاه باید سازگار باشد و در حالت بوت‌لودر قرار بگیرد. روش معمول ورود از اندروید:

```bash
adb reboot bootloader
fastboot devices
```

برای بازگشت به اندروید از گزینه راه‌اندازی مجدد پشتیبانی‌شده توسط دستگاه یا دستور مناسب همان دستگاه استفاده کنید.

> [!CAUTION]
> فلش‌کردن، پاک‌کردن پارتیشن‌ها، بازکردن قفل بوت‌لودر و تغییر اسلات می‌توانند باعث از دست رفتن داده‌ها، بالا نیامدن دستگاه یا تغییر وضعیت امنیتی و گارانتی شوند. پیش از هر عملیات دستور را دقیق بخوانید، دستگاه هدف را بررسی کنید و از داده‌های مهم نسخه پشتیبان بگیرید. دستورهایی را که درک نمی‌کنید اجرا نکنید.

### میان‌برهای صفحه‌کلید

| میان‌بر | عملکرد |
|---|---|
| `1` تا `9` | بازکردن بخش متناظر برنامه |
| `0` | بازکردن ترمینال |
| `F5` | به‌روزرسانی اطلاعات دستگاه‌های ADB و Fastboot |
| `F11` | تغییر حالت تمام‌صفحه |
| `Ctrl` + `+` | افزایش مقیاس رابط |
| `Ctrl` + `-` | کاهش مقیاس رابط |
| `Ctrl` + `0` | بازنشانی مقیاس رابط |
| `Ctrl` + `Q` | خروج از برنامه |

### عیب‌یابی

**ADB دستگاه را شناسایی نمی‌کند**

```bash
adb kill-server
adb start-server
adb devices
```

قفل گوشی را باز کنید و درخواست مجوز USB debugging را تأیید کنید. کابل و مجوزهای USB سیستم میزبان را هم بررسی کنید.

**نمایش زنده صفحه اجرا نمی‌شود**

```bash
scrcpy --version
```

` scrcpy ` را با مدیر بسته توزیع خود نصب کنید و دوباره امتحان کنید.

**Fastboot دستگاه را شناسایی نمی‌کند**

```bash
fastboot --version
fastboot devices
```

بررسی کنید دستگاه از Fastboot پشتیبانی می‌کند و واقعاً در حالت بوت‌لودر/Fastboot است.

**خطای import برای PyQt5**

```bash
python3 -c "import PyQt5"
```

در سیستم‌های مبتنی بر Debian بسته `python3-pyqt5` و در Arch Linux بسته `python-pyqt5` را نصب کنید.

### سلب مسئولیت

DROID SURGEON برای مدیریت مجاز دستگاه، توسعه و آزمایش ارائه شده است. مسئولیت عملیات انجام‌شده روی دستگاه‌های متصل بر عهده کاربر است. پیش از دسترسی یا تغییر هر دستگاه، مجوز لازم را داشته باشید و قبل از عملیات تغییردهنده، از داده‌های مهم پشتیبان تهیه کنید.

---

<a id="русский"></a>

## 🇷🇺 Русский

### О программе

**DROID SURGEON** — настольный графический интерфейс для управления Android-устройствами и их диагностики. Он объединяет распространённые сценарии работы с **ADB**, **Fastboot** и **scrcpy** в тёмном интерфейсе с изменяемым размером.

> [!NOTE]
> Приложение является графическим интерфейсом для внешних инструментов, а не их заменой. Доступные операции зависят от устройства, версии Android, разрешений, состояния загрузчика и версий установленных утилит.

### Возможности

- **Панель состояния:** доступные сведения о батарее, хранилище, памяти, температуре и времени работы.
- **Управление через ADB:** события аппаратных клавиш и поддерживаемые жесты — касание, свайп, длительное нажатие, pinch и прокрутка.
- **Трансляция экрана:** запуск scrcpy и настройка поддерживаемых параметров битрейта, FPS, размера и ориентации.
- **Инструменты Fastboot:** доступ к поддерживаемым операциям загрузчика.
- **Управление пакетами:** просмотр установленных приложений и доступные действия с пакетами.
- **Файловый браузер:** просмотр поддерживаемых путей устройства и доступные файловые операции.
- **Просмотр процессов:** сведения о работающих процессах и поддерживаемые действия с ними.
- **Logcat в реальном времени:** просмотр системных журналов Android.
- **Сетевая диагностика:** доступ к диагностическим функциям сети, реализованным в приложении.
- **Терминал и справочник:** поддерживаемые сценарии ADB/Fastboot и встроенные заметки по командам.
- **Масштабируемый интерфейс:** масштаб от 70% до 140% с сохранением настройки.

### Требования

**Компьютер**
- Linux; ниже приведены команды для Debian, Ubuntu, Kali Linux и Arch Linux.
- Python 3
- PyQt5
- Android platform tools (`adb` и `fastboot`)
- `scrcpy` для трансляции экрана

**Android-устройство**
- Включённая USB debugging для операций ADB
- USB-кабель с передачей данных либо корректно настроенное виртуальное Android-устройство
- Для Fastboot требуется совместимое устройство, загруженное в режим загрузчика/Fastboot

### Установка зависимостей

#### Debian / Ubuntu / Kali Linux

```bash
sudo apt update
sudo apt install -y python3 python3-pyqt5 android-tools-adb android-tools-fastboot scrcpy git
```

#### Arch Linux

```bash
sudo pacman -Syu
sudo pacman -S python python-pyqt5 android-tools scrcpy git
```

> Названия пакетов и доступные версии могут отличаться в разных дистрибутивах. При необходимости используйте официальные репозитории своего дистрибутива.

### Получение проекта

Замените URL ниже на адрес вашего репозитория GitHub:

```bash
git clone https://github.com/<ИМЯ-ПОЛЬЗОВАТЕЛЯ>/<ИМЯ-РЕПОЗИТОРИЯ>.git
cd <ИМЯ-РЕПОЗИТОРИЯ>
```

Также можно скачать `Droid_Surgeon.py` из репозитория и открыть терминал в каталоге с этим файлом.

### Проверка инструментов

```bash
python3 --version
python3 -c "import PyQt5; print('PyQt5 OK')"
adb version
fastboot --version
scrcpy --version
```

### Запуск

```bash
python3 Droid_Surgeon.py
```

Если графический интерфейс запускается, но отдельная функция не работает, убедитесь, что соответствующая внешняя утилита установлена и доступна через `PATH`.

### Подключение Android-устройства

1. Откройте на устройстве **Settings → About phone**.
2. Несколько раз нажмите **Build number**, чтобы включить Developer options. Названия меню зависят от производителя.
3. Включите **USB debugging** в Developer options.
4. Подключите устройство USB-кабелем с поддержкой передачи данных.
5. Разблокируйте устройство и подтвердите запрос авторизации USB debugging.
6. Обновите список устройств ADB в DROID SURGEON.

Проверьте подключение в терминале:

```bash
adb devices
```

Если устройство отображается как `unauthorized`, подтвердите запрос на самом устройстве. Если устройство не отображается, проверьте кабель, USB-порт и права доступа к USB на компьютере.

### Трансляция экрана

1. Убедитесь, что ADB обнаруживает устройство и авторизация подтверждена.
2. Откройте вкладку **MIRROR**.
3. Выберите нужные поддерживаемые параметры.
4. Нажмите **START**.

Для трансляции требуется установленный на компьютере `scrcpy`. Доступные параметры зависят от его версии.

### Работа с Fastboot

Для Fastboot требуется совместимое устройство в режиме загрузчика. Типичный переход из Android:

```bash
adb reboot bootloader
fastboot devices
```

Для возврата в Android используйте поддерживаемый устройством способ перезагрузки или соответствующую команду.

> [!CAUTION]
> Прошивка разделов, стирание данных, разблокировка загрузчика и переключение слотов могут привести к потере данных, невозможности загрузки устройства или изменению состояния безопасности и гарантии. Внимательно проверяйте каждую команду и целевое устройство, заранее создавайте резервные копии и не выполняйте непонятные команды.

### Сочетания клавиш

| Сочетание | Действие |
|---|---|
| `1`–`9` | Открыть соответствующий раздел |
| `0` | Открыть терминал |
| `F5` | Обновить сведения ADB и Fastboot |
| `F11` | Переключить полноэкранный режим |
| `Ctrl` + `+` | Увеличить масштаб интерфейса |
| `Ctrl` + `-` | Уменьшить масштаб интерфейса |
| `Ctrl` + `0` | Сбросить масштаб интерфейса |
| `Ctrl` + `Q` | Закрыть приложение |

### Устранение неполадок

**ADB не обнаруживает устройство**

```bash
adb kill-server
adb start-server
adb devices
```

Разблокируйте устройство и подтвердите запрос USB debugging. Также проверьте кабель и права доступа к USB.

**Не запускается трансляция экрана**

```bash
scrcpy --version
```

Установите `scrcpy` через менеджер пакетов своего дистрибутива и повторите попытку.

**Fastboot не обнаруживает устройство**

```bash
fastboot --version
fastboot devices
```

Убедитесь, что устройство поддерживает Fastboot и находится в режиме загрузчика/Fastboot.

**Ошибка импорта PyQt5**

```bash
python3 -c "import PyQt5"
```

В Debian-подобных системах установите `python3-pyqt5`, а в Arch Linux — `python-pyqt5`.

### Отказ от ответственности

DROID SURGEON предназначен для законного администрирования устройств, разработки и тестирования. Пользователь несёт ответственность за действия, выполняемые на подключённых устройствах. Получайте разрешение перед доступом к устройству или его изменением и создавайте резервные копии важных данных перед потенциально изменяющими операциями.

---

## Safety Notice

Operations that modify partitions, bootloader state, packages, or device files may be destructive. Verify the target device and understand the command before proceeding.

## License

This project is distributed under the **GNU General Public License v3.0**. See [`LICENSE`](LICENSE) for the complete license text.




