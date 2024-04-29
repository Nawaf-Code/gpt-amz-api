# Amazon Review Analyzer API

## Overview

This project provides an API for extracting and analyzing Amazon product reviews. It uses FastAPI to create an endpoint that receives a product review URL and returns a summary of the reviews using BeautifulSoup for scraping.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- BeautifulSoup4
- Requests
- lxml

## Installation

To run this project, you'll need to install the required Python libraries. You can install these dependencies using the following command:

```sh
pip install -r requirements.txt
```

## Usage
After installing the dependencies, you can start the server using the following command:
```sh
uvicorn app.api:app --host 0.0.0.0 --port 8000
```
## API Endpoint
```sh
POST /analyze-reviews
```
### Description: This endpoint accepts a POST request containing a URL to an Amazon product reviews page and returns a list of parsed reviews.
### Payload:
```sh
{
  "url": "https://www.amazon.com/product-reviews/..."
}
```
