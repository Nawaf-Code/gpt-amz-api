from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup

import requests

app = FastAPI()

class ProductReviewLink(BaseModel):
    url: str

@app.post("/analyze-reviews")
async def analyze_reviews(product: ProductReviewLink):
    try:
        reviews = get_reviews(product.url)
        return {"reviews": reviews}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def convert_review_link(original_url, page_number):

    # Split the URL into parts before and after the "ref" parameter
    url_parts = original_url.split('/ref=')
    base_url = url_parts[0]

    # Replace the existing "ref" parameter with the new one based on page number
    new_ref = f'ref=cm_cr_arp_d_paging_btm_next_{page_number}'

    # Reconstruct the URL with the new "ref" parameter and page number
    # The rest of the query string remains unchanged
    if len(url_parts) > 1:
        query_string = url_parts[1].split('?')[1] if '?' in url_parts[1] else ''
        modified_url = f"{base_url}/{new_ref}?{query_string}&pageNumber={page_number}"
    else:
        modified_url = f"{base_url}/{new_ref}?pageNumber={page_number}"
    
    return modified_url


def get_reviews(url):

    custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'cache-control' : 'no-cache',
    'x-Cache' : 'Miss from cloudfront'
    }

    page_number = 1
    scraped_reviews = []

    while True:

        paginated_url = convert_review_link(url, page_number)

        response = requests.get(paginated_url, headers=custom_headers)
        soup = BeautifulSoup(response.text, "lxml")

        review_elements = soup.select("div.review")

        for review in review_elements:

            r_rating_element = review.select_one("i.review-rating")
            r_rating = r_rating_element.text.replace("out of 5 stars", "") if r_rating_element else None

            r_title_element = review.select_one("a.review-title")
            r_title_span_element = r_title_element.select_one("span:not([class])") if r_title_element else None
            r_title = r_title_span_element.text if r_title_span_element else None

            r_content_element = review.select_one("span.review-text")
            r_content = r_content_element.text if r_content_element else None

            r = {
                "rating": r_rating,
                "title": r_title,
                "content": r_content,
            }

            scraped_reviews.append(r)

        if not soup.select_one("li.a-disabled.a-last"):
            page_number+=1
            #sleep(1) 
        else:
            break

    return scraped_reviews
    pass
