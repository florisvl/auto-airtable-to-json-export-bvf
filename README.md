# Airtable JSON Export

Dit project haalt gegevens op uit een Airtable-tabel en slaat deze op in een `data.json`-bestand. De JSON wordt elke 5 minuten automatisch bijgewerkt via GitHub Actions.

## Hoe het werkt

1. **Airtable API**: Het script maakt een API-aanroep naar Airtable om gegevens op te halen.
2. **GitHub Actions**: Het bestand `data.json` wordt elke 5 minuten automatisch bijgewerkt via een geplande GitHub Action.
3. **GitHub Pages**: De JSON is toegankelijk via GitHub Pages om te gebruiken voor statische websites.

### Configuratie

- Sla je API-sleutel, base ID en tabelnaam op in een `.env`-bestand:

```env
AIRTABLE_API_KEY=je_airtable_api_key
AIRTABLE_BASE_ID=je_airtable_base_id
AIRTABLE_TABLE_NAME=je_tabel_naam