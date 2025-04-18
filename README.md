
# Keylogger Project

This project demonstrates a basic keylogger that logs keystrokes, encrypts sensitive information, and sends the log file to a specified email address.

> ⚠️ **Disclaimer**: This project is for educational purposes only. Unauthorized use of keyloggers may violate privacy laws. Use only on machines you own or have permission to monitor.

---

## Features

- Logs all keystrokes made on the computer.
- Encrypts sensitive information such as email address, password, and recipient email.
- Sends the log file as an attachment to a specified email address.

---

## Requirements

- Python 3.x
- [`pynput`](https://pypi.org/project/pynput/) for keyboard input
- [`cryptography`](https://pypi.org/project/cryptography/) for encryption
- `smtplib` (standard Python library)

---

## Installation

1. **Install the required libraries**:

   ```bash
   pip install pynput cryptography
   ```

2. **Replace the placeholders in the keylogger script with your own information**:
   - `"*****@gmail.com"`: Replace with your Gmail email address.
   - `"***********"`: Replace with your Gmail password.
   - `"************.com.np"`: Replace with the email address of the recipient.

3. **Generate encryption keys for the sensitive information**:
   - Open the encryption script (`encrypt.py`) and run it to generate encryption keys for the email address, password, and recipient email address.
   - Replace the placeholders in the keylogger script with the generated encryption keys.

---

## Usage

1. **Run the encryption script**:

   ```bash
   python encrypt.py
   ```

   This will generate the encrypted email credentials that will be used in the keylogger script.

2. **Run the keylogger script**:

   ```bash
   python keylogger.py
   ```

   The keylogger will now start logging keystrokes and will send the log file to the specified email.

---

## Support

For support, [email us](https://mail.google.com/mail/?view=cm&fs=1&to=arunkbijuofficial@gmail.com&su=Let%27s%20Chat&body=Hi,%20I%20would%20love%20to%20connect%20with%20you.%20Looking%20forward%20to%20your%20response.).
