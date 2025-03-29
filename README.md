# 📡 BLE Secure Pairing Protocol & Android Security Audit Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Android / Kotlin](https://img.shields.io/badge/Platform-Android_%7C_Kotlin-green.svg)]()

## 📌 Project Overview
This repository contains the implementation of **Bluetooth Low Energy (BLE) Secure Pairing** (LESC / Numeric Comparison) with AES-128 link encryption to prevent Man-in-the-Middle (MitM) attacks, combined with an **Android Least Privilege Security Audit Module**.

---

## 🛠️ Security Capabilities
1. **LE Secure Connections (LESC)**: Forces ECDH (P-256) authenticated key exchange during BLE pairing.
2. **MitM Attack Prevention**: Enforces Passkey Entry or Numeric Comparison pairing modes.
3. **Android Permission Auditing**: Implements runtime permission checks ensuring dynamic requested scopes for `BLUETOOTH_SCAN`, `BLUETOOTH_CONNECT`, and `ACCESS_FINE_LOCATION`.
4. **SDK Data Leak Prevention**: Sanity checks prohibiting background broadcast leaks of sensitive BLE payload attributes.

---

## 📁 Repository Structure
```
ble-android-security/
├── README.md
├── android/
│   └── BleSecurityManager.kt      # Android Kotlin BLE pairing & permission enforcement class
└── .gitignore
```

---

## 👤 Author
- **Author:** Fahd BELHIBA
- **GitHub:** [@ScaramouW](https://github.com/ScaramouW)
