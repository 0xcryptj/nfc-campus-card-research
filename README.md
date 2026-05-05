# NFC Campus Card Security Research
**College of Charleston — Blackboard Transact System**
Passive Enumeration & Architecture Analysis | May 2026

## Summary
Passive security research analyzing the NFC student ID card infrastructure at the College of Charleston. All findings obtained through unauthenticated enumeration of the researcher's own card. No university systems were accessed or modified.

## Card Hardware
- **Type:** Mifare DESFire EV1 (NXP)
- **Storage:** 8KB chip, ~4KB free
- **Protocol:** ISO 14443-4A
- **Encryption:** AES-128

## Applications Found
| AID | Function |
|-----|----------|
| BBBBBB | Campus Identity |
| B3BBBB | Access Control |
| DABBBB | Dining/Transactional |

## Key Findings
- Vendor fingerprinted via AID pattern BBBBBB (Blackboard Transact)
- Plain communication mode on all files
- Key version inconsistency across applications
- Server-side balance architecture confirmed

## Tools Used
- Flipper Zero (Momentum firmware)
- Python + pyserial (Flipper CLI bridge)
- libfreefare / libnfc
- WSL2 + Ubuntu

## Methodology
Passive unauthenticated enumeration only. No keys or credentials obtained or attempted. Research performed on researcher's own card.

## Disclosure
Findings documented May 2026. Intended for responsible disclosure to CofC IT Security.
