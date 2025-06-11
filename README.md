# 🌓 DIMMER Node 8ch – ESP32 (ESPHome)
**HACS Custom Integration for Home Assistant**

Contrôlez une carte ESP32 configurée avec ESPHome pour piloter **8 canaux dimmer (PWM)**, avec détection automatique et intégration native dans Home Assistant.

> Développé par **[SoFarSoGood86](https://github.com/SoFarSoGood86)**

---

## ⚙️ Fonctionnalités

- 🔍 **Découverte automatique** des cartes ESPHome configurées avec le nom `dimmer-node-8ch`
- 💡 **8 entités `light`** monochromatiques
- 📶 Capteurs :
  - Signal Wi-Fi
  - Uptime
  - Adresse IP
  - Adresse MAC
  - SSID / BSSID
  - Version firmware
- 🔁 Bouton de redémarrage

---

## 📦 Installation via HACS

1. Ouvrez **HACS** dans Home Assistant
2. Allez dans **"Intégrations"** > menu ⋮ > **"Dépôt personnalisé"**
3. Ajoutez ce dépôt GitHub :
   ```
   https://github.com/SoFarSoGood86/dimmer_node_8ch
   ```
4. Catégorie : `Integration`
5. Cliquez sur **Installer**
6. Redémarrez Home Assistant si nécessaire

---

## 🧠 Configuration

Aucune configuration manuelle requise !

L'intégration détecte automatiquement les nœuds ESPHome exposant `api` et nommés `dimmer-node-8ch`.

### Prérequis dans votre code YAML ESPHome

Assurez-vous que votre nœud ESPHome contient :
```yaml
esphome:
  name: dimmer-node-8ch

api:
  encryption:
    key: "..."

logger:
ota:
wifi:
...
```

---

## 🏠 Entités créées

| Type       | Nom                       | ID HA (exemple)           |
|------------|---------------------------|---------------------------|
| `light`    | Variateur Lumière 01–08   | `light.variateur_lumiere_01` |
| `sensor`   | Signal WiFi               | `sensor.signal_wifi`      |
| `sensor`   | Temps d'utilisation       | `sensor.temps_utilisation`|
| `sensor`   | Adresse IP                | `sensor.adresse_ip`       |
| `sensor`   | Adresse MAC               | `sensor.adresse_mac`      |
| `sensor`   | SSID Wi-Fi                | `sensor.ssid_wifi`        |
| `sensor`   | BSSID Wi-Fi               | `sensor.bssid_wifi`       |
| `sensor`   | Version CPU (firmware)    | `sensor.cpu_version`      |
| `button`   | Redémarrer le Node        | `button.redemarrer_le_node`|

---

## 🔐 Sécurité

L'intégration communique via l'API native ESPHome (`api:`) avec chiffrement si configuré.

---

## 💡 Exemple d'usages

- Contrôle de l'éclairage architectural (LED dimmables)
- Gradation douce (fade in/out)
- Supervision réseau et état de fonctionnement

---

## 📚 Ressources

- [ESPHome - Monochromatic Light](https://esphome.io/components/light/monochromatic.html)
- [ESPHome - API](https://esphome.io/components/api.html)
- [ESPHome - Output PWM (LEDC)](https://esphome.io/components/output/ledc.html)

---

## 🧑‍💻 Auteur

Développé avec ❤️ par **[@SoFarSoGood86](https://github.com/SoFarSoGood86)**  
N'hésitez pas à ouvrir une [Issue](https://github.com/SoFarSoGood86/dimmer_node_8ch/issues) ou une Pull Request !

---

## 📜 Licence

[MIT](LICENSE)
