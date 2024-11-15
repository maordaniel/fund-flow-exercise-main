import json

from fastapi import APIRouter

from api.schema import FundGraphResponse, ChainId, FundGraphEdge, ChainAddress
from api.utils import try_parse_obj_as

route = APIRouter(
    prefix="/graph",
)


@route.get("/{chain}/{address}", response_model=FundGraphResponse)
def get_address_graph(
        address: str,
        chain: ChainId,
):
    with open('data.json') as user_file:
        file_data = json.loads(user_file.read())
        edges = try_parse_obj_as(list[FundGraphEdge], file_data)
        return FundGraphResponse(edges=edges)