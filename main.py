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

    url_parts = original_url.split('/ref=')
    base_url = url_parts[0]

    new_ref = f'ref=cm_cr_arp_d_paging_btm_next_{page_number}'


    if len(url_parts) > 1:
        query_string = url_parts[1].split('?')[1] if '?' in url_parts[1] else ''
        modified_url = f"{base_url}/{new_ref}?{query_string}&pageNumber={page_number}"
    else:
        modified_url = f"{base_url}/{new_ref}?pageNumber={page_number}"
    
    return modified_url


def get_reviews(url):

    custom_headers = {
    'user-agent': 'YOU USER AGENT',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'cache-control' : 'no-cache',
    'x-Cache' : 'Miss from cloudfront'
    }

    page_number = 1
    scraped_reviews = []

    while True and page_number < 11:

        paginated_url = convert_review_link(url, page_number)

        response = requests.get(paginated_url, headers=custom_headers)
        print('start with: ', paginated_url)
        soup = BeautifulSoup(response.text, "lxml")



        review_elements = soup.select("div.a-section.a-spacing-none.review-views.celwidget")

        print(review_elements)

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
            print('page_number: ', page_number)
            page_number+=1
            #sleep(1) 
        else:
            break

    return scraped_reviews