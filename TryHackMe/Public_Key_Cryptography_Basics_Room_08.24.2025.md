# Public Key Cryptography Basics Room

## Time: 1.30 Hr 

### URL: https://tryhackme.com/room/publickeycrypto
<img width="713" height="490" alt="image" src="https://github.com/user-attachments/assets/3ec8323b-47b3-420f-bd97-2656be16b736" />

Examples are RSA, Diffie-Hellman, and Elliptic Curve cryptography (ECC). The two keys involved in the process are referred to as a **public key** and a **private key**.

Data encrypted with the public key can be decrypted with the private  key. Your private key needs to be kept private, hence the name.

Asymmetric encryption tends to be slower, and many asymmetric encryption ciphers use larger keys than symmetric encryption. For example, RSA uses 2048-bit, 3072-bit, and 4096-bit keys; 2048-bit is the recommended minimum key size. Diffie-Hellman also has a recommended minimum key size of 2048 bits but uses 3072-bit and 4096-bit keys for enhanced security. On the other hand, ECC can achieve equivalent security with shorter keys. For example, with a 256-bit key, ECC provides a level of security comparable to a 3072-bit RSA key.

### 🔑 How asymmetric encryption normally works

- **Public key → encrypts**
- **Private key → decrypts**
    
    That’s how confidentiality is achieved: anyone can send you an encrypted message, but only you (with your private key) can read it.
    
---

### 🔏 What happens if you "encrypt" with your **private key** instead

If you take your private key and run the “encryption” operation:

- Anyone with your **public key** can “decrypt” it.
- But since the public key is… well, *public*, this doesn’t provide confidentiality. Anyone can read it.
- What it does provide is **authenticity** → it proves the data must have come from you, since only you had the private key to generate that output.

This is essentially how **digital signatures** work:

- You sign (private key operation).
- Others verify (public key operation).

---

✅ So the key idea is:

- **Encrypt with public → private decrypts → confidentiality.**
- **“Encrypt” with private → public decrypts → authenticity (signature).**

# Completed 
