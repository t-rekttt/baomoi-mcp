import httpx
import hmac
import hashlib
import json
import time
from typing import Literal, List
from dataclasses import dataclass
from urllib.parse import quote
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Baomoi")

# Constants
BASE_API_URL = 'https://w-api.baomoi.com'
SECRET = '882QcNXV4tUZbvAsjmFOHqNC1LpcBRKW'
VERSION = '0.7.16'
API_KEY = 'kI44ARvPwaqL7v0KuDSM0rGORtdY1nnw'

@dataclass
class Topic:
    value: str
    id: str

@dataclass
class TopicList:
    topic: List[Topic]

@dataclass
class Content:
    value: str
    id: str

@dataclass
class ContentList:
    article: List[Content]

def hmac_sign(path, data_dict):
    sorted_items = sorted(data_dict.items(), key=lambda x: x[0])
    data_str = ''.join(f"{k}={quote(str(v), safe="!~*'()")}" for k, v in sorted_items)
    payload = path + data_str

    signature = hmac.new(
        SECRET.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    return signature

@mcp.tool()
def list_by_type(list_type: int = 1, list_id: int = 0, page: int = 1, ctime: int = int(time.time()), version: str = VERSION):
    """
    Get a list of news by type from the Baomoi (newspaper) API.
    
    Args:
        list_type (int): The type of list to retrieve. Defaults to 1.
        list_id (int): The ID of the list. Defaults to 0.
        page (int): The page number to retrieve. Defaults to 1.
        ctime (int): Current timestamp. Defaults to current time.
        version (str): API version. Defaults to VERSION constant.
        
    Returns:
        dict: JSON response from the API containing the list of content items
    """
    path = '/api/v1/content/get/list-by-type'
    params = {
        'listType': list_type,
        'listId': list_id,
        'page': page,
        'ctime': ctime,
        'version': version,
    }
    signature = hmac_sign(path, params)
    return httpx.get(BASE_API_URL + path, params = params | {
        'sig': signature,
        'apiKey': API_KEY
    }).json()

@mcp.tool()
def search(keyword: str, type_: Literal['content', 'topic'] = 'content', size: int = 10) -> TopicList | ContentList:
    """
    Search for content or topics on Baomoi.
    
    Args:
        keyword (str): The search query term
        type_ (Literal['content', 'topic']): Type of search - either 'content' or 'topic'. Defaults to 'content'.
        size (int): Number of results to return. Defaults to 10.
        
    Returns:
        dict: JSON response containing search results
    """
    params = {
        'platform': 1,
        'types': type_,
        'query': keyword,
        'size': size
    }

    return httpx.get('https://ac-data.baomoi.com/get', params = params).json()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')