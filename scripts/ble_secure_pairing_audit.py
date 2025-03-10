#!/usr/bin/env python3
"""
Bluetooth Low Energy (BLE) Secure Pairing & Security Auditor
Author: Fahd BELHIBA
Description: Inspects BLE advertisement packets, checks security flags,
and verifies LE Secure Connections (LESC) pairing mode against MitM attacks.
"""

import sys

def audit_ble_pairing_flags(pairing_req_flags: dict):
    print("[*] Auditing BLE Security & Pairing Capabilities...")
    
    io_capability = pairing_req_flags.get("io_cap", "NoInputNoOutput")
    oob_data = pairing_req_flags.get("oob_present", False)
    auth_req = pairing_req_flags.get("auth_req", 0x00) # Bit 3: LE Secure Connections

    lesc_supported = bool(auth_req & 0x08)
    mitm_protection = bool(auth_req & 0x04)

    print(f"    ├─ IO Capability: {io_capability}")
    print(f"    ├─ OOB Data Present: {oob_data}")
    print(f"    ├─ LE Secure Connections (LESC): {'ENFORCED' if lesc_supported else 'VULNERABLE (Legacy Pairing)'}")
    print(f"    └─ MitM Protection Flag: {'ACTIVE' if mitm_protection else 'INACTIVE'}")

    if not lesc_supported:
        print("[!] WARN: Legacy BLE Pairing detected. Susceptible to passive eavesdropping!")
    elif not mitm_protection:
        print("[!] WARN: Just Works pairing mode used. Vulnerable to active MitM!")
    else:
        print("[✓] PASS: BLE Secure Pairing (LESC + MitM Protection) active.")

if __name__ == "__main__":
    sample_ble_flags = {
        "io_cap": "DisplayYesNo",
        "oob_present": False,
        "auth_req": 0x0D # LESC + MitM + Bonding
    }
    audit_ble_pairing_flags(sample_ble_flags)
