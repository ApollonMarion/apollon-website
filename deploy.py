#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apollon, automatischer Upload auf den Webserver.

Aufruf:      python3 deploy.py
Trockenlauf: python3 deploy.py --test     (zeigt nur an, was passieren würde)
Alles neu:   python3 deploy.py --alles    (ignoriert den Merkzettel und lädt alles hoch)

Die Zugangsdaten stehen in der Datei .deploy.env neben diesem Skript.
Sie werden nie in dieses Skript geschrieben und nie mitversendet.
"""

import os, sys, ssl, json, hashlib, posixpath
from ftplib import FTP, FTP_TLS, error_perm

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.join(HERE, ".deploy.env")
STATE = os.path.join(HERE, ".deploy-state.json")
QUELLE = os.path.join(HERE, "site")          # was hochgeladen wird
AUSNAHMEN = {".DS_Store", ".deploy.env", ".deploy-state.json", "deploy.py",
             "build.py", "pages.py", "pages2.py", "__pycache__"}

TEST = "--test" in sys.argv
ALLES = "--alles" in sys.argv


def lies_env():
    if not os.path.exists(ENV):
        sys.exit("Die Datei .deploy.env fehlt. Lege sie neben deploy.py an, "
                 "die Vorlage heißt .deploy.env.beispiel")
    werte = {}
    with open(ENV, encoding="utf-8") as f:
        for zeile in f:
            zeile = zeile.strip()
            if not zeile or zeile.startswith("#") or "=" not in zeile:
                continue
            k, v = zeile.split("=", 1)
            werte[k.strip()] = v.strip().strip('"').strip("'")
    for pflicht in ("FTP_HOST", "FTP_USER", "FTP_PASS"):
        if not werte.get(pflicht):
            sys.exit("In .deploy.env fehlt: " + pflicht)
    werte.setdefault("FTP_DIR", "/")
    werte.setdefault("FTP_TLS", "ja")
    return werte


def hash_datei(pfad):
    h = hashlib.sha256()
    with open(pfad, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def sammle_dateien():
    dateien = []
    for wurzel, ordner, namen in os.walk(QUELLE):
        ordner[:] = [o for o in ordner if o not in AUSNAHMEN]
        for n in namen:
            if n in AUSNAHMEN:
                continue
            voll = os.path.join(wurzel, n)
            rel = os.path.relpath(voll, QUELLE).replace(os.sep, "/")
            dateien.append((rel, voll))
    return sorted(dateien)


def verbinde(cfg):
    if cfg["FTP_TLS"].lower() in ("ja", "yes", "true", "1"):
        ftp = FTP_TLS(context=ssl.create_default_context())
        ftp.connect(cfg["FTP_HOST"], int(cfg.get("FTP_PORT", 21)), timeout=30)
        ftp.login(cfg["FTP_USER"], cfg["FTP_PASS"])
        ftp.prot_p()
    else:
        ftp = FTP()
        ftp.connect(cfg["FTP_HOST"], int(cfg.get("FTP_PORT", 21)), timeout=30)
        ftp.login(cfg["FTP_USER"], cfg["FTP_PASS"])
    ftp.set_pasv(True)
    return ftp


def sorge_fuer_ordner(ftp, pfad, bekannt):
    if pfad in ("", ".", "/") or pfad in bekannt:
        return
    eltern = posixpath.dirname(pfad)
    if eltern:
        sorge_fuer_ordner(ftp, eltern, bekannt)
    try:
        ftp.mkd(pfad)
    except error_perm as e:
        if not str(e).startswith("550"):
            raise
    bekannt.add(pfad)


def main():
    cfg = lies_env()
    zustand = {}
    if os.path.exists(STATE) and not ALLES:
        try:
            zustand = json.load(open(STATE, encoding="utf-8"))
        except Exception:
            zustand = {}

    dateien = sammle_dateien()
    zu_tun = []
    for rel, voll in dateien:
        h = hash_datei(voll)
        if zustand.get(rel) != h:
            zu_tun.append((rel, voll, h))

    if not zu_tun:
        print("Nichts zu tun, der Server ist auf dem aktuellen Stand.")
        return

    print("%d von %d Dateien haben sich geändert:" % (len(zu_tun), len(dateien)))
    for rel, _, _ in zu_tun:
        print("   " + rel)

    if TEST:
        print("\nTrockenlauf, es wurde nichts hochgeladen.")
        return

    ftp = verbinde(cfg)
    basis = cfg["FTP_DIR"].rstrip("/")
    if basis:
        ftp.cwd(basis)
    bekannt = set()
    for rel, voll, h in zu_tun:
        ordner = posixpath.dirname(rel)
        if ordner:
            sorge_fuer_ordner(ftp, ordner, bekannt)
        with open(voll, "rb") as f:
            ftp.storbinary("STOR " + rel, f)
        zustand[rel] = h
        print("hochgeladen: " + rel)
    ftp.quit()

    json.dump(zustand, open(STATE, "w", encoding="utf-8"), indent=1)
    print("\nFertig. %d Dateien übertragen." % len(zu_tun))


if __name__ == "__main__":
    main()
