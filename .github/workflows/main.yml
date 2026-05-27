name: Weekly WordPress Blog Post

on:
  schedule:
    - cron: "0 9 * * 1"
  workflow_dispatch:

jobs:
  post-to-wordpress:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Run blog post script
        env:
          WP_USERNAME: ${{ secrets.WP_USERNAME }}
          WP_APP_PASSWORD: ${{ secrets.WP_APP_PASSWORD }}
        run: python bristol_dental_auto_post.py
