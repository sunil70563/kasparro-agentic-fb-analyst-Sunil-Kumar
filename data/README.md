# Dataset Documentation

## Source
Synthetic eCommerce + Facebook Ads dataset provided by Kasparro.

## Schema
- **campaign_name**: Marketing campaign identifier (Note: Contains typos requiring normalization).
- **date**: DD-MM-YYYY format.
- **spend**: Ad spend in USD.
- **impressions/clicks/ctr**: Engagement metrics.
- **roas**: Return on Ad Spend (Revenue / Spend).
- **creative_message**: The actual ad copy text.

## Usage
- Full dataset: `synthetic_fb_ads_undergarments.csv` (4500 rows).
- Sample mode: Set `use_sample_data: true` in `config.yaml` to load top 50 rows.