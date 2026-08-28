#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Baut sitemap.xml und robots.txt aus den vorhandenen Seiten.
import os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
BASIS = "https://apollon.eu.com/"
DATUM = "2026-08-24"

# Seiten, die nicht in den Index gehoeren.
AUS = {"danke.html"}

# Wie wichtig ist welche Seite. Der Rest bekommt den Standardwert.
GEWICHT = {
    "index.html": ("1.0", "weekly"),
    "wissen.html": ("0.9", "weekly"),
    "wissen-verein.html": ("0.9", "weekly"),
    "wissen-ewiv.html": ("0.9", "weekly"),
    "wissen-koerper.html": ("0.8", "weekly"),
    "bodenplatte.html": ("0.8", "monthly"),
    "vereinsheim.html": ("0.8", "monthly"),
    "gespraech.html": ("0.8", "monthly"),
    "buch.html": ("0.7", "monthly"),
    "denkkreis.html": ("0.7", "monthly"),
    "ausstieg.html": ("0.7", "monthly"),
    "konvaleszenz.html": ("0.7", "monthly"),
    "impressum.html": ("0.2", "yearly"),
    "datenschutz.html": ("0.2", "yearly"),
}
STANDARD = ("0.7", "monthly")


def bauen():
    seiten = sorted(os.path.basename(p) for p in glob.glob(os.path.join(HERE, "*.html")))
    seiten = [s for s in seiten if s not in AUS]
    # Vorschauseiten sind Entwuerfe zur Durchsicht. Sie gehoeren niemals in
    # die Sitemap, auch nicht mit noindex, und werden auch nicht verlinkt.
    seiten = [s for s in seiten if not s.startswith("vorschau-")]

    zeilen = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for s in seiten:
        prio, takt = GEWICHT.get(s, STANDARD)
        adresse = BASIS if s == "index.html" else BASIS + s
        zeilen.append("  <url>")
        zeilen.append("    <loc>%s</loc>" % adresse)
        zeilen.append("    <lastmod>%s</lastmod>" % DATUM)
        zeilen.append("    <changefreq>%s</changefreq>" % takt)
        zeilen.append("    <priority>%s</priority>" % prio)
        zeilen.append("  </url>")
    zeilen.append("</urlset>")

    with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(zeilen) + "\n")

    robots = (
        "# Apollon\n"
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /formular.php\n"
        "Disallow: /danke.html\n"
        "Disallow: /vorschau-\n"
        "Disallow: /bearbeiten.php\n"
        "Disallow: /posteingang.php\n"
        "\n"
        "Sitemap: %ssitemap.xml\n" % BASIS
    )
    with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    print("sitemap.xml mit %d Seiten, robots.txt geschrieben." % len(seiten))


if __name__ == "__main__":
    bauen()
