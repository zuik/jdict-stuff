"""
FastAPI API for jdict.
Pull data from the mongoDB database. 
The collection is words

GET /words/<word>
    Returns the word and its definition
GET /search/<text>
    FTS for words matching text in the sense.gloss field
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Setup the DB connection
async def get_db():
    client = MongoClient("mongodb://biggy.lo:27017/", connect=False)
    db = client.get_database("jdict")
    try:
        yield db
    finally:
        client.close()


@app.get("/words/{word}")
async def get_word(word: str, db: Database = Depends(get_db)):
    """
    Get the word and its definition
    """

    word_data = db.words.find_one({"word": word})
    return word_data


@app.get("/search/{text}")
async def search_words(text: str, db: Database = Depends(get_db)):
    """
    Search for words matching text in the sense.gloss field
    """
    _words = db.words.find({"$text": {"$search": text, "$language": "english"}}).limit(10)
    r = [_w for _w in _words]
    [rr.pop("_id") for rr in r]
    return r    
    
    
