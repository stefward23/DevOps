# Hashing Basics

## Time: 1.30 Hr

### URL: https://tryhackme.com/room/hashingbasics

md5sum file: provides the md5 hash of a file

sha1sum file: provides the sha1 hash of a file

sha256sum file: provides the sha256 hash of a file

sha512sum file: provides the sha512 hash of a file

sha1 and md5 have been attacked and are easy to engineer hash collisions.

Websites like [CrackStation](https://crackstation.net/) and [Hashes.com](https://hashes.com/en/decrypt/hash) internally use massive rainbow tables to provide fast password cracking for **hashes without salts**.

The salt is added to either the start or the end of the password before it’s hashed, and this means that every user will have a different password hash even if they have the same password. Hash functions like Bcrypt and Scrypt handle this automatically. Salts don’t need to be kept private.

How to create a proper hashed password:

1. We select a secure hashing function, such as Argon2, Scrypt, Bcrypt, or PBKDF2.
2. We add a unique salt to the password, such as `Y4UV*^(=go_!`
3. Concatenate the password with the unique salt. For example, if the password is `AL4RMc10k`, the result string would be `AL4RMc10kY4UV*^(=go_!`
4. Calculate the hash value of the combined password and salt. In this example, using the chosen algorithm, you need to calculate the hash value of `AL4RMc10kY4UV*^(=go_!`.
5. Store the hash value and the unique salt used (`Y4UV*^(=go_!`).

https://hashcat.net/wiki/doku.php?id=example_hashes


# Completed
