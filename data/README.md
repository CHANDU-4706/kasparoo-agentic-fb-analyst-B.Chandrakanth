# Data

This directory contains the datasets used for the Kasparro Agentic FB Analyst.

## Files

-   `sample_fb_ads.csv`: A small subset (100 rows) of the full dataset, used for testing and development. This file is safe to commit to version control.
-   `synthetic_fb_ads_undergarments.csv`: The full synthetic dataset provided for the assignment. **Do not commit this file.** It is ignored by `.gitignore`.

## Usage

To switch between the sample and full dataset, edit `config/config.yaml`:

```yaml
use_sample_data: true  # Use sample_fb_ads.csv
# use_sample_data: false # Use synthetic_fb_ads_undergarments.csv
```
